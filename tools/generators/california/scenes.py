"""Hero scenes for the California site — layered-silhouette SVG, brand palette."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f7f4ec"/><stop offset="1" stop-color="#dbe7f0"/></linearGradient>'
       '<linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3e3c4"/><stop offset="1" stop-color="#e9b98a"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
DUSK = SKY.replace('fill="url(#sky)"', 'fill="url(#dusk)"')
def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=62, c="#e9c46a"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".7"/>'
def water(y, fill="#1b4e73", op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def hills(pts, fill, op="1"):
    return f'<path d="M0 360L0 {pts[0]}' + "".join(f"Q{x} {y} {x2} {y2}" for x, y, x2, y2 in pts[1]) + 'L1440 360Z" fill="{fill}" opacity="{op}"/>'.replace("{fill}", fill).replace("{op}", op)
def ridge(y0, seq, fill, op="1"):
    d = f"M0 360L0 {y0}"
    x = 0
    for dx, y in seq:
        d += f"Q{x+dx/2} {y-30} {x+dx} {y}"; x += dx
    return f'<path d="{d}L1440 360Z" fill="{fill}" opacity="{op}"/>'
def fog(y, op=".55"):
    return f'<path d="M0 {y}C200 {y-14} 400 {y+16} 720 {y} 1040 {y-16} 1240 {y+14} 1440 {y}V{y+60}H0Z" fill="#fffefb" opacity="{op}"/>'
def tree(x, y, h=90, w=26, fill="#2f4a33"):
    return f'<path d="M{x} {y}l{-w/2} 0 {w/2} {-h} {w/2} {h}z" fill="{fill}"/><rect x="{x-3}" y="{y}" width="6" height="14" fill="#5a4030"/>'
def palm(x, y, h=110, lean=8, fill="#4a6b3f"):
    fr = "".join(f'<path d="M{x+lean} {y-h}q{dx} {dy} {dx*2} {dy+22}q{-dx*0.9} {-dy*0.6} {-dx*2} {-dy-20}z" fill="{fill}"/>' for dx, dy in [(-46,-10),(-34,-30),(34,-30),(46,-10),(-18,-38),(18,-38)])
    return f'<path d="M{x} {y}q{lean} {-h/2} {lean} {-h}" stroke="#6b4a32" stroke-width="7" fill="none" stroke-linecap="round"/>' + fr
def poppies(y, n=14, x0=80, dx=48):
    return '<g>' + "".join(f'<circle cx="{x0+i*dx}" cy="{y-(i%3)*6}" r="6" fill="#d97a2b"/><rect x="{x0+i*dx-1}" y="{y-(i%3)*6}" width="2" height="16" fill="#4a6b3f"/>' for i in range(n)) + '</g>'
def gull(x, y):
    return f'<path d="M{x} {y}q12-10 24 0q12-10 24 0" stroke="#1c2630" stroke-width="2.5" fill="none" stroke-linecap="round"/>'

def goldengate():
    tower = lambda x: f'<rect x="{x-9}" y="120" width="18" height="240" fill="#c0503a"/><rect x="{x-16}" y="150" width="32" height="8" fill="#c0503a"/><rect x="{x-16}" y="200" width="32" height="8" fill="#c0503a"/>'
    cable = '<path d="M180 320Q470 120 760 320" stroke="#c0503a" stroke-width="5" fill="none"/><path d="M760 320Q1050 120 1340 320" stroke="#c0503a" stroke-width="5" fill="none"/>'
    deck = '<rect x="120" y="300" width="1320" height="10" fill="#a8412d"/>' + "".join(f'<rect x="{x}" y="{200+abs(760-x)//6}" width="2" height="{100-abs(760-x)//6}" fill="#c0503a" opacity=".7"/>' for x in range(200, 1340, 40))
    return wrap(fog(180, ".5") + ridge(260, [(300, 240), (400, 250), (740, 262)], "#7a93a8", ".6") + water(316) + water(330, "#2c6e96", ".8") + deck + cable + tower(470) + tower(1050) + gull(300, 120) + gull(1200, 90) + fog(300, ".35"))
def redwoods():
    trunks = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}" fill="#3d2a1e"/><path d="M{x+w/2} {y-40}l{-w*1.6} 60h{w*3.2}z" fill="#2f4a33" opacity=".9"/>' for x, y, w in [(90,60,26),(260,20,34),(430,80,22),(620,0,40),(820,50,28),(1010,10,36),(1180,70,24),(1350,30,30)])
    return wrap(fog(200, ".5") + ridge(250, [(500, 230), (500, 250), (440, 240)], "#4a6b3f", ".7") + trunks + '<rect x="0" y="330" width="1440" height="30" fill="#2f4a33"/>' + fog(310, ".45"))
def coast():
    return wrap(sun(1200, 100, 60) + water(280) + water(296, "#2c6e96", ".8") + gull(360, 90) + gull(420, 110) + ridge(200, [(200, 170), (140, 190), (120, 230), (200, 300)], "#8a7660") + ridge(240, [(160, 210), (160, 250), (120, 300), (200, 330)], "#6b5a48") + '<path d="M0 330C200 322 400 338 660 332 900 326 1200 340 1440 332V360H0Z" fill="#e8dcc0"/>' + '<path d="M300 322c120-6 240 4 360-2 120-6 240 6 360 0" stroke="#fffefb" stroke-width="2" fill="none" opacity=".6"/>')
def vineyards():
    rows = "".join(f'<path d="M0 {y}Q720 {y-14-i*2} 1440 {y}" stroke="#4a6b3f" stroke-width="{8+i}" fill="none" opacity=".85"/>' for i, y in enumerate(range(262, 360, 16)))
    return wrap(sun(1120, 118, 58) + ridge(190, [(360, 160), (360, 200), (360, 170), (360, 210)], "#b7c2a3", ".7") + ridge(230, [(480, 200), (480, 236), (480, 210)], "#8aa373", ".85") + rows + tree(200, 250, 70, 40, "#3d5a3a") + tree(1240, 246, 78, 44, "#3d5a3a") + '<rect x="600" y="222" width="90" height="34" fill="#c0503a"/><path d="M590 224l55-28 55 28z" fill="#8a3a2a"/>')
def desert():
    mills = "".join(f'<rect x="{x-2}" y="{y}" width="4" height="{300-y}" fill="#d9d4c7"/><g transform="translate({x} {y})"><path d="M0 0l-4-54 8 0z M0 0l50 22-4 7z M0 0l-50 22 4 7z" fill="#d9d4c7"/></g>' for x, y in [(160,170),(260,150),(360,180),(1120,160),(1230,140),(1330,175)])
    return wrap(sun(720, 96, 70, "#d97a2b") + ridge(200, [(360, 150), (300, 190), (400, 140), (380, 200)], "#b98a6a", ".85") + ridge(250, [(480, 220), (480, 260), (480, 226)], "#9a6a4a", ".9") + mills + '<rect x="0" y="300" width="1440" height="60" fill="#d8c3a0"/>' + palm(640, 300, 96, 6) + palm(720, 302, 110, -8) + palm(800, 300, 88, 4), DUSK)
def sierra():
    peaks = '<path d="M0 360L0 240 120 170 200 220 300 130 380 190 470 100 560 180 640 150 720 200 800 120 880 190 960 140 1040 210 1120 160 1200 220 1290 150 1370 200 1440 170V360Z" fill="#5f7385"/>' + '<path d="M470 100l-30 60 20-8 12 20 14-22 18 10z M800 120l-26 52 18-6 10 16 12-18 16 8z M1290 150l-22 44 14-4 10 14 10-16 14 6z" fill="#fffefb" opacity=".9"/>'
    return wrap(peaks + ridge(250, [(400, 230), (400, 262), (320, 236), (320, 270)], "#2f4a33", ".9") + water(300, "#1b4e73") + water(314, "#2c6e96", ".7") + tree(120, 300, 70, 26) + tree(180, 296, 84, 30) + tree(1300, 300, 76, 28))
def losangeles():
    b = '<g fill="#3a4c60">' + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in [(500,190,36),(544,150,30),(580,110,48),(636,170,28),(672,130,40),(720,90,56),(784,160,32),(824,120,44),(876,150,50),(936,180,30)]) + '</g>'
    return wrap(sun(1180, 110, 60) + ridge(200, [(360, 170), (300, 200), (400, 160), (380, 210)], "#8aa373", ".6") + ridge(240, [(480, 220), (480, 250), (480, 230)], "#6b8a5c", ".8") + b + '<rect x="0" y="310" width="1440" height="50" fill="#4a6b3f"/>' + palm(140, 312, 120, 10) + palm(230, 316, 96, -6) + palm(1200, 312, 118, -10) + palm(1300, 316, 92, 8) + palm(400, 314, 104, 4))
def valley():
    rows = "".join(f'<circle cx="{x}" cy="{y}" r="16" fill="#4a6b3f"/><rect x="{x-2}" y="{y+10}" width="4" height="20" fill="#5a4030"/>' for i, x in enumerate(range(60, 1440, 96)) for y in (276, 318) if (i + (y == 318)) % 2 == 0)
    return wrap(sun(1120, 120, 62) + ridge(220, [(480, 200), (480, 236), (480, 214)], "#b7c2a3", ".6") + '<rect x="0" y="250" width="1440" height="110" fill="#c9b989"/>' + rows + '<rect x="1040" y="222" width="70" height="30" fill="#c0503a"/><path d="M1032 224l43-24 43 24z" fill="#8a3a2a"/><rect x="1120" y="200" width="16" height="52" fill="#9aa4ad"/>')
def harbor():
    ship = lambda x, y, w: f'<path d="M{x} {y}h{w}l-14 26H{x+14}z" fill="#6b7b8a"/><rect x="{x+w*0.4}" y="{y-30}" width="{w*0.25}" height="30" fill="#6b7b8a"/><rect x="{x+w*0.55}" y="{y-46}" width="4" height="16" fill="#6b7b8a"/>'
    bridge = '<path d="M700 250Q980 150 1260 262" stroke="#4a5d70" stroke-width="10" fill="none"/>' + "".join(f'<rect x="{x}" y="{y}" width="8" height="{300-y}" fill="#4a5d70"/>' for x, y in [(780,232),(900,196),(1020,188),(1140,212)])
    return wrap(sun(220, 110, 56) + fog(200, ".3") + ridge(230, [(500, 210), (500, 236), (440, 220)], "#8aa373", ".6") + bridge + water(300) + water(314, "#2c6e96", ".8") + ship(160, 300, 200) + ship(500, 304, 150) + gull(600, 120) + palm(1320, 300, 100, -8))

SCENES = {"goldengate": goldengate(), "redwoods": redwoods(), "coast": coast(), "vineyards": vineyards(), "desert": desert(),
          "sierra": sierra(), "losangeles": losangeles(), "valley": valley(), "harbor": harbor()}
