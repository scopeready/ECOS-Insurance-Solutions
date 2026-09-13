"""Hero scenes for the Indiana site — layered-silhouette SVG in the Hoosier palette (limestone cream, cornfield green, red brick)."""
SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f5f0e3"/><stop offset="1" stop-color="#dde5e0"/></linearGradient></defs>'
       '<rect width="1440" height="360" fill="url(#sky)"/>')
FAR, MID, GREEN, DEEP = "#cfd6cc", "#9fb489", "#5f7d3c", "#2e5a3a"
BRICK, GOLD, STONE, WATER, INK = "#9b3b25", "#e6c26a", "#e3d8bd", "#4f7f95", "#2a3a32"

def wrap(inner, sky=SKY):
    return '<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">' + sky + inner + '</svg>'
def sun(cx=1160, cy=118, r=60, c=GOLD):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".6"/>'
def ground(y, fill, op="1"):
    return f'<path d="M0 {y}C240 {y-8} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+8} 1440 {y}V360H0Z" fill="{fill}" opacity="{op}"/>'
def oak(x, y, s=1.0, f=GREEN):
    """A round-crowned hardwood — the oak and maple that line every Indiana county road."""
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-6" y="-34" width="12" height="38" fill="#4a3728"/>'
            f'<path d="M-58-34c-24-26 4-70 44-64 18-30 72-22 74 10 30-2 44 40 12 52-8 22-52 24-74 8-22 14-64 10-56-6z" fill="{f}"/></g>')
def cornrows(y, spacing=26, h=22, f=GREEN):
    """Corn stalks along a field edge."""
    return '<g>' + ''.join(f'<path d="M{x} {y}v-{h}M{x} {y-h*0.55}l-9-8M{x} {y-h*0.7}l9-8M{x} {y-h*0.35}l-8-6" stroke="{f}" stroke-width="2.4" fill="none"/>'
                           f'<ellipse cx="{x}" cy="{y-h-3}" rx="2.4" ry="5" fill="{GOLD}"/>' for x in range(20, 1440, spacing)) + '</g>'
def elevator(x, y, s=1.0, f="#8d8577"):
    """A grain elevator: silo cluster, headhouse and leg."""
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="0" y="-120" width="40" height="120" fill="{f}"/><rect x="44" y="-120" width="40" height="120" fill="{f}"/>'
            f'<rect x="88" y="-120" width="40" height="120" fill="{f}"/><path d="M0-120a20 20 0 0 1 40 0zM44-120a20 20 0 0 1 40 0zM88-120a20 20 0 0 1 40 0z" fill="{f}"/>'
            f'<rect x="132" y="-150" width="26" height="150" fill="#6f685c"/><rect x="128" y="-162" width="34" height="14" fill="#6f685c"/><rect x="60" y="-80" width="70" height="80" fill="#7a7266"/></g>')
def barn(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0v-48l10-16 30-16 30 16 10 16V0z" fill="{BRICK}"/><path d="M0-48l10-16 30-16 30 16 10 16z" fill="#7a2c1a"/>'
            f'<rect x="30" y="-30" width="20" height="30" fill="#4a3728"/><rect x="34" y="-56" width="12" height="10" fill="{STONE}"/></g>')

