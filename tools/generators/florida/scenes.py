"""Hero scenes for the Florida site — layered-silhouette SVG, brand palette."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6f2e8"/><stop offset="1" stop-color="#d9e9ee"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=62, c="#e7c486"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".65"/>'
def water(y, fill="#0f5c6e", op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def sand(y=330):
    return f'<path d="M0 {y}C300 {y-8} 600 {y+10} 900 {y} 1200 {y-8} 1350 {y+6} 1440 {y}V360H0Z" fill="#e8dcc0"/>'
def palm(x, y, h=110, lean=8, fill="#3a7a5a"):
    fr = "".join(f'<path d="M{x+lean} {y-h}q{dx} {dy} {dx*2} {dy+22}q{-dx*0.9} {-dy*0.6} {-dx*2} {-dy-20}z" fill="{fill}"/>' for dx, dy in [(-46,-10),(-34,-30),(34,-30),(46,-10),(-18,-38),(18,-38),(8,-2),(-8,-2)])
    return f'<path d="M{x} {y}q{lean} {-h/2} {lean} {-h}" stroke="#7a5a3c" stroke-width="7" fill="none" stroke-linecap="round"/>' + fr
def pelican(x, y):
    return f'<g fill="#1c2630" transform="translate({x} {y})"><path d="M0 0c20-14 60-14 80 0-10 6-70 6-80 0z"/><path d="M60-4c4-14 20-20 36-12l-10 6 4 8z"/></g>'
def ripples(y):
    return f'<path d="M300 {y}c120-6 240 4 360-2 120-6 240 6 360 0" stroke="#e9f1f5" stroke-width="2" fill="none" opacity=".5"/>'

def beach():
    return wrap(sun(1170, 110, 66) + water(292) + water(306, "#2b8aa0", ".8") + ripples(318) + sand(330) + pelican(600, 150) + palm(140, 336, 120, 10) + palm(210, 340, 90, -6) + palm(1260, 336, 116, -10) + palm(1330, 340, 84, 6))
def miami():
    b = '<g fill="#2b4b62">' + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in
        [(420,170,40),(470,130,34),(514,90,50),(574,150,34),(616,110,44),(670,160,36),(716,100,58),(784,176,30),(824,128,40),(874,150,52),(936,190,36),(982,164,30)]) + '</g>'
    w = '<g fill="#e7c486" opacity=".7">' + "".join(f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in [(526,110),(538,130),(628,130),(640,160),(728,130),(750,150),(836,150),(890,170),(552,170)]) + '</g>'
    return wrap(sun(1200, 100, 54) + b + w + water(304) + ripples(318) + palm(120, 336, 100, 8) + palm(1300, 336, 104, -8) + sand(334))
def lighthouse():
    stripes = "".join(f'<path d="M{262+i*6} {236-i*18}h34l-4-18h-26z" fill="{"#1c2630" if i%2 else "#e9e2d4"}"/>' for i in range(0)) 
    tower = ('<g><path d="M262 236h34l-4-110h-26z" fill="#e9e2d4"/>' + "".join(f'<path d="M{264+i*0.6} {230-i*14}l{26-i*0.6*2} 0 -1 -8 -24 0z" fill="#1c2630"/>' for i in range(0, 8, 2)) +
             '<rect x="254" y="124" width="50" height="10" fill="#d0603c"/><rect x="266" y="100" width="26" height="24" fill="#2b4b62"/><rect x="270" y="104" width="18" height="16" fill="#e7c486"/><path d="M258 100h42l-21-14z" fill="#d0603c"/></g>')
    return wrap(sun(1180, 116, 58) + '<path d="M290 112L700 60V160z" fill="#e7c486" opacity=".18"/>' + water(300) + ripples(316) + sand(330) + '<path d="M0 340h420V236h-160z" fill="#e8dcc0"/>' + tower + palm(120, 340, 96, 8) + palm(1280, 336, 108, -8))
def everglades():
    grass = "".join(f'<path d="M{x} 330q4-40 8-60q2 34 6 60z" fill="#7a9a4a"/>' for x in range(20, 1440, 26))
    cypress = lambda x: f'<rect x="{x-4}" y="200" width="8" height="130" fill="#5a4a3c"/><ellipse cx="{x}" cy="190" rx="34" ry="44" fill="#3a7a5a"/><path d="M{x-40} 210q40-30 80 0" stroke="#9aa88a" stroke-width="4" fill="none"/>'
    egret = '<g fill="#f4f6f8" transform="translate(720 262)"><ellipse cx="0" cy="0" rx="18" ry="9"/><path d="M14-4q10-24 2-40" stroke="#f4f6f8" stroke-width="4" fill="none"/><circle cx="16" cy="-44" r="5"/><path d="M20-44l16 2-16 2z" fill="#e7c486"/><path d="M-4 8v40M4 8v40" stroke="#1c2630" stroke-width="2"/></g>'
    return wrap(sun(1160, 112, 60) + water(300, "#3f8fa8") + grass + cypress(180) + cypress(1240) + egret + water(340, "#2b6e80"))
def liveoaks():
    def oak(x, y, s):
        return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-8" y="-40" width="16" height="44" fill="#4a3728"/>'
                '<path d="M-90-40c-30-40 10-90 60-80 20-40 90-30 100 10 40 0 60 50 20 60-10 30-60 30-90 12-30 20-80 14-90-2z" fill="#3a7a5a"/>'
                + "".join(f'<path d="M{dx} {dy}q6 26 -2 50" stroke="#9aa88a" stroke-width="3" fill="none"/>' for dx, dy in [(-60,-30),(-20,-20),(30,-24),(70,-30)]) + '</g>')
    return wrap(sun(1180, 110, 56) + '<path d="M0 290C300 276 700 300 1440 280V360H0Z" fill="#9db08a"/>' + oak(300, 320, 1.1) + oak(1120, 318, .9) + water(336, "#3f8fa8", ".9"))
def citrus():
    tree = lambda x, y: (f'<rect x="{x-5}" y="{y-40}" width="10" height="42" fill="#5a4a3c"/><circle cx="{x}" cy="{y-70}" r="44" fill="#3a7a5a"/>'
                         + "".join(f'<circle cx="{x+dx}" cy="{y-70+dy}" r="6" fill="#e7943c"/>' for dx, dy in [(-20,-10),(10,-24),(24,6),(-8,18),(-28,14),(14,20)]))
    return wrap(sun(1180, 110, 62) + '<path d="M0 296C300 288 700 304 1440 290V360H0Z" fill="#7a9a4a"/>' + "".join(tree(x, 320) for x in range(120, 1440, 170)) + '<path d="M0 340h1440v20H0z" fill="#c9a97a"/>')
def spacecoast():
    rocket = ('<g transform="translate(1080 120)"><rect x="-14" y="0" width="28" height="120" rx="6" fill="#e9e2d4"/><path d="M-14 0q14-40 28 0z" fill="#d0603c"/>'
              '<path d="M-14 100l-20 30h20zM14 100l20 30h-20z" fill="#2b4b62"/><path d="M-8 120q8 60 16 0z" fill="#e7c486"/><path d="M-6 130q6 90 12 0" fill="#f4f6f8" opacity=".7"/></g>')
    return wrap(sun(220, 110, 54) + rocket + water(300) + ripples(316) + sand(330) + palm(140, 336, 110, 8) + palm(1330, 340, 90, -6) + pelican(500, 160))
def keys():
    bridge = '<rect x="0" y="262" width="1440" height="12" fill="#b9a688"/>' + "".join(f'<rect x="{x}" y="274" width="10" height="40" fill="#8a7a6a"/>' for x in range(30, 1440, 90)) + "".join(f'<path d="M{x} 274a45 40 0 0 1 90 0" fill="#3f8fa8"/>' for x in range(40, 1440, 90))
    return wrap(sun(1170, 106, 60) + water(280, "#3f8fa8") + water(300, "#0f5c6e", ".9") + bridge + ripples(330) + pelican(400, 170) + pelican(760, 140))
def macdill():
    jet = '<g fill="#2b4b62" transform="translate(880 120)"><path d="M0 0l70 12-36 6zM-46 4h80l-8 10h-64zM-24 4l-16-18h12l18 18zM-24 14l-16 18h12l18-18z"/></g>'
    return wrap(sun(220, 110, 54) + jet + water(300) + ripples(316) + sand(332) + palm(130, 338, 104, 8) + palm(1310, 338, 96, -8) + '<rect x="0" y="340" width="1440" height="8" fill="#6f6f6f"/>')

SCENES = {"beach": beach(), "miami": miami(), "lighthouse": lighthouse(), "everglades": everglades(), "liveoaks": liveoaks(),
          "citrus": citrus(), "spacecoast": spacecoast(), "keys": keys(), "macdill": macdill()}
