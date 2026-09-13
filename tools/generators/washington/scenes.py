"""Hero scenes for the Washington site — layered-silhouette SVG in the state palette
(Puget Sound grey-blue, evergreen, Cascade snow, apple red). Every `scene` key used in the
content modules must exist in SCENES at the bottom."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f3ee"/><stop offset="1" stop-color="#cfd9df"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
SNOW, FAR, MID, RIDGE = "#eef2f4", "#8fa4b0", "#5a7a8a", "#3f6272"
FIR, FIR_DARK, TRUNK = "#2f5d3f", "#1f4230", "#4a3728"
WATER, WATER_DEEP, SUN, APPLE = "#4f7e93", "#2c5567", "#e7c486", "#b0312a"
FIELD, WHEAT, FOG = "#9db08a", "#c9b26a", "#e7eae5"

def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=60, c=SUN):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".6"/>'
def ground(y, fill, op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def water(y, fill=WATER, op="1"):
    waves = ''.join(f'<path d="M{x} {y+18+i*14}c30-4 60 4 90 0s60-4 90 0" stroke="#e9f1f5" stroke-width="2" fill="none" opacity=".45"/>' for i, x in enumerate((180, 620, 1040)))
    return f'<rect x="0" y="{y}" width="1440" height="{360-y}" fill="{fill}" opacity="{op}"/>' + waves
def peak(cx, base, h, w, fill=MID, snow=0.42):
    """A single mountain: jagged silhouette with an optional snow cap covering the top `snow` fraction."""
    pts = [(cx-w, base), (cx-w*0.55, base-h*0.5), (cx-w*0.3, base-h*0.78), (cx, base-h), (cx+w*0.22, base-h*0.76), (cx+w*0.5, base-h*0.52), (cx+w, base)]
    body = '<polygon points="' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in pts) + f'" fill="{fill}"/>'
    if not snow:
        return body
    t = base - h; sy = t + h * snow
    cap = [(cx, t), (cx+w*0.22, base-h*0.76), (cx+w*0.5*snow/0.42*0.85, sy), (cx+w*0.2, sy-h*0.06), (cx+w*0.05, sy+h*0.05), (cx-w*0.1, sy-h*0.04),
           (cx-w*0.25, sy+h*0.03), (cx-w*0.3*snow/0.42, sy-h*0.02), (cx-w*0.3, base-h*0.78)]
    return body + '<polygon points="' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in cap) + f'" fill="{SNOW}"/>'
def cone(cx, base, h, w):
    """A broad volcanic cone (Rainier, Baker, Adams): snow down to the timberline."""
    body = f'<path d="M{cx-w} {base}C{cx-w*0.55} {base-h*0.35} {cx-w*0.35} {base-h*0.75} {cx-w*0.12} {base-h} L{cx+w*0.1} {base-h}C{cx+w*0.35} {base-h*0.72} {cx+w*0.55} {base-h*0.38} {cx+w} {base}Z" fill="{FAR}"/>'
    snowcap = f'<path d="M{cx-w*0.62} {base-h*0.3}C{cx-w*0.45} {base-h*0.6} {cx-w*0.3} {base-h*0.86} {cx-w*0.12} {base-h} L{cx+w*0.1} {base-h}C{cx+w*0.3} {base-h*0.84} {cx+w*0.45} {base-h*0.62} {cx+w*0.6} {base-h*0.32} L{cx+w*0.45} {base-h*0.36} L{cx+w*0.3} {base-h*0.28} L{cx+w*0.1} {base-h*0.4} L{cx-w*0.1} {base-h*0.3} L{cx-w*0.3} {base-h*0.38} L{cx-w*0.48} {base-h*0.28}Z" fill="{SNOW}"/>'
    return body + snowcap
def fir(x, y, h, w, f=FIR):
    step = h / 4
    parts = ''.join(f"M{x} {y-h+i*step:.0f}l{w*(0.45+0.28*i):.0f} {step*1.35:.0f}h{-2*w*(0.45+0.28*i):.0f}z" for i in range(3))
    return f'<path d="{parts}" fill="{f}"/><rect x="{x-3}" y="{y-8}" width="6" height="12" fill="{TRUNK}"/>'
def treeline(y, fill=FIR_DARK, x0=0, x1=1440, step=26, hs=(54, 40, 66, 46, 60, 36)):
    """A ragged conifer horizon: overlapping narrow triangles."""
    out = []
    for i, x in enumerate(range(x0, x1, step)):
        h = hs[i % len(hs)]
        out.append(f'<path d="M{x} {y}l{step*0.55:.0f} -{h}l{step*0.55:.0f} {h}z"/>')
    return f'<g fill="{fill}">' + ''.join(out) + '</g>'
def ferry(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-90 0l14 18h152l14-18z" fill="{WATER_DEEP}"/><rect x="-78" y="-14" width="156" height="16" rx="3" fill="#f6f7f5"/>'
            f'<rect x="-62" y="-30" width="124" height="18" rx="3" fill="#f6f7f5"/><rect x="-30" y="-42" width="60" height="14" rx="3" fill="#f6f7f5"/>'
            f'<g fill="{WATER_DEEP}" opacity=".7">' + ''.join(f'<rect x="{-56+i*14}" y="-26" width="8" height="8"/>' for i in range(9)) + '</g>'
            f'<rect x="-78" y="-2" width="156" height="4" fill="{FIR}"/></g>')
def gull(x, y):
    return f'<path d="M{x} {y}c8-8 16-8 22 0M{x+22} {y}c6-8 14-8 22 0" stroke="#5a7a8a" stroke-width="2.5" fill="none"/>'

# ------------------------------------------------------------------ scenes
def rainier():
    """Mount Rainier over Puget Sound: cone, foothills, firs, water, a ferry."""
    return wrap(sun(220, 112, 54) + cone(900, 262, 220, 420)
                + f'<path d="M0 250C200 226 380 252 560 236 760 220 940 250 1440 232V360H0Z" fill="{FAR}" opacity=".85"/>'
                + f'<path d="M0 282C260 258 520 290 780 270 1040 254 1240 286 1440 266V360H0Z" fill="{MID}"/>'
                + treeline(300, FIR_DARK, -10, 1450, 24) + water(302, WATER) + ferry(1040, 318, .8) + gull(160, 200) + gull(300, 176)
                + fir(120, 356, 120, 34, FIR) + fir(1330, 356, 100, 30, FIR) + fir(1390, 356, 74, 22, FIR_DARK))
def skyline():
    """Seattle: Space Needle, towers, the Sound and a ferry, Olympics behind."""
    b = f'<g fill="{RIDGE}">' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in
        [(520,196,38),(566,150,32),(606,112,48),(662,164,30),(700,86,44),(752,140,36),(796,124,56),(860,176,30),(898,150,42),(948,166,50),(1006,200,36)]) + '</g>'
    b += f'<path d="M700 86l22-22 22 22z" fill="{RIDGE}"/>'
    needle = (f'<g fill="{RIDGE}"><rect x="436" y="130" width="8" height="180"/><path d="M400 118c0-16 80-16 80 0 0 8-8 12-10 14H410c-2-2-10-6-10-14z"/>'
              f'<ellipse cx="440" cy="116" rx="44" ry="8" fill="{MID}"/><rect x="438" y="72" width="4" height="40"/></g>')
    w = f'<g fill="{SUN}" opacity=".7">' + ''.join(f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in [(618,140),(630,170),(712,120),(724,150),(812,150),(834,170),(910,170),(960,190),(580,180)]) + '</g>'
    return wrap(sun(1200, 104, 52) + peak(180, 262, 120, 200, FAR, .4) + peak(1260, 262, 100, 220, FAR, .38)
                + f'<path d="M0 262L1440 246V360H0Z" fill="{MID}" opacity=".6"/>' + needle + b + w + water(312, WATER) + ferry(240, 332, .9) + gull(1100, 190))
def ferryscene():
    """Kitsap / the Sound: water in front, an island of firs, a ferry crossing, the Olympics behind."""
    return wrap(sun(1170, 110, 58) + peak(300, 250, 130, 260, FAR, .45) + peak(620, 250, 96, 200, FAR, .4) + peak(1000, 250, 150, 300, FAR, .48)
                + f'<path d="M0 262C300 246 700 270 1440 250V360H0Z" fill="{MID}" opacity=".7"/>'
                + treeline(294, FIR_DARK, 420, 1100, 22, (60, 44, 72, 50, 64, 40)) + water(296, WATER) + ferry(760, 330, 1.05)
                + fir(90, 358, 130, 36) + fir(150, 358, 96, 28, FIR_DARK) + fir(1360, 358, 118, 34) + gull(560, 200) + gull(640, 186))
def sanjuans():
    """The San Juan Islands: rounded islands stacked in haze, a sailboat, Mount Baker far off."""
    isl = ''.join(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{f}"/>' for cx, cy, rx, ry, f in
                  [(300, 270, 260, 40, FAR), (1100, 268, 300, 44, FAR), (700, 290, 220, 34, MID), (1300, 300, 200, 40, MID), (180, 306, 240, 44, RIDGE)])
    boat = f'<g transform="translate(900 318)"><path d="M-30 0h60l-8 12h-44z" fill="#f6f7f5"/><rect x="-2" y="-70" width="4" height="70" fill="{TRUNK}"/><path d="M2-66l40 60H2z" fill="#f6f7f5"/><path d="M-2-56l-26 50h26z" fill="{FOG}"/></g>'
    return wrap(sun(1180, 100, 56) + cone(1180, 262, 150, 300) + isl + treeline(306, FIR_DARK, 0, 460, 20, (40, 28, 46, 32))
                + treeline(300, FIR_DARK, 1140, 1450, 20, (38, 26, 44, 30)) + water(310, WATER) + boat + gull(520, 190) + gull(600, 210))
def rainforest():
    """The Olympic rain forest: huge trunks, moss, ferns, fog between the trees."""
    trunks = ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}" rx="6" fill="{f}"/>' for x, y, w, f in
                     [(90, 40, 44, FIR_DARK), (330, 20, 60, "#2a3d33"), (620, 60, 40, FIR_DARK), (860, 0, 70, "#2a3d33"), (1130, 50, 46, FIR_DARK), (1340, 30, 54, "#2a3d33")])
    branches = ''.join(f'<path d="M{x} {y}c-60-10-100 10-140 40" stroke="{FIR_DARK}" stroke-width="10" fill="none" stroke-linecap="round"/>' for x, y in [(330, 120), (860, 90), (1340, 140)])
    moss = ''.join(f'<path d="M{x} {y}c10 30 0 60-8 90" stroke="#5f8a5a" stroke-width="6" fill="none" stroke-linecap="round" opacity=".8"/>' for x, y in [(260, 100), (300, 150), (800, 110), (1310, 120)])
    ferns = ''.join(f'<g transform="translate({x} 340)"><path d="M0 0c-20-30-40-40-70-44M0 0c-6-36-20-60-44-76M0 0c6-36 20-60 44-76M0 0c20-30 40-40 70-44" stroke="{FIR}" stroke-width="5" fill="none" stroke-linecap="round"/></g>' for x in (200, 520, 760, 1040, 1260))
    return wrap(f'<rect width="1440" height="360" fill="{FOG}" opacity=".5"/>' + trunks + branches + moss + f'<rect x="0" y="200" width="1440" height="90" fill="{FOG}" opacity=".35"/>' + ground(330, "#4b6b47") + ferns,
                sky='<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e7eae5"/><stop offset="1" stop-color="#b9c9bf"/></linearGradient></defs><rect width="1440" height="360" fill="url(#sky)"/>')
def cascades():
    """The North Cascades and a mountain lake: sharp snowy peaks, firs, still water."""
    return wrap(sun(200, 100, 48) + peak(360, 262, 200, 220, MID, .5) + peak(720, 262, 250, 260, RIDGE, .46) + peak(1080, 262, 190, 230, MID, .5) + peak(1340, 262, 140, 200, FAR, .42)
                + treeline(290, FIR_DARK, -10, 1450, 22, (56, 40, 70, 48, 62, 38)) + water(292, "#5f8ea3")
                + f'<path d="M0 292C300 300 700 286 1440 296V360H0Z" fill="{WATER}" opacity=".5"/>'
                + fir(70, 358, 126, 34) + fir(1380, 358, 110, 32) + fir(1320, 358, 80, 24, FIR_DARK))
def orchards():
    """Wenatchee and Yakima: orchard rows, red apples, dry hills and a snowy ridge far back."""
    tree = lambda x, y, s: (f'<g transform="translate({x} {y}) scale({s})"><rect x="-4" y="-18" width="8" height="20" fill="{TRUNK}"/>'
                            f'<circle cx="0" cy="-34" r="24" fill="{FIR}"/><circle cx="-14" cy="-26" r="16" fill="#3d7050"/>'
                            f'<circle cx="-8" cy="-40" r="4" fill="{APPLE}"/><circle cx="10" cy="-30" r="4" fill="{APPLE}"/><circle cx="4" cy="-46" r="3.5" fill="{APPLE}"/></g>')
    rows = ''.join(tree(x, 318, .9) for x in range(60, 1440, 96)) + ''.join(tree(x, 346, 1.1) for x in range(20, 1460, 120))
    return wrap(sun(1180, 110, 58) + peak(520, 250, 130, 400, FAR, .35) + peak(1100, 250, 110, 380, FAR, .3)
                + f'<path d="M0 262C300 236 600 268 900 246 1100 234 1300 258 1440 248V360H0Z" fill="#c7b58a"/>'
                + f'<path d="M0 290C260 276 520 300 780 286 1040 274 1240 296 1440 284V360H0Z" fill="{FIELD}"/>' + ground(322, "#6f8f5a") + rows)
def gorge():
    """The Columbia River gorge: basalt walls on both sides, the river running through, wind turbines on the rim."""
    turbine = lambda x, y: f'<g transform="translate({x} {y})" stroke="#f6f7f5" stroke-width="3" stroke-linecap="round"><path d="M0 0v-46"/><path d="M0-46l0-26M0-46l22 14M0-46l-22 14"/></g>'
    return wrap(sun(1160, 104, 56) + peak(720, 250, 130, 360, FAR, .3)
                + f'<path d="M0 200l140-40 120 30 100-50 90 60 40-20 40 40 60-30V360H0Z" fill="#6b5e52"/>'
                + f'<path d="M1440 190l-150-40-110 34-90-46-100 62-40-22-40 44-60-34V360h590z" fill="#6b5e52"/>'
                + f'<path d="M0 250l120-20 140 34 130-40 70 40 50-14V360H0Z" fill="#544a40"/><path d="M1440 240l-130-24-140 40-120-36-80 44-50-16V360h520z" fill="#544a40"/>'
                + turbine(200, 172) + turbine(260, 190) + turbine(1200, 168) + turbine(1260, 186)
                + f'<path d="M520 360C560 320 620 290 720 286 820 282 880 316 920 360z" fill="{WATER}"/>'
                + f'<path d="M560 360c40-30 90-52 160-54 70-2 130 22 170 54z" fill="{WATER_DEEP}" opacity=".5"/>'
                + fir(470, 358, 90, 26) + fir(980, 358, 84, 24) + fir(1020, 358, 60, 18, FIR_DARK))
def palouse():
    """The Palouse: rolling wheat hills in gold and green, a lone grain elevator, big sky."""
    elev = f'<g fill="#8a7a6a"><rect x="1080" y="230" width="46" height="80"/><path d="M1080 230h46l-23-24z"/><rect x="1130" y="256" width="60" height="54"/><rect x="1196" y="270" width="26" height="40"/></g>'
    return wrap(sun(260, 104, 60)
                + f'<path d="M0 240C200 200 400 250 600 214 800 178 1000 230 1200 204 1320 190 1400 210 1440 214V360H0Z" fill="{WHEAT}"/>'
                + f'<path d="M0 276C220 246 380 292 580 262 760 236 900 288 1100 262 1260 240 1380 270 1440 262V360H0Z" fill="{FIELD}"/>'
                + f'<path d="M0 310C240 282 420 322 640 300 860 278 1000 320 1200 302 1340 290 1400 306 1440 304V360H0Z" fill="#b39a48"/>'
                + elev + ground(336, "#6f8f5a") + fir(180, 336, 70, 20, FIR_DARK) + fir(206, 336, 54, 16, FIR_DARK)
                + ''.join(f'<path d="M{x} 358c2-14 6-24 10-30" stroke="{WHEAT}" stroke-width="2" fill="none"/>' for x in range(40, 1440, 34)))
def spokanefalls():
    """Spokane: the falls in Riverfront Park, the Clock Tower, basalt rocks, pines."""
    rocks = f'<g fill="#5a5048"><path d="M0 250h420l40 40v70H0z"/><path d="M1440 244H1000l-40 40v76h480z"/><path d="M460 300h520v60H460z"/></g>'
    fall = (f'<g fill="#eaf1f5"><rect x="600" y="240" width="240" height="70" rx="6" opacity=".95"/>' + ''.join(f'<rect x="{x}" y="244" width="8" height="70" opacity=".6" fill="{WATER}"/>' for x in range(612, 830, 28)) + '</g>'
            f'<rect x="560" y="310" width="320" height="50" fill="{WATER}"/><path d="M560 318c40-8 80 8 120 0s80-8 120 0 60 8 80 0" stroke="#eaf1f5" stroke-width="3" fill="none" opacity=".7"/>')
    river = f'<path d="M600 240H840V200H600z" fill="{WATER}"/><path d="M0 240h600v-14H0z" fill="{WATER}" opacity=".0"/>'
    tower = f'<g fill="#8a6a48"><rect x="1120" y="130" width="46" height="120"/><path d="M1114 130h58l-29-30z"/><circle cx="1143" cy="170" r="14" fill="{FOG}"/><path d="M1143 170v-9M1143 170h6" stroke="#8a6a48" stroke-width="2"/></g>'
    return wrap(sun(220, 110, 52) + f'<path d="M0 230C300 210 600 236 1440 214V360H0Z" fill="{FAR}" opacity=".6"/>'
                + treeline(250, FIR_DARK, -10, 440, 22) + treeline(244, FIR_DARK, 1000, 1450, 22) + river + rocks + fall + tower
                + fir(120, 250, 90, 26) + fir(300, 250, 110, 30) + fir(1300, 244, 96, 28) + fir(1380, 244, 70, 22))

SCENES = {"rainier": rainier(), "skyline": skyline(), "ferry": ferryscene(), "sanjuans": sanjuans(), "rainforest": rainforest(),
          "cascades": cascades(), "orchards": orchards(), "gorge": gorge(), "palouse": palouse(), "spokanefalls": spokanefalls()}