def monument():
    """Downtown Indianapolis: Soldiers' and Sailors' Monument on the Circle, skyline behind."""
    b = f'<g fill="#3d4f46">' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in
        [(380,190,36),(424,150,40),(474,110,48),(530,168,34),(572,96,44),(624,178,36),(1020,164,36),(1064,120,56),(1128,150,40),(1176,182,34),(1216,140,44),(1268,196,36)]) + '</g>'
    b += '<path d="M572 96l22-24 22 24z" fill="#3d4f46"/><rect x="1080" y="100" width="16" height="20" fill="#3d4f46"/>'
    w = f'<g fill="{GOLD}" opacity=".7">' + ''.join(f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in [(488,130),(500,150),(586,120),(598,150),(1076,140),(1090,164),(1226,160),(1140,170)]) + '</g>'
    mon = (f'<g fill="{STONE}"><rect x="700" y="300" width="112" height="60"/><rect x="716" y="286" width="80" height="16"/><rect x="738" y="120" width="36" height="170"/>'
           f'<rect x="732" y="112" width="48" height="10"/><rect x="730" y="250" width="52" height="8"/></g>'
           f'<path d="M756 60l7 14 15 2-11 10 3 15-14-8-14 8 3-15-11-10 15-2z" fill="{GOLD}"/><rect x="750" y="88" width="12" height="26" fill="{STONE}"/>'
           f'<g fill="{STONE}"><ellipse cx="690" cy="330" rx="24" ry="8"/><ellipse cx="822" cy="330" rx="24" ry="8"/></g>')
    return wrap(sun(1200, 100, 52) + f'<path d="M0 262L1440 240V360H0Z" fill="{FAR}"/>' + b + w + mon + ground(334, DEEP, ".95")
                + f'<path d="M0 346C360 340 720 352 1080 344 1260 340 1350 346 1440 344" stroke="{GOLD}" stroke-width="2" fill="none" opacity=".4"/>')

def speedway():
    """The Indianapolis Motor Speedway: grandstand, the pagoda, the yard of bricks."""
    stand = f'<path d="M160 300L160 200L1280 200L1280 300Z" fill="#6d7f74"/>' + ''.join(f'<rect x="{160}" y="{y}" width="1120" height="3" fill="#dfe5df" opacity=".5"/>' for y in range(212, 300, 14))
    roof = f'<path d="M140 200L720 168L1300 200L1300 208L140 208Z" fill="#4c5c53"/>' + ''.join(f'<rect x="{x}" y="176" width="4" height="26" fill="#4c5c53"/>' for x in range(180, 1280, 90))
    pagoda = (f'<g fill="#3d4f46"><rect x="684" y="120" width="72" height="180"/><path d="M660 130h120l-14-14H674z"/><path d="M664 172h112l-12-12H676z"/><path d="M668 214h104l-10-10H678z"/></g>'
              f'<g fill="{GOLD}" opacity=".7"><rect x="696" y="140" width="10" height="14"/><rect x="734" y="140" width="10" height="14"/><rect x="696" y="184" width="10" height="14"/><rect x="734" y="184" width="10" height="14"/></g>')
    track = f'<path d="M0 320C300 312 600 326 900 318 1200 310 1350 322 1440 318V360H0Z" fill="#4a4a4a"/>' + f'<rect x="700" y="318" width="40" height="42" fill="{BRICK}"/>' + f'<path d="M0 340H1440" stroke="#f5f0e3" stroke-width="3" opacity=".6"/>'
    flag = f'<g transform="translate(300 250)"><rect x="0" y="-70" width="3" height="70" fill="{INK}"/><path d="M3-70h44v30H3z" fill="#f5f0e3"/>' + ''.join(f'<rect x="{3+i*11}" y="{-70+j*10}" width="11" height="10" fill="{INK}"/>' for i in range(4) for j in range(3) if (i+j)%2==0) + '</g>'
    return wrap(sun(1180, 110, 56) + f'<path d="M0 262L1440 250V360H0Z" fill="{FAR}"/>' + roof + stand + pagoda + track + flag)

