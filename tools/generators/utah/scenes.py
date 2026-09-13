"""Hero scenes for the Utah site — layered-silhouette SVG, brand palette."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f5f1ea"/><stop offset="1" stop-color="#dde6ee"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=60, c="#e7c486"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".6"/>'
def ground(y, fill, op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def peaks(pts, fill, snow=None):
    d = "M0 360L" + " ".join(f"{x} {y}" for x, y in pts) + " L1440 360Z"
    out = f'<path d="{d}" fill="{fill}"/>'
    if snow:
        for x, y in pts:
            if y < snow:
                out += f'<path d="M{x-28} {y+34}L{x} {y}L{x+28} {y+34}L{x+14} {y+28}L{x+4} {y+38}L{x-8} {y+26}L{x-18} {y+36}Z" fill="#f4f6f8"/>'
    return out
def conifers(spec, fill="#4a6b52"):
    out = []
    for x, y, h, w in spec:
        step = h / 4
        parts = "".join(f"M{x} {y-h+i*step:.0f}l{w*(0.45+0.28*i):.0f} {step*1.35:.0f}h{-2*w*(0.45+0.28*i):.0f}z" for i in range(3))
        out.append(f'<path d="{parts}" fill="{fill}"/><rect x="{x-2}" y="{y-8}" width="4" height="10" fill="#3b2a1e"/>')
    return "".join(out)

def wasatch():
    return wrap(sun(1180, 110, 56) + peaks([(0,250),(160,150),(300,210),(420,120),(560,200),(700,130),(860,190),(1000,110),(1140,180),(1300,140),(1440,200)], "#8fa3b8", snow=175)
                + peaks([(0,300),(200,250),(400,280),(640,240),(880,270),(1120,236),(1440,262)], "#5f7d92")
                + ground(316, "#7f9a70") + conifers([(120,318,70,20),(170,320,50,15),(1240,316,76,22),(1300,320,54,16)]))
def saltlake():
    b = '<g fill="#2b4b62">' + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in
        [(480,200,40),(530,160,44),(584,180,34),(628,120,50),(690,190,36),(736,150,58),(804,200,30),(844,170,40)]) + '</g>'
    cap = '<g fill="#cfc6b4"><rect x="900" y="230" width="180" height="130"/><rect x="955" y="196" width="70" height="40"/><path d="M955 200a35 35 0 0 1 70 0z"/><rect x="986" y="176" width="8" height="24"/></g>'
    w = '<g fill="#e7c486" opacity=".7">' + "".join(f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in [(540,180),(552,200),(640,140),(652,170),(748,170),(770,190),(856,190)]) + '</g>'
    return wrap(sun(200, 106, 50) + peaks([(0,220),(180,130),(360,200),(520,110),(700,190),(880,120),(1060,200),(1240,130),(1440,210)], "#8fa3b8", snow=160) + b + cap + w + ground(330, "#7f9a70"))
def arch():
    a = ('<g fill="#b8522e"><path d="M420 360V240c0-90 60-150 150-150s150 60 150 150v120h-70V250c0-50-30-80-80-80s-80 30-80 80v110z"/>'
         '<path d="M880 360V300l60-40 40 40v60z"/><path d="M1000 360V280l50-30 60 30v80z"/></g>'
         '<path d="M0 320l180-60 160 40 120-30 100 20V360H0z" fill="#a34a2a"/>')
    return wrap(sun(1170, 110, 62) + peaks([(0,260),(300,220),(600,250),(900,200),(1200,240),(1440,210)], "#c9b8a8", snow=None) + a + ground(340, "#c9a97a"))
def redcliffs():
    return wrap(sun(1180, 112, 60) + peaks([(0,230),(200,180),(380,220),(560,160),(760,210),(960,150),(1160,200),(1440,170)], "#c76a4a")
                + '<path d="M0 290l160-40 140 20 200-50 220 40 200-30 260 30 260-20V360H0z" fill="#b8522e"/>' + ground(330, "#d8bb8a") + conifers([(200,332,50,16),(900,330,44,14),(1320,332,58,18)], "#6b7a4a"))
def bearlake():
    boat = '<g transform="translate(700 300)"><path d="M-40 0h80l-10 14h-60z" fill="#5a4a3c"/><path d="M0-4V-70L34-8z" fill="#f4f6f8"/><path d="M0-4V-60L-26-8z" fill="#e9e2d4"/></g>'
    return wrap(sun(260, 110, 56) + peaks([(0,240),(220,170),(440,230),(680,160),(900,220),(1140,150),(1440,220)], "#8fa3b8", snow=190) + ground(300, "#3f8fa8") + ground(314, "#2b7a9a", ".8") + boat
                + '<path d="M0 334C300 326 600 342 900 334 1200 326 1350 340 1440 334V360H0Z" fill="#e8dcc0"/>')
def hoodoos():
    h = "".join(f'<g fill="{c}"><path d="M{x} 360V{y}q10-20 20-10v-20q6-14 14 0v18q10-12 20 6V360z"/></g>' for x, y, c in
                [(120,230,"#d07a4e"),(200,250,"#c76a4a"),(300,210,"#d07a4e"),(390,260,"#b8522e"),(520,220,"#d07a4e"),(640,240,"#c76a4a"),(760,200,"#d07a4e"),(880,250,"#b8522e"),(1000,215,"#d07a4e"),(1120,245,"#c76a4a"),(1240,205,"#d07a4e"),(1340,255,"#b8522e")])
    return wrap(sun(1180, 106, 58) + peaks([(0,260),(300,230),(600,250),(900,220),(1200,246),(1440,226)], "#e0c8b0") + h + ground(340, "#c9a97a") + conifers([(60,340,60,18),(1400,340,56,16)], "#4a6b52"))
def utahvalley():
    return wrap(sun(220, 110, 54) + peaks([(0,240),(200,160),(400,220),(600,110),(760,200),(940,150),(1120,210),(1300,160),(1440,220)], "#8fa3b8", snow=170)
                + ground(300, "#3f8fa8", ".9") + ground(320, "#7f9a70") + conifers([(140,322,60,18),(1260,320,66,20),(1320,324,48,14)]))
def aspens():
    tree = lambda x, y, h: f'<rect x="{x-3}" y="{y-h}" width="6" height="{h}" fill="#e9e2d4"/><ellipse cx="{x}" cy="{y-h}" rx="22" ry="34" fill="#d9a441"/>'
    lift = '<path d="M0 200L1440 90" stroke="#5a4a3c" stroke-width="3"/>' + "".join(f'<rect x="{x-8}" y="{200-int(110*x/1440)}" width="16" height="22" rx="3" fill="#2b4b62"/>' for x in range(200, 1440, 260))
    return wrap(sun(1170, 110, 54) + peaks([(0,230),(240,140),(480,210),(720,120),(960,200),(1200,130),(1440,210)], "#8fa3b8", snow=160) + lift + ground(320, "#4a6b52")
                + "".join(tree(x, 322, h) for x, h in [(100,80),(150,60),(240,90),(620,70),(680,96),(1080,84),(1130,64),(1360,90)]))
def hillafb():
    jet = '<g fill="#2b4b62" transform="translate(900 120)"><path d="M0 0l60 10-30 6zM-40 4h70l-6 8h-58zM-20 4l-14-16h10l16 16zM-20 12l-14 16h10l16-16z"/></g>'
    runway = '<rect x="0" y="330" width="1440" height="14" fill="#6f6f6f"/>' + "".join(f'<rect x="{x}" y="336" width="40" height="3" fill="#f4f6f8"/>' for x in range(20, 1440, 100))
    return wrap(sun(200, 110, 52) + peaks([(0,240),(200,150),(420,220),(640,120),(860,200),(1080,140),(1300,210),(1440,180)], "#8fa3b8", snow=170) + jet + ground(322, "#7f9a70") + runway)

SCENES = {"wasatch": wasatch(), "saltlake": saltlake(), "arch": arch(), "redcliffs": redcliffs(), "bearlake": bearlake(),
          "hoodoos": hoodoos(), "utahvalley": utahvalley(), "aspens": aspens(), "hillafb": hillafb()}
