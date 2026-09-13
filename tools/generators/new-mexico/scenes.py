"""Hero scenes for the New Mexico site — layered-silhouette SVG in the adobe / turquoise / chile / sage palette."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6efe4"/><stop offset="1" stop-color="#e8d9c6"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
SUNSET = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6efe4"/><stop offset=".55" stop-color="#efd3bd"/><stop offset="1" stop-color="#e2b6a3"/></linearGradient></defs>'
          '<rect width="1440" height="360" fill="url(#sky)"/>')
MORNING = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6efe4"/><stop offset="1" stop-color="#d6e6e6"/></linearGradient></defs>'
           '<rect width="1440" height="360" fill="url(#sky)"/>')
def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=60, c="#deaa6e"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".65"/>'
def ground(y, fill, op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def mesa(x, w, top, h, fill):
    """Flat-topped mesa with sloped talus sides."""
    return f'<path d="M{x} {top+h}l{w*0.18:.0f} {-h}h{w*0.64:.0f}l{w*0.18:.0f} {h}z" fill="{fill}"/>'
def juniper(x, y, s=1.0, f="#5f7350"):
    return f'<g transform="translate({x} {y}) scale({s})"><rect x="-3" y="-14" width="6" height="16" fill="#4a3a2c"/><path d="M-26-10c-8-22 10-44 26-40 16-4 34 18 26 40-8 12-44 12-52 0z" fill="{f}"/></g>'
def pinon(x, y, s=1.0, f="#4d6444"):
    return f'<g transform="translate({x} {y}) scale({s})"><rect x="-3" y="-12" width="6" height="14" fill="#4a3a2c"/><path d="M0-70c14 8 26 26 30 46 6 12-8 24-30 24s-36-12-30-24c4-20 16-38 30-46z" fill="{f}"/></g>'
def yucca(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-3" y="-60" width="6" height="60" fill="#6b7d5a"/>'
            '<path d="M0-28l-30-36M0-28l30-36M0-28l-40-14M0-28l40-14M0-28l-14-44M0-28l14-44" stroke="#6b7d5a" stroke-width="3"/><ellipse cx="0" cy="-78" rx="6" ry="14" fill="#f3ede2"/></g>')
def cottonwood(x, y, s=1.0, f="#d4a13f"):
    return f'<g transform="translate({x} {y}) scale({s})"><rect x="-6" y="-34" width="12" height="38" fill="#5a4636"/><path d="M-62-30c-16-34 14-72 48-64 22-32 78-18 74 14 30 4 34 46 2 52-12 20-52 22-72 6-20 14-56 10-52-8z" fill="{f}"/></g>'
def adobe(x, y, w, h, f="#c68a5c", vigas=True, door=None):
    g = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{f}"/>'
    if vigas:
        g += ''.join(f'<circle cx="{vx}" cy="{y+12}" r="4" fill="#7a5238"/>' for vx in range(x + 14, x + w - 8, 22))
    if door:
        g += f'<rect x="{door}" y="{y+h-46}" width="26" height="46" rx="3" fill="#2f8a8a"/>'
    return g
def ristra(x, y, n=7):
    pods = ''.join(f'<ellipse cx="{x + (i % 2) * 6 - 3}" cy="{y + i * 9}" rx="4.5" ry="7" fill="#a6321e"/>' for i in range(n))
    return f'<rect x="{x-1}" y="{y-14}" width="2" height="16" fill="#6b5a40"/>' + pods
def balloon(x, y, s=1.0, c1="#2f8a8a", c2="#a6321e"):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0-90c-34 0-52 28-52 56 0 26 22 44 40 62l12 20 12-20c18-18 40-36 40-62 0-28-18-56-52-56z" fill="{c1}"/>'
            f'<path d="M-18-84c-14 12-20 34-14 62 6 18 20 34 32 54-2-30-12-58-6-86 2-14 6-24-12-30z" fill="{c2}" opacity=".85"/>'
            '<rect x="-7" y="52" width="14" height="10" fill="#6b4a32"/><path d="M-10 48l-4 6M10 48l4 6" stroke="#6b4a32" stroke-width="1.5"/></g>')

def sandia():
    """The Sandias at sunset over Albuquerque — watermelon light on the crest, the bosque below."""
    range_ = ('<path d="M0 262l120-34 90 22 110-40 150 46 140-30 120 36 160-24 120 30 160-40 160 34 110-20v148H0z" fill="#c9b8a3"/>'
              '<path d="M760 300l90-70 70 24 60-58 90 36 80-44 90 42 80-30 120 40v70H760z" fill="#c97a6a"/>'
              '<path d="M980 250l60-40 60 30 60-46 80 40 60-28 140 46v58H980z" fill="#a85c52"/>')
    town = '<g fill="#143f45" opacity=".85">' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{306-y}"/>' for x, y, w in [(330,270,26),(362,258,18),(386,246,30),(422,266,22),(450,238,16),(472,262,34),(512,272,20)]) + '</g>'
    return wrap(sun(1120, 96, 58, "#e6a77a") + range_ + town + ground(306, "#8a9a76") + '<path d="M0 330C300 322 600 340 900 330 1200 322 1350 336 1440 330V360H0Z" fill="#3f8f8f" opacity=".55"/>'
                + cottonwood(180, 330, .8) + cottonwood(640, 328, .7) + balloon(1300, 150, .45, "#deaa6e", "#a6321e"), SUNSET)
def balloons():
    """Balloon Fiesta morning: a sky full of envelopes, the Sandias behind, cottonwoods along the river."""
    far = '<path d="M0 286l200-30 160 22 200-40 220 34 200-28 180 30 280-26v112H0z" fill="#c9b8a3"/>'
    bs = balloon(260, 120, .9) + balloon(520, 70, .6, "#deaa6e", "#2f8a8a") + balloon(700, 150, 1.0, "#a6321e", "#deaa6e") + balloon(960, 60, .55, "#2f8a8a", "#f3ede2") \
        + balloon(1160, 130, .8, "#deaa6e", "#a6321e") + balloon(1340, 80, .5, "#6b7d5a", "#deaa6e")
    return wrap(sun(120, 100, 50) + far + bs + ground(312, "#8a9a76") + cottonwood(100, 318, .8) + cottonwood(840, 316, .9) + cottonwood(1240, 318, .7), MORNING)
def adobe_scene():
    """Adobe walls and vigas under the Sangre de Cristos — Santa Fe, Taos, the northern villages."""
    mts = ('<path d="M0 250l160-70 120 46 140-80 160 60 150-50 170 66 160-40 140 44 240-56v130H0z" fill="#b9a8a0"/>'
           '<path d="M340 262l100-50 80 30 110-56 90 40 100-30 110 44v70H340z" fill="#8f7a70"/>')
    bld = adobe(470, 236, 200, 124, "#c68a5c", door=560) + adobe(660, 210, 150, 150, "#b97e52") + adobe(800, 250, 130, 110, "#c68a5c") \
        + '<rect x="700" y="150" width="8" height="70" fill="#7a5238"/><rect x="724" y="150" width="8" height="70" fill="#7a5238"/>' + ''.join(f'<rect x="700" y="{y}" width="32" height="5" fill="#7a5238"/>' for y in range(158, 216, 14)) \
        + ristra(830, 262) + ristra(880, 262) + '<rect x="690" y="270" width="34" height="40" rx="3" fill="#2f8a8a"/>'
    return wrap(sun(1200, 110, 56) + mts + bld + ground(340, "#a98b6a") + pinon(300, 342, .9) + pinon(1100, 340, 1.0) + juniper(1240, 342, .8))
def whitesands():
    """White Sands: gypsum dunes against the San Andres, soaptree yucca on the crest."""
    mts = '<path d="M0 240l180-60 140 40 160-70 180 50 170-40 160 56 170-34 140 40 140-30v128H0z" fill="#b9a8a0"/>'
    dunes = ('<path d="M0 300C240 260 420 320 640 282 860 250 1060 316 1440 276V360H0Z" fill="#f3ede2"/>'
             '<path d="M0 330C300 300 560 350 820 318 1080 292 1260 340 1440 320V360H0Z" fill="#e6dfd1"/>'
             '<path d="M0 346C360 336 700 356 1440 340V360H0Z" fill="#d9d0bf"/>')
    return wrap(sun(1160, 104, 64, "#e6c48f") + mts + dunes + yucca(300, 318, 1.0) + yucca(1180, 322, .8), MORNING)
def bosque():
    """The Rio Grande bosque in October — cottonwood gold, the river, the Sandias faint behind."""
    far = '<path d="M0 270l220-36 180 26 200-44 240 40 200-30 200 34 200-24v124H0z" fill="#d6c6b3"/>'
    river = '<path d="M0 320C260 306 520 336 780 322 1040 308 1260 334 1440 318V360H0Z" fill="#3f8f8f" opacity=".7"/>'
    trees = ''.join(cottonwood(x, 316, s, f) for x, s, f in [(90,1.0,"#d4a13f"),(230,.8,"#e0b555"),(380,1.1,"#c9902f"),(560,.9,"#d4a13f"),(720,.7,"#e0b555"),(900,1.0,"#c9902f"),(1080,.8,"#d4a13f"),(1240,1.1,"#e0b555"),(1400,.9,"#c9902f")])
    return wrap(sun(1180, 112, 58) + far + ground(312, "#8a9a76") + trees + river)
def shiprock():
    """Shiprock rising off the desert floor, the volcanic dikes running out to the horizon."""
    rock = ('<path d="M560 330l60-120 30 30 40-110 30 50 30-70 40 90 30-40 50 170z" fill="#5b4a45"/>'
            '<path d="M690 190l40-90 30 50 30-70 40 90 30-40 20 70-190 0z" fill="#4a3b37"/>'
            '<path d="M0 334l560-14v14zM880 320l560 16v-2z" fill="#6a5a52"/>')
    return wrap(sun(1200, 100, 54, "#e6a77a") + '<path d="M0 286l1440-18v92H0z" fill="#c9b8a3"/>' + mesa(140, 200, 250, 36, "#b59a86") + mesa(1180, 180, 262, 26, "#b59a86")
                + ground(334, "#b8935e") + juniper(200, 342, .7, "#6b7d5a") + juniper(1300, 340, .6, "#6b7d5a"), SUNSET)
def ristras():
    """An adobe wall hung with chile ristras, a turquoise gate, a Hatch-valley sun."""
    wall = adobe(380, 200, 680, 160, "#c68a5c", vigas=False) + '<rect x="380" y="196" width="680" height="8" rx="3" fill="#b97e52"/>' \
        + ''.join(ristra(x, 226, 9) for x in range(420, 1040, 62)) + '<rect x="690" y="262" width="60" height="98" rx="4" fill="#2f8a8a"/><rect x="716" y="300" width="6" height="6" fill="#deaa6e"/>'
    return wrap(sun(1240, 104, 58) + '<path d="M0 262l1440-20v118H0z" fill="#d6c6b3"/>' + wall + ground(350, "#a98b6a") + pinon(200, 350, .9) + juniper(1240, 352, .8))
def pinon_scene():
    """Piñon-juniper country: mesas, a mountain wall, the trees that give the state its scent."""
    mts = ('<path d="M0 240l150-60 130 40 150-76 160 50 150-44 160 62 160-40 140 42 240-50v136H0z" fill="#b9a8a0"/>'
           '<path d="M220 262l100-50 80 30 100-56 100 40 90-30 100 44v70H220z" fill="#8f7a70"/>')
    trees = ''.join(pinon(x, 326, s) for x, s in [(80,1.0),(150,.7),(260,1.1),(420,.8),(700,.9),(860,1.1),(1010,.7),(1180,1.0),(1330,.8)]) + juniper(560, 330, .9) + juniper(1260, 332, .7)
    return wrap(sun(1160, 116, 60) + mts + mesa(900, 260, 246, 30, "#a98b6a") + ground(326, "#8a9a76") + trees)
def plains():
    """The eastern plains: a pumpjack, a grain elevator, a windmill and a very big sky."""
    pj = ('<g transform="translate(300 330)" fill="#5a4a3c"><rect x="-4" y="-70" width="8" height="70"/><path d="M-60-64l120-14 4 8-120 14z"/><rect x="-70" y="-78" width="24" height="22" rx="4"/>'
          '<path d="M56-78l6 4-14 40-6-4z"/><circle cx="46" cy="-34" r="12" fill="none" stroke="#5a4a3c" stroke-width="5"/></g>')
    elev = '<g fill="#8a7a6a"><rect x="1040" y="196" width="70" height="140"/><path d="M1040 196h70l-35-26z"/><rect x="1120" y="236" width="90" height="100"/></g>'
    wm = ('<g transform="translate(700 332)" stroke="#5a4a3c" stroke-width="4" fill="none"><path d="M-18 0L0-110L18 0M-13-36h26"/>'
          '<g transform="translate(0 -118)"><circle r="20"/><path d="M0-20V20M-20 0H20M-14-14L14 14M14-14L-14 14"/></g></g>')
    return wrap(sun(560, 118, 68, "#e6c48f") + '<path d="M0 312L1440 302V360H0Z" fill="#c9a97a"/>' + ground(334, "#b8a76c") + pj + elev + wm)
def organ():
    """The Organ Mountains over the Mesilla Valley — pecan rows and chile fields below."""
    spires = ('<path d="M760 300l40-90 30 60 30-110 30 70 30-96 40 80 24-50 40 84 30-60 40 90 50-40 60 62v40H760z" fill="#b07a6a"/>'
              '<path d="M900 300l30-100 30 60 20-70 30 76 30-40 40 74H900z" fill="#8f5d52"/>')
    rows = ''.join(f'<path d="M0 {y}L1440 {y-10}" stroke="#4d6444" stroke-width="{w}" opacity=".7"/>' for y, w in [(322, 5), (334, 6), (346, 7)])
    chile = ''.join(f'<circle cx="{x}" cy="{352 + (x // 40) % 3}" r="3" fill="#a6321e"/>' for x in range(30, 700, 40))
    return wrap(sun(200, 104, 56, "#e6a77a") + '<path d="M0 280l760 0 680-20v100H0z" fill="#c9b8a3"/>' + spires + ground(318, "#8a9a76") + rows + chile + yucca(1320, 318, .8), SUNSET)

SCENES = {"sandia": sandia(), "balloons": balloons(), "adobe": adobe_scene(), "whitesands": whitesands(), "bosque": bosque(),
          "shiprock": shiprock(), "ristras": ristras(), "pinon": pinon_scene(), "plains": plains(), "organ": organ()}
