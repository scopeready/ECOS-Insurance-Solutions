#!/usr/bin/env python3
"""
Build one generator-based state section into this repository.

    python3 tools/build_state.py texas            # rebuilds <repo>/texas/ from tools/generators/texas/
    python3 tools/build_state.py hawaii --og      # also renders og-image.png (needs Pillow)

The generator engine (tools/generators/<state>/generate.py) was written for a
site living at the root of its own domain, so it emits root-absolute links
(`/about`, `/site.css`) and canonicals built from SITE["url"]. This script:

  1. runs the generator into a scratch directory (ECOS_OUT),
  2. prefixes every root-absolute reference with `/<state>` and normalises the
     new-domain URLs (`.../<state>/` -> `.../<state>`, no `.html`), using the
     same rewriters as scripts/migrate.py,
  3. drops the per-domain files the engine writes (CNAME, vercel.json,
     robots.txt, .nojekyll) — the consolidated site has one of each at the root,
  4. copies the result over <repo>/<state>/, keeping darin.jpg and og-image.png
     if the generator does not produce them.

SITE["url"] in the state's content_site.py must be
`https://www.ecosinsurancesolutions.com/<state>` (no trailing slash).
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from migrate import NEW_HOST, rewrite_abs_links, rewrite_domains, clean_path, TEXT_EXT  # noqa: E402

DROP = {"CNAME", "vercel.json", "robots.txt", ".nojekyll"}
KEEP_IF_MISSING = {"darin.jpg", "og-image.png"}


def normalise_new_host(text, state):
    """The engine builds canonicals as SITE_URL + '/' for the home page and never strips .html."""
    base = re.escape(f"{NEW_HOST}/{state}")

    def repl(m):
        path = m.group(1) or ""
        if path in ("", "/"):
            return f"{NEW_HOST}/{state}"
        return NEW_HOST + clean_path(f"/{state}{path}")
    return re.sub(base + r"(/[^\s\"'<>)]*)?", repl, text)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    state = sys.argv[1]
    gen = REPO / "tools" / "generators" / state
    if not (gen / "generate.py").is_file():
        sys.exit(f"no generator at {gen}")
    out = REPO / state
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, ECOS_OUT=tmp)
        subprocess.run([sys.executable, str(gen / "generate.py")], cwd=gen, env=env, check=True)
        if "--og" in sys.argv:
            subprocess.run([sys.executable, str(gen / "og.py")], cwd=gen, env=env, check=True)
        tmp = Path(tmp)
        for f in list(tmp.iterdir()):
            if f.name in DROP:
                f.unlink()
        for f in tmp.rglob("*"):
            if f.is_file() and f.suffix.lower() in TEXT_EXT:
                text = f.read_text(encoding="utf-8")
                if f.suffix.lower() in (".html", ".htm"):
                    text = rewrite_abs_links(text, state)
                elif f.suffix.lower() == ".css":
                    text = re.sub(r"url\((['\"]?)/(?!/)", rf"url(\1/{state}/", text)
                text = rewrite_domains(text)
                text = normalise_new_host(text, state)
                f.write_text(text, encoding="utf-8")
        keep = {}
        if out.is_dir():
            for name in KEEP_IF_MISSING:
                if (out / name).is_file() and not (tmp / name).is_file():
                    keep[name] = (out / name).read_bytes()
            shutil.rmtree(out)
        shutil.copytree(tmp, out)
        for name, data in keep.items():
            (out / name).write_bytes(data)
        if not (out / "darin.jpg").is_file():
            shutil.copy2(REPO / "texas" / "darin.jpg", out / "darin.jpg")  # the same headshot every section uses
    n = len(list(out.glob("*.html")))
    print(f"{state}: {n} pages written to {out.relative_to(REPO)}/")


if __name__ == "__main__":
    main()
