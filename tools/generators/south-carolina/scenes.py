"""Hero scenes for the South Carolina site — layered-silhouette SVG in the brand palette.
Palette: indigo (#1f2d5c / #14204a), palmetto green (#2e6b48 / #3f7f57), marsh gold (#c9a84a / #ad7a1a),
oyster-tabby paper (#f6f2e9), Charleston pastels (#f3d9d2 rose, #dfe6f0 haze, #e9dfc8 sand), terracotta (#b5573f)."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6f2e9"/><stop offset="1" stop-color="#dfe6f0"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
DUSK = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6f2e9"/><stop offset=".55" stop-color="#f3d9d2"/><stop offset="1" stop-color="#dfe6f0"/></linearGradient></defs>'
        '<rect width="1440" height="360" fill="url(#sky)"/>')
def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=60, c="#c9a84a"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".6"/>'
def ground(y, fill, op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def water(y, fill="#2f4f86", op="1"):
    return (f'<path d="M0 {y}C240 {y-4} 480 {y+4} 720 {y} 960 {y-4} 1200 {y+4} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
            + ''.join(f'<path d="M{x} {y+18+i*14}c30-5 60 5 90 0" stroke="#e9f0f6" stroke-width="2" fill="none" opacity=".45"/>' for i, x in enumerate((120, 520, 960, 300, 1240))))
def palmetto(x, y, s=1.0, trunk="#3b2f22", frond="#2e6b48"):
    fronds = ''.join(f'<path d="M0 -70 L{dx} {dy}" stroke="{frond}" stroke-width="7" stroke-linecap="round"/>'
                     for dx, dy in [(-44, -96), (-52, -66), (-38, -42), (44, -96), (52, -66), (38, -42), (-14, -108), (14, -108), (0, -112)])
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-6 0c-2-30 2-50 6-70c4 20 8 40 6 70z" fill="{trunk}"/>'
            f'{fronds}<circle cx="0" cy="-70" r="9" fill="{frond}"/></g>')
def liveoak(x, y, s=1.0, moss=True):
    m = ('<g stroke="#b9b391" stroke-width="3" opacity=".8"><path d="M-40-40v34M-18-52v40M22-50v36M46-38v28M0-60v30"/></g>' if moss else '')
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-8" y="-34" width="16" height="38" fill="#3b2f22"/>'
            '<path d="M-96-34c-26-34 12-78 58-64 22-32 78-24 84 10 34-2 48 42 14 56-8 24-56 26-82 10-24 18-70 12-74-12z" fill="#2e6b48"/>' + m + '</g>')
def pine(x, y, h, w, f="#2e6b48"):
    step = h / 4; parts = ''.join(f"M{x} {y-h+i*step:.0f}l{w*(0.45+0.28*i):.0f} {step*1.35:.0f}h{-2*w*(0.45+0.28*i):.0f}z" for i in range(3))
    return f'<path d="{parts}" fill="{f}"/><rect x="{x-3}" y="{y-8}" width="6" height="12" fill="#3b2f22"/>'
def marshgrass(y, x0=0, x1=1440, step=16, c="#c9a84a"):
    return '<g>' + ''.join(f'<path d="M{x} {y}c-2-12 2-22 4-30c2 10 4 20 2 30z" fill="{c}"/>' for x in range(x0, x1, step)) + '</g>'
def egret(x, y):
    return (f'<g transform="translate({x} {y})" fill="#fffdf8" stroke="#b9b391" stroke-width="1"><ellipse cx="0" cy="0" rx="16" ry="8"/>'
            '<path d="M12-4c6-16 4-30 2-40" stroke="#fffdf8" stroke-width="3" fill="none"/><circle cx="14" cy="-42" r="4"/><path d="M-4 8v22M4 8v22" stroke="#3b2f22" stroke-width="2"/></g>')

def battery():
    # Charleston: pastel row houses along the Battery, palmettos, harbor water, evening sun.
    colors = ["#f3d9d2", "#e9dfc8", "#cfdcc9", "#dfe6f0", "#f0e2b8", "#e3cfd8", "#f3d9d2", "#d9e4d0"]
    houses = ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{300-y}" fill="{colors[i % len(colors)]}" stroke="#b9b391" stroke-width="1"/>'
                     + f'<rect x="{x}" y="{y-14}" width="{w}" height="14" fill="#8a7a66"/>'
                     + ''.join(f'<rect x="{x+10+k*22}" y="{y+18+r*40}" width="10" height="20" fill="#14204a" opacity=".55"/>' for k in range(w // 24) for r in range((300 - y - 30) // 40))
                     for i, (x, y, w) in enumerate([(360, 190, 70), (434, 176, 84), (522, 200, 64), (590, 170, 92), (686, 196, 70), (760, 182, 80), (844, 206, 62), (910, 180, 88)]))
    prom = '<rect x="0" y="300" width="1440" height="16" fill="#8a7a66"/><rect x="0" y="296" width="1440" height="4" fill="#b9b391"/>'
    return wrap(sun(1180, 112, 60) + houses + prom + palmetto(300, 300, 1.0) + palmetto(1010, 300, .9) + palmetto(1160, 300, 1.1)
                + water(316, "#2f4f86") + ground(346, "#14204a", ".9"), DUSK)
def harbor():
    # Charleston harbor: cable-stayed bridge silhouette, container crane, water, palmetto.
    tower = lambda x: (f'<path d="M{x-14} 300V120l14-30 14 30v180z" fill="#1f2d5c"/>'
                       + ''.join(f'<path d="M{x} {130+i*10}L{x-40-i*44} 262M{x} {130+i*10}L{x+40+i*44} 262" stroke="#1f2d5c" stroke-width="2" opacity=".8"/>' for i in range(6)))
    deck = '<path d="M60 262H1380" stroke="#1f2d5c" stroke-width="10"/>'
    crane = '<g fill="#8a7a66"><rect x="1240" y="200" width="10" height="100"/><rect x="1300" y="200" width="10" height="100"/><rect x="1200" y="196" width="180" height="10"/><rect x="1230" y="206" width="6" height="40"/></g>'
    return wrap(sun(230, 110, 56) + tower(500) + tower(940) + deck + crane + water(300, "#2f4f86") + ground(340, "#1f2d5c", ".9") + palmetto(120, 336, .8))
def marsh():
    # Lowcountry: spartina marsh gold, a tidal creek, a live oak with moss, an egret.
    creek = '<path d="M0 320C260 300 420 340 700 322 980 304 1200 336 1440 318V360H0Z" fill="#2f4f86" opacity=".9"/>'
    return wrap(sun(1170, 116, 62) + '<path d="M0 262C300 246 700 270 1440 250V360H0Z" fill="#cfd6c8"/>' + ground(292, "#c9a84a")
                + marshgrass(292, 0, 1440, 14) + creek + marshgrass(346, 0, 1440, 18, "#ad7a1a") + liveoak(300, 290, 1.1) + egret(1100, 286))
def pier():
    # Myrtle Beach: long pier over the Atlantic, waves, sand, an umbrella.
    p = ('<rect x="760" y="246" width="560" height="8" fill="#8a7a66"/><rect x="760" y="238" width="560" height="4" fill="#b9b391"/>'
         + ''.join(f'<rect x="{x}" y="254" width="6" height="48" fill="#6a5a48"/><rect x="{x+22}" y="254" width="6" height="48" fill="#6a5a48"/>' for x in range(780, 1320, 54))
         + '<rect x="1240" y="200" width="70" height="40" fill="#8a7a66"/><path d="M1236 200l39-20 39 20z" fill="#b5573f"/>')
    umb = '<g transform="translate(300 300)"><rect x="-2" y="-40" width="4" height="46" fill="#3b2f22"/><path d="M-40-40a40 18 0 0 1 80 0z" fill="#b5573f"/><path d="M-40-40a40 18 0 0 1 80 0" stroke="#f6f2e9" stroke-width="3" fill="none"/></g>'
    return wrap(sun(1160, 110, 64) + '<path d="M0 250L1440 244V360H0Z" fill="#cfd6c8"/>' + water(268, "#2f4f86") + water(292, "#4f6fa6", ".8") + p
                + '<path d="M0 330C300 320 600 340 900 330 1200 322 1350 336 1440 330V360H0Z" fill="#e9dfc8"/>' + umb)
def foothills():
    # Blue Ridge foothills: layered ridges, a Table Rock-like face, pines.
    return wrap(sun(1180, 116, 62) + '<path d="M0 236C160 200 300 250 460 214 600 184 700 220 820 206 960 190 1100 230 1440 200V360H0Z" fill="#b9c2d6"/>'
                + '<path d="M0 270C200 250 300 286 440 262 520 246 560 200 640 200 700 200 740 250 860 262 1000 276 1200 250 1440 258V360H0Z" fill="#7d8fb0"/>'
                + '<path d="M560 236l80-40 80 40z" fill="#8a7a66"/>'
                + '<path d="M0 300C260 286 520 310 780 296 1040 282 1240 306 1440 292V360H0Z" fill="#3f7f57"/>'
                + ''.join(pine(x, 326, h, w) for x, h, w in [(120, 100, 28), (180, 74, 20), (420, 96, 26), (940, 110, 30), (1000, 80, 22), (1300, 98, 26), (1360, 66, 18)])
                + ground(326, "#2e6b48"))
def falls():
    # Greenville: the Reedy River falls and the curve of a pedestrian bridge over them.
    bridge = ('<path d="M420 214C600 150 840 150 1020 214" stroke="#1f2d5c" stroke-width="8" fill="none"/>'
              + ''.join(f'<path d="M{x} {y}V214" stroke="#1f2d5c" stroke-width="3"/>' for x, y in [(500, 184), (580, 166), (660, 158), (740, 156), (820, 158), (900, 166), (980, 184)])
              + '<rect x="410" y="210" width="620" height="6" fill="#1f2d5c"/>')
    rock = '<path d="M0 262C200 250 380 270 520 258 620 250 660 240 720 240 780 240 820 250 920 258 1080 270 1260 250 1440 262V360H0Z" fill="#8a7a66"/>'
    fall = '<path d="M600 240c-10 40 10 70 0 120h140c-10-50 10-80 0-120z" fill="#dfe6f0" opacity=".95"/><path d="M620 260v90M660 250v100M700 262v88" stroke="#fffdf8" stroke-width="3" opacity=".8"/>'
    trees = liveoak(200, 262, .9, False) + liveoak(1220, 262, 1.0, False)
    return wrap(sun(1180, 110, 58) + bridge + rock + fall + trees + water(340, "#2f4f86"))
def peaches():
    # The Ridge and Upstate: peach-orchard rows across low hills.
    tree = lambda x, y, s: (f'<g transform="translate({x} {y}) scale({s})"><rect x="-3" y="-22" width="6" height="24" fill="#3b2f22"/>'
                            '<circle cx="0" cy="-34" r="22" fill="#3f7f57"/><circle cx="-8" cy="-30" r="4" fill="#e8956b"/><circle cx="9" cy="-40" r="4" fill="#e8956b"/><circle cx="4" cy="-24" r="4" fill="#e8956b"/></g>')
    rows = ''.join(tree(x, y, s) for y, s, off in [(296, .7, 0), (318, .85, 30), (346, 1.0, 60)] for x in range(off + 40, 1440, 90))
    return wrap(sun(1170, 116, 60) + '<path d="M0 262C300 236 600 270 1440 240V360H0Z" fill="#cfd6c8"/>' + ground(300, "#9db98a") + ground(326, "#3f7f57", ".9") + rows)
def cotton():
    # The Pee Dee: flat cotton rows, a tobacco barn, pines on the horizon.
    barn = '<g fill="#8a7a66"><rect x="1080" y="236" width="90" height="70"/><path d="M1076 236l49-30 49 30z"/><rect x="1176" y="256" width="40" height="50" opacity=".8"/></g>'
    bolls = '<g>' + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#fffdf8"/>' for y, off in [(314, 0), (332, 12), (350, 24)] for x in range(off + 20, 1440, 26)) + '</g>'
    return wrap(sun(700, 112, 66) + ''.join(pine(x, 262, h, w, "#7d8fb0") for x, h, w in [(60, 60, 16), (100, 48, 14), (300, 58, 16), (1300, 62, 16), (1350, 48, 14), (1400, 56, 16)])
                + '<path d="M0 262L1440 258V360H0Z" fill="#9db98a"/>' + barn + ground(306, "#3f7f57") + ground(324, "#2e6b48", ".9") + ground(342, "#3b2f22", ".85") + bolls)
def statehouse():
    # Columbia: the State House dome and portico, palmettos.
    dome = ('<g fill="#9a8f80"><rect x="540" y="236" width="360" height="124"/><rect x="640" y="176" width="160" height="62"/><path d="M640 180a80 80 0 0 1 160 0z"/>'
            '<rect x="714" y="130" width="12" height="48"/><rect x="450" y="270" width="90" height="90"/><rect x="900" y="270" width="90" height="90"/></g>'
            '<path d="M660 180a60 60 0 0 1 120 0z" fill="#b08d5c" opacity=".7"/>'
            + '<g fill="#f6f2e9" opacity=".9">' + ''.join(f'<rect x="{x}" y="250" width="12" height="70"/>' for x in range(570, 870, 34)) + '</g>'
            + '<g fill="#14204a" opacity=".5">' + ''.join(f'<rect x="{x}" y="288" width="10" height="26"/>' for x in range(470, 540, 30)) + ''.join(f'<rect x="{x}" y="288" width="10" height="26"/>' for x in range(910, 980, 30)) + '</g>')
    return wrap(sun(210, 110, 50) + '<path d="M0 270C300 250 600 268 1440 246V360H0Z" fill="#cfd6c8"/>' + dome + palmetto(330, 340, 1.0) + palmetto(1120, 340, 1.0) + ground(334, "#3f7f57"))
def horse():
    # Aiken horse country: rail fences, a live oak, a horse silhouette, sandy track.
    fence = ''.join(f'<rect x="{x}" y="292" width="6" height="44" fill="#5a4a3c"/>' for x in range(40, 1440, 90)) + '<rect x="0" y="304" width="1440" height="4" fill="#5a4a3c"/><rect x="0" y="322" width="1440" height="4" fill="#5a4a3c"/>'
    h = ('<g transform="translate(1040 292)" fill="#3b2f22"><path d="M-60 0c-4-30 6-50 30-56 20-4 40-4 58 0 6-14 14-22 26-26l12 8 8-6-2 18c8 6 6 16-2 20l-14 2c-2 12-4 22-6 40h-10l-4-26-10 2-6 24h-10l0-24c-14 2-28 2-40-2l-4 26h-10l-2-28c-8-2-12-8-14-16z"/></g>')
    return wrap(sun(1180, 116, 60) + '<path d="M0 266C300 246 600 266 1440 246V360H0Z" fill="#9db98a"/>' + ground(300, "#3f7f57") + liveoak(400, 296, 1.1) + fence + h + ground(344, "#e9dfc8", ".95"))

SCENES = {"battery": battery(), "harbor": harbor(), "marsh": marsh(), "pier": pier(), "foothills": foothills(),
          "falls": falls(), "peaches": peaches(), "cotton": cotton(), "statehouse": statehouse(), "horse": horse()}