def dunes():
    """Lake Michigan from the Indiana Dunes: water, marram grass, a distant mill stack."""
    grass = '<g>' + ''.join(f'<path d="M{x} 330c-4-10-2-22 4-30M{x+6} 330c2-12 8-20 14-24" stroke="{GREEN}" stroke-width="2" fill="none"/>' for x in range(30, 1440, 46)) + '</g>'
    mill = f'<g fill="#5c6b66" opacity=".55"><rect x="60" y="230" width="90" height="34"/><rect x="80" y="180" width="10" height="50"/><rect x="120" y="196" width="8" height="34"/><path d="M85 180c-4-14 4-24 10-30 6 6 12 16 6 30z" fill="#c9d1ce"/></g>'
    gull = f'<g stroke="{INK}" stroke-width="2.5" fill="none"><path d="M600 120c10-10 20-10 30 0M630 120c10-10 20-10 30 0"/><path d="M900 90c8-8 16-8 24 0M924 90c8-8 16-8 24 0"/></g>'
    return wrap(sun(1150, 112, 66) + mill + f'<path d="M0 240L1440 236V360H0Z" fill="{WATER}"/>' + f'<path d="M0 252C300 246 600 258 900 250 1200 244 1350 254 1440 250V360H0Z" fill="#3d6c82" opacity=".85"/>'
                + f'<path d="M0 300C240 262 520 300 760 276 1000 256 1220 296 1440 270V360H0Z" fill="{STONE}"/>' + f'<path d="M0 330C300 310 620 338 900 318 1150 302 1330 330 1440 320V360H0Z" fill="#d9cdae"/>' + grass + gull)

def mill():
    """The Region: a steel mill on the lakefront, Gary and Hammond's skyline of stacks."""
    stacks = f'<g fill="#5c6b66">' + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{300-y}"/>' for x, y, w in [(300,150,18),(340,120,22),(420,170,16),(700,110,26),(760,160,20),(1000,140,24),(1060,180,16)]) + '</g>'
    sheds = f'<g fill="#6d7f74"><rect x="200" y="230" width="360" height="70"/><path d="M200 230l60-30h240l60 30z"/><rect x="640" y="240" width="300" height="60"/><path d="M640 240l50-26h200l50 26z"/><rect x="980" y="250" width="200" height="50"/></g>'
    plumes = f'<g fill="#e4e8e6" opacity=".7"><ellipse cx="351" cy="106" rx="26" ry="12"/><ellipse cx="380" cy="90" rx="30" ry="14"/><ellipse cx="713" cy="96" rx="28" ry="12"/><ellipse cx="746" cy="80" rx="34" ry="14"/><ellipse cx="1012" cy="126" rx="22" ry="10"/></g>'
    return wrap(sun(1200, 104, 48, "#e7b07a") + plumes + f'<path d="M0 262L1440 252V360H0Z" fill="{FAR}"/>' + stacks + sheds
                + f'<path d="M0 300C300 296 600 306 900 300 1200 294 1350 304 1440 300V360H0Z" fill="{WATER}"/>' + f'<path d="M0 330C240 326 480 334 720 330 960 326 1200 334 1440 330V360H0Z" fill="#3d6c82" opacity=".85"/>')

def coveredbridge():
    """Parke County: a red covered bridge over a creek, sycamores on the bank."""
    bridge = (f'<g><rect x="520" y="200" width="400" height="90" fill="{BRICK}"/><path d="M510 200l200-40 200 40z" fill="#7a2c1a"/><rect x="520" y="290" width="400" height="10" fill="#4a3728"/>'
              f'<path d="M560 290v-56a30 30 0 0 1 60 0v56z" fill="{INK}" opacity=".85"/><path d="M820 290v-56a30 30 0 0 1 60 0v56z" fill="{INK}" opacity=".85"/>'
              f'<g fill="#f5f0e3" opacity=".8"><rect x="660" y="230" width="18" height="22"/><rect x="700" y="230" width="18" height="22"/><rect x="740" y="230" width="18" height="22"/></g>'
              f'<rect x="540" y="300" width="18" height="40" fill="#5b5148"/><rect x="882" y="300" width="18" height="40" fill="#5b5148"/></g>')
    creek = f'<path d="M0 330C300 322 600 340 900 330 1200 322 1350 336 1440 330V360H0Z" fill="{WATER}"/>'
    return wrap(sun(1170, 114, 58) + f'<path d="M0 250C240 232 500 256 760 240 1020 224 1240 250 1440 236V360H0Z" fill="{FAR}"/>'
                + f'<path d="M0 290C260 270 520 300 780 282 1040 264 1240 296 1440 276V360H0Z" fill="{MID}"/>' + ground(314, GREEN) + creek + bridge + oak(240, 314, 1.1) + oak(1180, 312, .9, DEEP))

