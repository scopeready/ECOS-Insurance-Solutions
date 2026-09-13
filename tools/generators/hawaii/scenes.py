"""Hero scenes for the Hawaii site — layered-silhouette SVG, brand palette (ocean, lava, plumeria, koa, sand)."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f7f3ea"/><stop offset="1" stop-color="#d5e8ee"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
RAINSKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef0ec"/><stop offset="1" stop-color="#c9d9dc"/></linearGradient></defs>'
           '<rect width="1440" height="360" fill="url(#sky)"/>')
def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=62, c="#e7c486"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".65"/>'
def ground(y, fill, op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def water(y, fill="#0d4f6c", op="1"):
    return (f'<path d="M0 {y}C240 {y-6} 480 {y+6} 720 {y} 960 {y-6} 1200 {y+6} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
            f'<path d="M0 {y+22}c120-6 240 6 360 0s240-6 360 0 240 6 360 0 240-6 360 0" stroke="#e9f3f6" stroke-width="2" fill="none" opacity=".45"/>')
def sand(y=332, fill="#e8dcc0"):
    return f'<path d="M0 {y}C300 {y-8} 600 {y+10} 900 {y} 1200 {y-8} 1350 {y+6} 1440 {y}V360H0Z" fill="{fill}"/>'
def palm(x, y, h=110, lean=10, fill="#3f6b4a"):
    top = (x + lean, y - h)
    fronds = ''.join(f'<path d="M{top[0]} {top[1]}q{dx*0.5} {dy*0.3-18} {dx} {dy}" stroke="{fill}" stroke-width="7" fill="none" stroke-linecap="round"/>'
                     for dx, dy in [(-58, 8), (-44, -22), (-14, -34), (18, -32), (46, -18), (58, 10)])
    return f'<path d="M{x} {y}q{lean*0.6} {-h*0.55} {lean} {-h}" stroke="#5a4a3c" stroke-width="9" fill="none" stroke-linecap="round"/>{fronds}<circle cx="{top[0]}" cy="{top[1]+4}" r="7" fill="#6b4a2a"/>'
def cloud(x, y, s=1.0, fill="#ffffff", op=".8"):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="{fill}" opacity="{op}"><ellipse cx="0" cy="0" rx="60" ry="22"/>'
            '<ellipse cx="-30" cy="-8" rx="34" ry="20"/><ellipse cx="26" cy="-10" rx="40" ry="24"/></g>')
def plumeria(x, y, s=1.0):
    petals = ''.join(f'<ellipse cx="0" cy="-9" rx="5" ry="9" fill="#fff6e6" transform="rotate({a})"/>' for a in range(0, 360, 72))
    return f'<g transform="translate({x} {y}) scale({s})">{petals}<circle r="3.5" fill="#e7c486"/></g>'
def canoe(x, y, s=1.0, fill="#5a4a3c"):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-70 0q70 22 140 0l-10 12q-60 16-120 0z" fill="{fill}"/>'
            f'<path d="M-40 4l-30-26M-30 -22h60" stroke="{fill}" stroke-width="4" stroke-linecap="round"/><path d="M-70 -22q-10 10-4 24" stroke="{fill}" stroke-width="5" fill="none"/>'
            f'<rect x="-10" y="-30" width="6" height="30" fill="{fill}"/><rect x="26" y="-30" width="6" height="30" fill="{fill}"/><circle cx="-7" cy="-36" r="6" fill="{fill}"/><circle cx="29" cy="-36" r="6" fill="{fill}"/></g>')
def rain(x0=0, x1=1440, y0=60, y1=300, step=46, c="#8fb0b8"):
    return '<g stroke="' + c + '" stroke-width="1.5" opacity=".5">' + ''.join(f'<path d="M{x} {y0 + (i % 3) * 30}l-6 40"/>' for i, x in enumerate(range(x0, x1, step))) + '</g>'

def diamondhead():
    # Waikiki: Diamond Head crater profile, hotel towers, palms, ocean.
    crater = '<path d="M780 250C860 214 940 176 1020 168 1100 160 1160 190 1240 214 1320 236 1380 250 1440 254V360H780Z" fill="#7a8a6a"/><path d="M960 190c40-14 80-16 120-8-40 10-80 14-120 8z" fill="#5f6f52"/>'
    towers = '<g fill="#2b5a70">' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{300-y}"/>' for x, y, w in [(300,200,28),(336,170,34),(378,186,26),(412,150,38),(458,178,30),(496,196,40),(544,166,28),(580,190,32)]) + '</g>'
    windows = '<g fill="#e7c486" opacity=".6">' + ''.join(f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in [(346,190),(346,210),(422,170),(436,190),(552,186),(590,206),(310,220)]) + '</g>'
    return wrap(sun(1140, 110, 58) + cloud(240, 96, .9) + cloud(700, 70, .7, op=".7") + crater + towers + windows
                + water(296) + sand(330) + palm(120, 334, 120, 12) + palm(680, 336, 96, -10) + plumeria(1300, 320, 1.4) + plumeria(1330, 330, 1.0))
def koolau():
    # Windward: fluted Koolau cliffs, low cloud, Kaneohe Bay.
    cliffs = ('<path d="M0 230C120 120 220 96 330 108 440 120 520 200 640 190 760 180 820 110 940 118 1060 126 1140 210 1260 200 1360 192 1400 176 1440 180V360H0Z" fill="#3f6b4a"/>'
              '<g stroke="#2f5238" stroke-width="3" fill="none" opacity=".7">' + ''.join(f'<path d="M{x} {y}l-10 90"/>' for x, y in [(150,150),(230,120),(300,112),(380,130),(560,196),(700,188),(860,124),(980,124),(1080,170),(1200,204),(1320,196)]) + '</g>')
    return wrap(cloud(200, 150, 1.4, op=".85") + cloud(900, 140, 1.6, op=".85") + cloud(1300, 170, 1.0, op=".8") + cliffs + ground(292, "#5a8a5e")
                + water(314, "#2b7a9a") + sand(340, "#e8dcc0") + palm(1320, 342, 100, -8), sky=RAINSKY)
def pearlharbor():
    # Leeward: harbor water, ship silhouettes, Waianae range, warm sunset.
    range_ = '<path d="M0 240C160 200 300 170 440 176 580 182 700 230 860 226 1020 222 1160 190 1440 210V360H0Z" fill="#8a7a6a"/>'
    ships = ('<g fill="#1b2a30"><path d="M300 300h220l-16 18H316z"/><rect x="380" y="270" width="60" height="30"/><rect x="404" y="252" width="14" height="18"/>'
             '<path d="M900 304h160l-12 14H912z"/><rect x="960" y="282" width="40" height="22"/><rect x="976" y="268" width="8" height="14"/></g>')
    memorial = '<path d="M620 296h110v-8q-30-14-55-6-25-8-55 6z" fill="#f7f3ea"/><rect x="640" y="296" width="70" height="6" fill="#dfeef3"/>'
    return wrap(sun(1120, 130, 70, "#e7b07a") + cloud(300, 90, .8, op=".6") + range_ + water(292, "#0d4f6c") + ships + memorial + sand(338, "#d9c9a6") + palm(120, 340, 110, 10) + palm(1340, 340, 90, -8))
def plantation():
    # Central Oahu: pineapple/cane field rows, plantation town roofs, Waianae ridge.
    ridge = '<path d="M0 232C180 186 320 172 480 184 640 196 760 236 900 228 1040 220 1180 176 1440 200V360H0Z" fill="#6f8a5a"/>'
    rows = '<g stroke="#4f7a48" stroke-width="3" fill="none" opacity=".8">' + ''.join(f'<path d="M0 {y}C480 {y-14} 960 {y+14} 1440 {y}"/>' for y in range(282, 356, 12)) + '</g>'
    town = ('<g fill="#b5471f"><path d="M560 262l30-22 30 22z"/><path d="M640 266l26-18 26 18z"/><path d="M700 262l34-24 34 24z"/></g>'
            '<g fill="#f7f3ea"><rect x="566" y="262" width="48" height="22"/><rect x="646" y="266" width="40" height="18"/><rect x="708" y="262" width="52" height="22"/></g>'
            '<rect x="820" y="230" width="10" height="56" fill="#5a4a3c"/><rect x="800" y="222" width="50" height="14" fill="#5a4a3c"/>')
    return wrap(sun(1160, 112, 60) + cloud(200, 80, 1.0, op=".7") + ridge + ground(276, "#5f8a4e") + rows + town + palm(1200, 286, 96, 8) + palm(160, 288, 84, -8))
def haleakala():
    # Maui: Haleakala's long shoulder, West Maui mountains, cane-field green, Kahului bay.
    hale = '<path d="M520 254C700 180 880 120 1060 118 1200 116 1330 170 1440 190V360H520Z" fill="#7a6a5a"/><path d="M980 132c30-8 60-8 90 0-30 6-60 6-90 0z" fill="#5a4a3c"/>'
    west = '<path d="M0 256C80 200 160 168 260 176 360 184 440 236 560 250V360H0Z" fill="#3f6b4a"/>'
    return wrap(sun(200, 104, 52) + cloud(1100, 150, 1.3, op=".8") + cloud(760, 190, .9, op=".75") + hale + west + ground(296, "#5f8a4e")
                + water(324, "#2b7a9a") + sand(344) + palm(1300, 346, 90, -10) + plumeria(120, 336, 1.3))
def maunakea():
    # Hilo side: rain, Mauna Kea's snowcapped dome behind, rainforest, observatories.
    dome = '<path d="M300 236C500 170 700 140 900 138 1100 136 1250 170 1440 214V360H300Z" fill="#7a7a80"/><path d="M780 156c60-14 140-16 200-2-60 8-140 8-200 2z" fill="#f7f3ea"/>'
    obs = '<g fill="#dfeef3"><rect x="840" y="140" width="10" height="10"/><circle cx="845" cy="139" r="6"/><rect x="900" y="144" width="8" height="8"/><circle cx="904" cy="143" r="5"/></g>'
    forest = ('<path d="M0 262C200 250 300 240 460 258 620 276 760 262 900 272 1040 282 1240 268 1440 276V360H0Z" fill="#2f5238"/>'
              + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="34" ry="18" fill="#3f6b4a"/>' for x, y in [(80,270),(220,258),(400,268),(560,282),(720,270),(880,280),(1040,286),(1200,276),(1360,282)]))
    return wrap(rain(0, 1440, 40, 300, 52) + cloud(240, 120, 1.5, "#e6ecec", ".9") + dome + obs + forest + ground(306, "#3f6b4a") + water(334, "#2b7a9a", ".9"), sky=RAINSKY)
def kona():
    # Kona side: coffee slopes of Hualalai, lava shoreline, calm sea, coffee shrubs.
    slope = '<path d="M0 200C240 150 480 132 720 150 960 168 1200 226 1440 232V360H0Z" fill="#6f8a5a"/>'
    shrubs = '<g fill="#3f6b4a">' + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="18" ry="12"/>' for x, y in [(100,236),(160,240),(220,236),(280,244),(340,240),(400,250),(460,246),(520,254),(580,252),(640,262),(700,258),(760,268),(820,266)]) + '</g>'
    lava = '<path d="M0 300C200 292 360 308 560 300 760 292 940 310 1140 302 1300 296 1380 306 1440 300V360H0Z" fill="#1b2a30"/>'
    return wrap(sun(1160, 116, 66, "#e7b07a") + slope + shrubs + lava + water(322, "#0d4f6c") + palm(1240, 306, 100, -10) + palm(1320, 308, 80, 8) + plumeria(60, 288, 1.2))
def napali():
    # Kauai: Na Pali cliffs stepping into the sea, sea stack, surf, palms.
    cliffs = ('<path d="M0 150C80 120 120 100 200 110 280 120 300 200 360 220 420 240 470 190 540 200 610 210 640 260 720 262 800 264 830 230 900 236V360H0Z" fill="#3f6b4a"/>'
              '<path d="M0 200C60 180 120 170 180 190 240 210 260 250 330 262 400 274 440 250 500 254 560 258 590 290 640 290V360H0Z" fill="#2f5238"/>'
              '<g stroke="#2a4a32" stroke-width="3" fill="none" opacity=".7">' + ''.join(f'<path d="M{x} {y}l-8 70"/>' for x, y in [(90,130),(160,116),(240,140),(320,200),(400,214),(480,204),(560,220),(680,262)]) + '</g>')
    stack = '<path d="M1080 300l14-70 18-10 12 80z" fill="#3f6b4a"/>'
    return wrap(sun(1200, 108, 60) + cloud(1000, 80, 1.0, op=".7") + cliffs + stack + water(302, "#0d4f6c") + water(318, "#2b7a9a", ".8") + sand(344) + palm(1340, 346, 96, -8))
def outrigger():
    # Statewide: outrigger canoe on open water at sunrise, distant island.
    island = '<path d="M980 262C1060 236 1140 224 1220 226 1300 228 1380 250 1440 258V300H980Z" fill="#7a8a6a" opacity=".9"/>'
    return wrap(sun(720, 130, 74) + cloud(300, 90, 1.1, op=".7") + cloud(1160, 120, .9, op=".7") + island + water(280, "#0d4f6c") + water(300, "#2b7a9a", ".85")
                + canoe(520, 292, 1.3) + sand(344) + palm(140, 346, 110, 12) + plumeria(1360, 334, 1.3))

SCENES = {"diamondhead": diamondhead(), "koolau": koolau(), "pearlharbor": pearlharbor(), "plantation": plantation(), "haleakala": haleakala(),
          "maunakea": maunakea(), "kona": kona(), "napali": napali(), "outrigger": outrigger()}
