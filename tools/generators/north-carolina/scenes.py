"""Hero scenes for the North Carolina site — layered-silhouette SVG in the state palette
(Carolina blue deepened to navy, longleaf green, brick red, sea-oat gold, warm sand)."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6f2e9"/><stop offset="1" stop-color="#cfe3f3"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=60, c="#e9c46a"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".6"/>'
def ground(y, fill, op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def ridge(pts, fill, op="1"):
    """A mountain ridge line from (x, y) points, closed to the bottom."""
    d = "M" + " L".join(f"{x} {y}" for x, y in pts) + "V360H0Z"
    return f'<path d="{d}" fill="{fill}" opacity="{op}"/>'
def longleaf(x, y, s=1.0, f="#3e6b3a"):
    """Longleaf pine: tall bare trunk, tufted crown."""
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-4" y="-120" width="8" height="120" fill="#5a4030"/>'
            f'<path d="M-42-120c10-30 30-44 42-40 12-4 32 10 42 40-14-6-28-4-42 6-14-10-28-12-42-6z" fill="{f}"/>'
            f'<path d="M-30-150c8-22 22-30 30-26 8-4 22 4 30 26-10-4-20-2-30 6-10-8-20-10-30-6z" fill="{f}"/></g>')
def oak(x, y, s=1.0, f="#3e6b3a"):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-6" y="-34" width="12" height="38" fill="#4a3728"/>'
            f'<path d="M-64-34c-22-30 8-72 52-62 22-30 74-20 74 12 32 0 42 42 10 52-12 20-52 20-74 6-22 14-64 10-62-8z" fill="{f}"/></g>')
def dogwood(x, y, s=1.0):
    """A small dogwood: dark branches, pale four-petal blossoms."""
    bl = ''.join(f'<circle cx="{dx}" cy="{dy}" r="5" fill="#fbf7ef" stroke="#e9c46a" stroke-width="1"/>' for dx, dy in
                 [(-30,-60),(-12,-74),(8,-62),(26,-72),(38,-52),(-40,-42),(-6,-46),(20,-40),(0,-88),(-22,-24),(30,-26)])
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0v-40M0-40l-30-24M0-40l32-30M0-60l-14-24M0-60l22-28M-20-56l-20-2" stroke="#4a3728" stroke-width="4" fill="none" stroke-linecap="round"/>{bl}</g>')
def seaoats(xs, y, h=26):
    return '<g>' + ''.join(f'<path d="M{x} {y}q-3-{h//2} 2-{h}" stroke="#b07a1a" stroke-width="2" fill="none"/><ellipse cx="{x+2}" cy="{y-h}" rx="3" ry="8" fill="#c9a24a"/>' for x in xs) + '</g>'
def barn(x, y, s=1.0):
    """A tobacco barn: tall, narrow, tin roof, brick-red weathered boards."""
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-34" y="-96" width="68" height="96" fill="#8a4a3a"/>'
            '<path d="M-42-96l42-26 42 26z" fill="#6b5a4a"/><rect x="-10" y="-40" width="20" height="40" fill="#4a3728"/>'
            '<rect x="-52" y="-58" width="18" height="58" fill="#7a4232"/><path d="M-56-58l22-12v12z" fill="#6b5a4a"/></g>')

def blueridge():
    """The Blue Ridge Parkway: stacked hazy ridges, a stone overlook wall, a dogwood in bloom."""
    r1 = ridge([(0,190),(160,150),(300,176),(460,128),(620,170),(800,120),(960,160),(1120,110),(1300,156),(1440,130)], "#a9c6de")
    r2 = ridge([(0,230),(180,200),(340,226),(520,186),(700,222),(880,190),(1060,224),(1240,196),(1440,214)], "#6e9bc0")
    r3 = ridge([(0,270),(200,250),(400,272),(600,244),(800,270),(1000,250),(1200,274),(1440,256)], "#3b6e9a")
    r4 = ridge([(0,306),(240,292),(480,310),(720,290),(960,308),(1200,292),(1440,304)], "#1f4e79")
    wall = '<rect x="0" y="330" width="1440" height="30" fill="#6d665b"/>' + ''.join(f'<rect x="{x}" y="{332 + (i % 2) * 14}" width="34" height="12" fill="#8a8275" opacity=".8"/>' for i, x in enumerate(range(10, 1440, 46)))
    return wrap(sun(1180, 110, 62) + r1 + r2 + r3 + r4 + wall + dogwood(180, 332, 1.1) + longleaf(1300, 332, .7, "#2f5430"))
def hatteras():
    """Cape Hatteras: the spiral-striped lighthouse on a dune line, sea oats, the Atlantic behind."""
    sea = '<path d="M0 232L1440 224V360H0Z" fill="#2b7aa8"/>' + '<path d="M0 250C300 242 600 258 900 248 1200 240 1350 254 1440 248V360H0Z" fill="#1f5f8a" opacity=".8"/>'
    dune = '<path d="M0 300C260 268 520 312 780 284 1040 258 1240 300 1440 280V360H0Z" fill="#e8dcc0"/>'
    lh = ('<g transform="translate(720 300)"><path d="M-30 0L-20-200h40L30 0z" fill="#f4f1ea"/>'
          '<clipPath id="lhc"><path d="M-30 0L-20-200h40L30 0z"/></clipPath>'
          '<g clip-path="url(#lhc)">' + ''.join(f'<path d="M-40 {y}l80 -22v20l-80 22z" fill="#1c2630"/>' for y in range(-190, 20, 44)) + '</g>'
          '<rect x="-24" y="-214" width="48" height="16" fill="#1c2630"/><rect x="-16" y="-240" width="32" height="26" fill="#1c2630"/>'
          '<rect x="-12" y="-236" width="24" height="18" fill="#e9c46a" opacity=".9"/><path d="M-18-240l18-14 18 14z" fill="#1c2630"/>'
          '<rect x="-36" y="-14" width="72" height="14" fill="#a63d2a"/></g>')
    return wrap(sun(1160, 108, 64) + sea + dune + lh + seaoats(range(40, 700, 26), 318) + seaoats(range(780, 1440, 26), 312))
def charlotte():
    """The Charlotte skyline: the crown-topped tower and its neighbours, oaks in the foreground."""
    b = '<g fill="#1f4e79">' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in
        [(430,190,36),(474,150,40),(524,120,44),(578,166,30),(616,96,56),(682,140,40),(730,110,48),(788,170,34),(830,132,44),(884,154,52),(946,186,40),(996,168,30)]) + '</g>'
    b += '<path d="M616 96l10-20 8 14 10-24 10 24 8-14 10 20z" fill="#1f4e79"/>'  # the crown
    w = '<g fill="#e9c46a" opacity=".7">' + ''.join(f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in [(536,140),(548,160),(630,124),(644,150),(742,130),(758,156),(842,150),(898,176),(690,170)]) + '</g>'
    return wrap(sun(1200, 100, 52) + '<path d="M0 262L1440 240V360H0Z" fill="#cfe3f3"/>' + b + w + ground(318, "#3e6b3a") + oak(200, 318, 1.0) + oak(1220, 316, .9))
def raleigh():
    """Raleigh: the old State Capitol dome among oaks — the City of Oaks."""
    cap = ('<g fill="#c9c3b3"><rect x="560" y="236" width="320" height="124"/><rect x="646" y="186" width="148" height="56"/>'
           '<path d="M646 190a74 74 0 0 1 148 0z"/><rect x="712" y="146" width="16" height="42"/><circle cx="720" cy="142" r="8"/>'
           '<rect x="470" y="268" width="90" height="92"/><rect x="880" y="268" width="90" height="92"/></g>'
           '<g fill="#8a8275">' + ''.join(f'<rect x="{x}" y="262" width="10" height="28"/>' for x in range(586, 870, 30)) + '</g>')
    return wrap(sun(220, 110, 50) + '<path d="M0 272C300 254 600 270 1440 250V360H0Z" fill="#cfe3f3"/>' + cap + ground(332, "#3e6b3a")
                + oak(300, 340, 1.1) + oak(1120, 338, 1.0) + oak(1340, 342, .7) + dogwood(440, 340, .8))
def tobacco():
    """Coastal Plain farmland: a tobacco barn, longleaf pines, flat fields to the horizon."""
    rows = ''.join(f'<path d="M0 {y}L1440 {y - 4}" stroke="#7a9a5a" stroke-width="2" opacity=".55"/>' for y in range(300, 360, 9))
    return wrap(sun(1180, 116, 60) + '<path d="M0 262L1440 250V360H0Z" fill="#b8c9a0"/>' + ground(292, "#8fae6a") + rows
                + barn(360, 300, 1.0) + barn(1060, 302, .8) + longleaf(180, 300, .9) + longleaf(1280, 300, 1.0) + longleaf(1340, 302, .7))
def dunes():
    """Outer Banks: dune ridges, sea oats, a fishing pier reaching into the sound."""
    pier = '<rect x="880" y="280" width="320" height="8" fill="#6d5a45"/>' + ''.join(f'<rect x="{x}" y="288" width="6" height="34" fill="#5a4a3c"/>' for x in range(900, 1200, 48))
    gull = '<g fill="none" stroke="#1c2630" stroke-width="3" stroke-linecap="round"><path d="M520 140q12-10 24 0M544 140q12-10 24 0"/><path d="M640 170q10-8 20 0M660 170q10-8 20 0"/></g>'
    return wrap(sun(1160, 112, 64) + '<path d="M0 258L1440 248V360H0Z" fill="#2b7aa8"/>' + '<path d="M0 274C300 266 600 282 900 272 1200 264 1350 278 1440 272V360H0Z" fill="#1f5f8a" opacity=".8"/>'
                + '<path d="M0 320C200 286 420 330 640 300 860 274 1020 318 1440 296V360H0Z" fill="#e8dcc0"/>' + '<path d="M0 340C260 320 520 346 780 330 1040 316 1240 344 1440 330V360H0Z" fill="#d9c9a4"/>'
                + pier + gull + seaoats(range(30, 700, 22), 330, 28) + seaoats(range(1240, 1440, 22), 322, 24))
def longleafs():
    """The Sandhills: a longleaf pine savanna on sandy ground, wiregrass beneath."""
    grass = ''.join(f'<path d="M{x} 336q-2-10 2-18" stroke="#8fae6a" stroke-width="2" fill="none"/>' for x in range(20, 1440, 18))
    pines = ''.join(longleaf(x, 330, s, f) for x, s, f in [(120,1.0,"#3e6b3a"),(260,.8,"#2f5430"),(420,1.1,"#3e6b3a"),(640,.9,"#2f5430"),(860,1.0,"#3e6b3a"),(1040,.75,"#2f5430"),(1220,1.05,"#3e6b3a"),(1380,.8,"#2f5430")])
    return wrap(sun(1170, 116, 60) + '<path d="M0 262C300 246 700 272 1440 246V360H0Z" fill="#cfe3f3"/>' + ground(320, "#e2d3ad") + grass + pines)
def piedmont():
    """The Piedmont: rolling red-clay hills, a brick mill with its water tower, dogwoods."""
    mill = ('<g><rect x="560" y="236" width="300" height="124" fill="#a63d2a"/><rect x="580" y="256" width="20" height="30" fill="#e3eef7"/>'
            '<rect x="620" y="256" width="20" height="30" fill="#e3eef7"/><rect x="660" y="256" width="20" height="30" fill="#e3eef7"/><rect x="700" y="256" width="20" height="30" fill="#e3eef7"/>'
            '<rect x="740" y="256" width="20" height="30" fill="#e3eef7"/><rect x="780" y="256" width="20" height="30" fill="#e3eef7"/><rect x="820" y="256" width="20" height="30" fill="#e3eef7"/>'
            '<rect x="880" y="200" width="14" height="160" fill="#8a8275"/><rect x="900" y="200" width="14" height="160" fill="#8a8275"/>'
            '<ellipse cx="897" cy="196" rx="34" ry="22" fill="#6d665b"/><rect x="600" y="150" width="14" height="86" fill="#7a3a2a"/></g>')
    return wrap(sun(1180, 112, 58) + ridge([(0,236),(240,214),(480,240),(720,212),(960,238),(1200,216),(1440,232)], "#b8c9a0")
                + ridge([(0,280),(260,262),(520,286),(780,266),(1040,288),(1300,270),(1440,282)], "#8fae6a") + mill
                + ground(330, "#3e6b3a") + oak(220, 330, 1.0) + dogwood(1180, 332, 1.0) + dogwood(1320, 334, .8))
def riverport():
    """Wilmington: the Cape Fear riverfront — a battleship silhouette, a bridge, live oaks with moss."""
    bridge = ('<g fill="none" stroke="#1c2630" stroke-width="5"><path d="M900 250H1440"/><path d="M1000 250V206M1180 250V206"/><path d="M1000 206H1180"/>'
              '<path d="M1000 206L1090 236L1180 206"/></g>')
    ship = ('<g fill="#46535e"><path d="M300 296l40-30h340l60 30z"/><rect x="440" y="230" width="120" height="36"/><rect x="480" y="200" width="40" height="30"/>'
            '<rect x="496" y="170" width="8" height="30"/><path d="M400 250h30v16h-30zM600 250h30v16h-30z"/></g>')
    moss = ''.join(f'<path d="M{x} {y}q2 18 -2 34" stroke="#9db8a0" stroke-width="2" fill="none"/>' for x, y in [(150,246),(178,240),(206,250),(1250,244),(1276,238),(1302,250)])
    return wrap(sun(1160, 110, 60) + '<path d="M0 262L1440 250V360H0Z" fill="#cfe3f3"/>' + ship + bridge + ground(296, "#3b6e9a") + ground(314, "#1f5f8a", ".85")
                + '<path d="M0 334C300 326 600 342 900 334 1200 326 1350 340 1440 334V360H0Z" fill="#6d665b"/>' + oak(180, 300, 1.1, "#2f5430") + oak(1280, 300, 1.0, "#2f5430") + moss)

SCENES = {"blueridge": blueridge(), "hatteras": hatteras(), "charlotte": charlotte(), "raleigh": raleigh(), "tobacco": tobacco(),
          "dunes": dunes(), "longleaf": longleafs(), "piedmont": piedmont(), "riverport": riverport()}