def farm():
    """Corn and soybean country: fields to the horizon, a grain elevator, a red barn."""
    rows = '<g>' + ''.join(f'<path d="M{x} 360L{720+(x-720)*0.3} 296" stroke="#7e9a58" stroke-width="2" opacity=".55"/>' for x in range(-200, 1700, 60)) + '</g>'
    return wrap(sun(1170, 116, 62) + f'<path d="M0 262L1440 254V360H0Z" fill="{FAR}"/>' + f'<path d="M0 282C300 276 700 288 1440 278V360H0Z" fill="{MID}"/>'
                + elevator(1040, 296, .9) + barn(220, 296, 1.1) + oak(360, 296, .8, DEEP) + ground(296, GREEN) + rows + cornrows(340, 24, 26, DEEP))

def quarry():
    """Southern Indiana limestone: quarry benches, a derrick, and the cut stone that built the country."""
    benches = (f'<g fill="{STONE}"><path d="M120 360V250h300v30h-60v30h-80v30h-60v20z"/><path d="M1000 360V240h320v40h-70v30h-90v30h-60v20z"/></g>'
               f'<g fill="#cdbf9e"><rect x="120" y="250" width="300" height="6"/><rect x="180" y="280" width="240" height="6"/><rect x="260" y="310" width="160" height="6"/><rect x="1000" y="240" width="320" height="6"/><rect x="1000" y="280" width="250" height="6"/><rect x="1000" y="310" width="160" height="6"/></g>')
    derrick = f'<g stroke="#5b5148" stroke-width="4" fill="none"><path d="M700 340L720 180L740 340M706 300h28M710 260h20M714 220h12"/><path d="M720 180L860 260" stroke-width="3"/><path d="M860 260v40" stroke-width="2"/></g><rect x="846" y="300" width="28" height="22" fill="{STONE}"/>'
    blocks = f'<g fill="{STONE}"><rect x="560" y="322" width="48" height="26"/><rect x="612" y="322" width="48" height="26"/><rect x="586" y="296" width="48" height="26"/></g>'
    return wrap(sun(1180, 110, 60) + f'<path d="M0 256C300 240 700 262 1440 244V360H0Z" fill="{FAR}"/>' + f'<path d="M0 290C300 272 700 300 1440 280V360H0Z" fill="{MID}"/>' + ground(348, "#d9cdae") + benches + derrick + blocks + oak(480, 318, .8, DEEP))

def river():
    """The Ohio River: a towboat pushing barges, the Kentucky hills beyond, a bridge downstream."""
    bridge = f'<g stroke="#5c6b66" stroke-width="5" fill="none"><path d="M900 282h540"/><path d="M960 282v-60M1080 282v-60M1200 282v-60M1320 282v-60"/><path d="M900 282C1000 200 1100 200 1200 282M1200 282C1260 230 1330 230 1440 270" stroke-width="3"/></g>'
    barge = (f'<g><rect x="180" y="300" width="360" height="22" fill="#5b5148"/><rect x="200" y="290" width="150" height="10" fill="#4a3f36"/><rect x="370" y="290" width="150" height="10" fill="#4a3f36"/>'
             f'<rect x="540" y="280" width="70" height="42" fill="#3d4f46"/><rect x="560" y="256" width="36" height="24" fill="#3d4f46"/><rect x="584" y="236" width="8" height="20" fill="#3d4f46"/></g>')
    return wrap(sun(1160, 112, 64) + f'<path d="M0 240C300 224 700 250 1440 226V360H0Z" fill="{FAR}"/>' + f'<path d="M0 270C260 254 520 280 780 264 1040 248 1240 276 1440 258V360H0Z" fill="{MID}"/>'
                + bridge + f'<path d="M0 296C300 290 600 302 900 296 1200 290 1350 300 1440 296V360H0Z" fill="{WATER}"/>' + f'<path d="M0 326C300 320 600 332 900 326 1200 320 1350 330 1440 326V360H0Z" fill="#3d6c82" opacity=".85"/>' + barge)

