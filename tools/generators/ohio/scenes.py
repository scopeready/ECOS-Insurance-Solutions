"""Hero scenes for the Ohio site — layered-silhouette SVG, brand palette (Lake Erie blue, buckeye brown, cornfield gold, scarlet)."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f2ec"/><stop offset="1" stop-color="#dbe7f1"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
FAR, MID, NEAR, DEEP = "#cdd6d2", "#8fa583", "#5f7d4a", "#3f5a36"
WATER, WATER2, SAND = "#2f6a99", "#4a84ad", "#e6dcc3"
BROWN, GOLD, SCARLET, INK = "#6b4a2b", "#d9b25f", "#a6131f", "#1f2428"

def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=60, c=GOLD):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".6"/>'
def ground(y, fill, op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def hills(y, amp, fill):
    return f'<path d="M0 {y}C180 {y-amp} 360 {y+amp} 540 {y} 720 {y-amp} 900 {y+amp} 1080 {y} 1260 {y-amp} 1440 {y}V360H0Z" fill="{fill}"/>'
def buckeye(x, y, s=1.0, leaf=NEAR):
    """A round-crowned buckeye tree: broad crown, short trunk, a few pale seed-cases."""
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-7" y="-34" width="14" height="38" fill="{BROWN}"/>'
            f'<path d="M-70-34c-16-36 14-78 52-72 18-28 70-22 74 8 32 2 40 44 6 54-8 22-48 26-70 10-24 14-62 8-62 0z" fill="{leaf}"/>'
            f'<circle cx="-24" cy="-64" r="4" fill="{GOLD}" opacity=".8"/><circle cx="26" cy="-52" r="4" fill="{GOLD}" opacity=".8"/></g>')
def skyline(blocks, fill="#2f4a63", windows=(), wfill=GOLD):
    b = f'<g fill="{fill}">' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in blocks) + '</g>'
    w = f'<g fill="{wfill}" opacity=".7">' + ''.join(f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in windows) + '</g>'
    return b + w
def water(y, fill=WATER, op="1"):
    return f'<rect x="0" y="{y}" width="1440" height="{360-y}" fill="{fill}" opacity="{op}"/>'
def ripples(y, c="#e9f1f5"):
    return f'<path d="M120 {y}c120-6 240 4 360-2 120-6 240 6 360 0 120-6 200 4 300 0" stroke="{c}" stroke-width="2" fill="none" opacity=".5"/>'
def corn(xs, y, h=40):
    return '<g>' + ''.join(f'<path d="M{x} {y}v-{h}M{x} {y-h*0.55}l-9-10M{x} {y-h*0.55}l9-10M{x} {y-h*0.8}l-8-9M{x} {y-h*0.8}l8-9" stroke="{GOLD}" stroke-width="2.4" fill="none"/>' for x in xs) + '</g>'
def barn(x, y, s=1.0, fill=SCARLET):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-46 0v-44l46-30 46 30V0z" fill="{fill}"/>'
            f'<path d="M-46-44l46-30 46 30" stroke="{INK}" stroke-width="3" fill="none" opacity=".35"/>'
            f'<rect x="-12" y="-28" width="24" height="28" fill="{INK}" opacity=".35"/><rect x="58" y="-70" width="22" height="70" fill="#b9b3a6"/><path d="M58-70a11 11 0 0 1 22 0z" fill="#b9b3a6"/></g>')
def roundbarn(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-40" y="-40" width="80" height="40" rx="4" fill="{BROWN}"/>'
            f'<path d="M-46-40q46-40 92 0z" fill="{SCARLET}"/><rect x="-6" y="-58" width="12" height="18" fill="{BROWN}"/><path d="M-6-58l6-8 6 8z" fill="{SCARLET}"/></g>')
def hemlock(x, y, h, w, f=DEEP):
    step = h / 4
    parts = ''.join(f"M{x} {y-h+i*step:.0f}l{w*(0.45+0.28*i):.0f} {step*1.35:.0f}h{-2*w*(0.45+0.28*i):.0f}z" for i in range(3))
    return f'<path d="{parts}" fill="{f}"/><rect x="{x-3}" y="{y-8}" width="6" height="12" fill="#3b2a1e"/>'

def erie():
    """Cleveland on Lake Erie: Key Tower, Terminal Tower, the Justice Center, a freighter, the water."""
    blocks = [(420,196,36),(464,150,30),(500,176,46),(552,96,34),(592,140,40),(640,120,26),(672,160,54),(734,132,30),(770,186,40),(816,170,48),(870,204,30)]
    b = skyline(blocks, windows=[(560,120),(572,150),(600,160),(646,140),(690,180),(742,150),(830,190),(506,190)])
    b += '<path d="M552 96l17-22 17 22z" fill="#2f4a63"/><rect x="646" y="100" width="14" height="20" fill="#2f4a63"/><path d="M646 100l7-14 7 14z" fill="#2f4a63"/>'
    ship = f'<g fill="{INK}" opacity=".8"><rect x="1040" y="286" width="220" height="14" rx="3"/><rect x="1058" y="270" width="36" height="16"/><rect x="1226" y="266" width="26" height="20"/><rect x="1236" y="256" width="6" height="10"/></g>'
    light = f'<g><rect x="200" y="240" width="18" height="60" fill="#e9e2d4"/><rect x="196" y="234" width="26" height="8" fill="{SCARLET}"/><rect x="203" y="222" width="12" height="12" fill="{GOLD}"/></g>'
    return wrap(sun(1200, 100, 54) + hills(262, 6, FAR) + b + water(300, WATER) + water(318, WATER2, ".7") + ripples(330) + ship + light)
def scioto():
    """Columbus on the Scioto: the LeVeque Tower spire, Rhodes Tower, the river and the Scioto Mile."""
    blocks = [(440,190,40),(490,150,44),(544,124,30),(584,176,36),(628,86,44),(680,150,30),(716,120,52),(776,170,34),(818,144,44),(870,182,52),(930,200,30)]
    b = skyline(blocks, fill="#33506b", windows=[(500,170),(556,150),(640,110),(652,140),(730,150),(752,170),(830,164),(886,200)])
    b += '<rect x="642" y="60" width="16" height="26" fill="#33506b"/><path d="M642 60l8-22 8 22z" fill="#33506b"/><rect x="726" y="100" width="6" height="20" fill="#33506b"/>'
    bridge = f'<g fill="{FAR}"><rect x="360" y="286" width="740" height="8"/><path d="M380 286q80-28 160 0M540 286q80-28 160 0M700 286q80-28 160 0M860 286q80-28 160 0" stroke="{FAR}" stroke-width="6" fill="none"/></g>'
    return wrap(sun(220, 104, 50) + hills(258, 8, FAR) + b + buckeye(1200, 300, .9) + water(300, WATER) + ripples(318) + bridge + ground(330, NEAR, ".9"))
def roebling():
    """Cincinnati: the Roebling Suspension Bridge towers and cables over the Ohio River, hills behind."""
    hillsb = f'<path d="M0 244C200 214 400 250 600 226 800 204 1000 240 1440 216V360H0Z" fill="{FAR}"/><path d="M0 280C260 252 520 286 780 264 1040 246 1240 282 1440 262V360H0Z" fill="{MID}"/>'
    tower = lambda x: (f'<g fill="{BROWN}"><rect x="{x}" y="150" width="22" height="160"/><rect x="{x+34}" y="150" width="22" height="160"/><rect x="{x}" y="138" width="56" height="14"/>'
                       f'<rect x="{x-4}" y="120" width="64" height="8"/><path d="M{x+6} 138v-10h10v10M{x+40} 138v-10h10v10" /></g>'
                       f'<rect x="{x+22}" y="196" width="12" height="60" fill="{SKY_HOLE}"/>')
    global SKY_HOLE
    SKY_HOLE = "#e6edf3"
    cables = (f'<path d="M180 296Q400 150 520 148M520 148Q740 280 960 148M960 148Q1080 150 1300 296" stroke="{INK}" stroke-width="3" fill="none" opacity=".7"/>'
              + ''.join(f'<line x1="{x}" y1="{y}" x2="{x}" y2="296" stroke="{INK}" stroke-width="1.5" opacity=".5"/>' for x, y in [(300,220),(360,190),(420,166),(460,154),(600,176),(660,214),(740,270),(820,214),(880,176),(1020,154),(1060,166),(1120,190),(1180,220)]))
    deck = f'<rect x="120" y="296" width="1200" height="8" fill="{INK}" opacity=".8"/>'
    return wrap(sun(1180, 110, 56) + hillsb + cables + tower(492) + tower(932) + deck + water(310, WATER) + water(326, WATER2, ".7") + ripples(336))
def hocking():
    """Hocking Hills: sandstone cliff, a recess cave, hemlocks, a thin waterfall."""
    cliff = (f'<path d="M0 200h520c40 0 60 30 60 60v100H0z" fill="#b39a7a"/><path d="M0 214h480c30 0 44 20 44 46v100H0z" fill="#9c8262"/>'
             f'<path d="M120 246c80-10 200-10 300 0v70H120z" fill="#6f5a42"/><rect x="392" y="214" width="6" height="110" fill="#dbe7f1" opacity=".85"/>')
    trees = ''.join(hemlock(x, 322, h, w) for x, h, w in [(700,120,32),(760,88,24),(900,130,34),(980,96,26),(1140,124,32),(1220,84,22),(1340,110,28)])
    return wrap(sun(1180, 100, 52) + hills(250, 10, FAR) + hills(280, 10, MID) + cliff + trees + ground(326, DEEP) + f'<path d="M0 340C300 332 600 348 900 338 1200 330 1350 344 1440 338V360H0Z" fill="{WATER}" opacity=".8"/>')
def amish():
    """Holmes County farmland: rolling fields, a round barn, a red barn and silo, a buggy on the road."""
    buggy = (f'<g transform="translate(1120 326)" fill="{INK}"><rect x="-26" y="-34" width="52" height="30" rx="4"/><circle cx="-16" cy="0" r="9" fill="none" stroke="{INK}" stroke-width="3"/>'
             f'<circle cx="16" cy="0" r="9" fill="none" stroke="{INK}" stroke-width="3"/><rect x="34" y="-28" width="34" height="18" rx="6"/><rect x="62" y="-40" width="8" height="16" rx="3"/><rect x="40" y="-10" width="4" height="12"/><rect x="58" y="-10" width="4" height="12"/></g>')
    fields = f'<path d="M0 270C300 250 600 274 900 256 1200 240 1350 262 1440 252V360H0Z" fill="{MID}"/>' + ''.join(f'<path d="M{x} 300q40-30 80 0" stroke="{GOLD}" stroke-width="2" fill="none" opacity=".5"/>' for x in range(0, 1440, 80))
    road = f'<path d="M0 336C300 328 700 344 1440 334V360H0Z" fill="#b9b3a6"/>'
    return wrap(sun(1180, 108, 58) + hills(240, 12, FAR) + fields + roundbarn(360, 300, 1.0) + barn(760, 306, .9) + ground(318, NEAR) + road + buggy + corn(range(40, 300, 22), 318, 34))
def buckeye_scene():
    """A buckeye lane: two big buckeye trees, a split-rail fence, cornfield gold on the horizon."""
    fence = ''.join(f'<rect x="{x}" y="296" width="6" height="40" fill="{BROWN}"/>' for x in range(40, 1440, 90)) + f'<rect x="0" y="306" width="1440" height="4" fill="{BROWN}"/><rect x="0" y="322" width="1440" height="4" fill="{BROWN}"/>'
    return wrap(sun(1170, 116, 60) + hills(252, 10, FAR) + f'<path d="M0 282C300 262 600 286 1440 262V360H0Z" fill="{GOLD}" opacity=".55"/>' + hills(292, 8, MID)
                + buckeye(300, 324, 1.2) + buckeye(1080, 322, 1.0) + ground(330, NEAR) + fence)
def maumee():
    """Toledo on the Maumee: grain elevators, the glass towers, a drawbridge, the river to the lake."""
    blocks = [(520,170,34),(562,140,46),(616,186,26),(650,150,40),(700,172,48),(756,196,30)]
    b = skyline(blocks, fill="#3a5670", windows=[(576,160),(588,190),(662,170),(716,190)])
    elev = f'<g fill="#8a8578"><rect x="240" y="200" width="30" height="120"/><rect x="274" y="200" width="30" height="120"/><rect x="308" y="200" width="30" height="120"/><rect x="230" y="186" width="118" height="16"/><rect x="270" y="150" width="40" height="40"/></g>'
    bridge = f'<g fill="{INK}" opacity=".75"><rect x="880" y="286" width="380" height="8"/><path d="M960 286v-70h12v70M1180 286v-70h12v70M972 224l208-6" stroke="{INK}" stroke-width="4" fill="none"/></g>'
    return wrap(sun(1200, 104, 52) + hills(262, 6, FAR) + elev + b + water(302, WATER) + water(320, WATER2, ".7") + ripples(332) + bridge)
def millvalley():
    """The Mahoning Valley / Akron: mill stacks, a blast-furnace silhouette, a river, factory roofs."""
    mill = (f'<g fill="#4e5a63"><rect x="300" y="210" width="120" height="110"/><path d="M300 210l30-24 30 24 30-24 30 24z"/><rect x="440" y="150" width="20" height="170"/><rect x="480" y="120" width="26" height="200"/>'
            f'<rect x="530" y="180" width="70" height="140"/><path d="M540 180l-10-50h60l-10 50z"/><rect x="640" y="232" width="200" height="88"/><path d="M640 232l25-20 25 20 25-20 25 20 25-20 25 20 25-20 25 20z"/></g>'
            f'<g fill="#c9c5bb" opacity=".6"><ellipse cx="450" cy="138" rx="22" ry="12"/><ellipse cx="493" cy="104" rx="26" ry="14"/><ellipse cx="470" cy="118" rx="16" ry="9"/></g>')
    return wrap(sun(1180, 112, 56) + hills(250, 10, FAR) + hills(282, 8, MID) + mill + buckeye(1160, 318, .9) + ground(320, NEAR) + f'<path d="M0 338C300 330 600 346 900 336 1200 328 1350 342 1440 336V360H0Z" fill="{WATER}" opacity=".8"/>')
def flightline():
    """Wright-Patterson: hangars, the control tower, an aircraft on the ramp, a big Ohio sky."""
    hangar = lambda x, w: f'<path d="M{x} 320v-70q{w/2}-50 {w} 0v70z" fill="#5c6670"/><rect x="{x+w*0.35}" y="280" width="{w*0.3}" height="40" fill="{INK}" opacity=".35"/>'
    tower = f'<g fill="#5c6670"><rect x="1010" y="220" width="16" height="100"/><rect x="990" y="196" width="56" height="30" rx="4"/><rect x="994" y="200" width="48" height="12" fill="{GOLD}" opacity=".6"/></g>'
    plane = (f'<g transform="translate(560 300)" fill="{INK}" opacity=".85"><path d="M-90 0h180l-14-10H-76z"/><path d="M-20-8l24-46h10l-4 46z"/><path d="M-70-8l-40-22h12l44 22zM20-8l70-22h12l-70 22z"/>'
             f'<path d="M84-6l16-22h6l-6 22z"/><circle cx="-40" cy="4" r="4"/><circle cx="40" cy="4" r="4"/></g>')
    return wrap(sun(1200, 96, 50) + hills(262, 6, FAR) + hangar(120, 220) + hangar(360, 160) + hangar(1140, 200) + tower + ground(320, MID) + plane + f'<rect x="0" y="330" width="1440" height="30" fill="#8a8578"/><path d="M0 344h1440" stroke="{GOLD}" stroke-width="3" stroke-dasharray="40 30"/>')
def ohioriver():
    """The Ohio River valley: wooded hills, a towboat with barges, the river bending under a wide sky."""
    barge = (f'<g fill="{INK}" opacity=".8"><rect x="760" y="296" width="120" height="12" rx="2"/><rect x="884" y="296" width="120" height="12" rx="2"/><rect x="1008" y="284" width="54" height="24" rx="3"/>'
             f'<rect x="1020" y="270" width="26" height="14"/><rect x="1030" y="262" width="6" height="8"/></g>')
    trees = ''.join(hemlock(x, 300, h, w, MID) for x, h, w in [(80,60,18),(130,44,14),(1240,56,16),(1300,40,12),(1380,60,18)])
    return wrap(sun(1170, 106, 56) + f'<path d="M0 226C200 200 380 236 560 212 760 190 940 230 1440 204V360H0Z" fill="{FAR}"/>'
                + f'<path d="M0 270C260 244 520 280 780 256 1040 236 1240 274 1440 250V360H0Z" fill="{MID}"/>' + trees + ground(300, NEAR)
                + f'<path d="M0 316C300 306 600 326 900 314 1200 304 1350 320 1440 314V360H0Z" fill="{WATER}"/>' + ripples(338) + barge)

SCENES = {"erie": erie(), "scioto": scioto(), "roebling": roebling(), "hocking": hocking(), "amish": amish(), "buckeye": buckeye_scene(),
          "maumee": maumee(), "millvalley": millvalley(), "flightline": flightline(), "ohioriver": ohioriver()}