def courthouse():
    """A county-seat courthouse square: limestone courthouse with clock tower, brick storefronts, hardwoods."""
    ch = (f'<g fill="{STONE}"><rect x="560" y="200" width="320" height="140"/><rect x="600" y="180" width="240" height="20"/><rect x="690" y="90" width="60" height="90"/><path d="M684 90h72l-36-34z"/></g>'
          f'<circle cx="720" cy="130" r="14" fill="#f5f0e3" stroke="#5b5148" stroke-width="3"/><path d="M720 130v-9M720 130l6 4" stroke="#5b5148" stroke-width="2"/>'
          f'<g fill="#5b5148" opacity=".6">' + ''.join(f'<rect x="{x}" y="222" width="14" height="30"/><rect x="{x}" y="276" width="14" height="30"/>' for x in range(580, 870, 40)) + '</g>'
          f'<rect x="700" y="300" width="40" height="40" fill="#4a3728"/><g fill="{STONE}">' + ''.join(f'<rect x="{x}" y="200" width="8" height="140"/>' for x in (640, 672, 768, 800)) + '</g>')
    shops = (f'<g fill="{BRICK}"><rect x="140" y="250" width="70" height="90"/><rect x="216" y="236" width="90" height="104"/><rect x="312" y="256" width="70" height="84"/>'
             f'<rect x="1060" y="244" width="80" height="96"/><rect x="1146" y="258" width="70" height="82"/><rect x="1222" y="240" width="90" height="100"/></g>'
             f'<g fill="{STONE}" opacity=".85">' + ''.join(f'<rect x="{x}" y="{y}" width="14" height="20"/>' for x, y in [(160,268),(180,268),(236,254),(262,254),(282,254),(330,272),(352,272),(1080,262),(1108,262),(1164,276),(1188,276),(1242,258),(1268,258),(1290,258)]) + '</g>')
    return wrap(sun(1180, 108, 54) + f'<path d="M0 262L1440 250V360H0Z" fill="{FAR}"/>' + shops + ch + ground(340, GREEN) + oak(470, 340, .9) + oak(980, 338, .9, DEEP))

def lakes():
    """Northern Indiana lake country: Kosciusko and the St. Joseph valley — still water, cottages, a fishing pier."""
    pier = f'<rect x="880" y="292" width="220" height="7" fill="#8a6a48"/>' + ''.join(f'<rect x="{x}" y="299" width="5" height="26" fill="#6a4e34"/>' for x in range(896, 1100, 40))
    cottage = f'<g><rect x="240" y="262" width="80" height="44" fill="{BRICK}"/><path d="M232 262l48-30 48 30z" fill="#7a2c1a"/><rect x="270" y="280" width="16" height="26" fill="#4a3728"/><rect x="296" y="274" width="12" height="12" fill="{STONE}"/></g>'
    boat = f'<g><path d="M600 318l14 12h70l14-12z" fill="#5b5148"/><rect x="646" y="278" width="3" height="40" fill="#5b5148"/><path d="M649 278l30 32h-30z" fill="#f5f0e3"/></g>'
    return wrap(sun(1170, 118, 60) + f'<path d="M0 252C300 236 700 258 1440 240V360H0Z" fill="{FAR}"/>' + f'<path d="M0 278C260 262 520 288 780 272 1040 256 1240 284 1440 266V360H0Z" fill="{MID}"/>'
                + cottage + oak(150, 306, .8, DEEP) + oak(420, 306, .9) + ground(306, GREEN) + f'<path d="M0 318C300 312 600 324 900 318 1200 312 1350 322 1440 318V360H0Z" fill="{WATER}"/>' + pier + boat
                + f'<path d="M100 340c60-4 120 4 180 0M1200 346c60-4 120 4 180 0" stroke="#dfe8ee" stroke-width="2" fill="none" opacity=".5"/>')

SCENES = {"monument": monument(), "speedway": speedway(), "dunes": dunes(), "mill": mill(), "coveredbridge": coveredbridge(),
          "farm": farm(), "quarry": quarry(), "river": river(), "courthouse": courthouse(), "lakes": lakes()}
