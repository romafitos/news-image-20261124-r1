"""Small hand-written SVG scenes for the front page.

Every drawing is plain SVG built from shapes typed here; no clip art, fonts
or images are pulled in. Hero scenes are 300x90, card scenes 180x48.
"""

from stories import ULLEUNG_TIME

INK = "#111111"
NAVY = "#1d2b45"
SEA = "#6b98b8"
SKY = "#dfe8ee"
RED = "#c8102e"
FIRE = "#e8792b"
GOLD = "#e2b33c"
GREEN = "#2f7d4f"
GREY = "#8a8f96"
PAPER = "#f8f6f0"


def svg(w, h, body, bg=None):
    back = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice">{back}{body}</svg>')


def light(key, sx, sy):
    # soft directional light for a hero scene: a warm glow from the light source (sx, sy as 0-1 of the frame)
    # fading out, plus a gentle shade toward the far corner; flat shapes stay flat underneath
    return (f'<defs><radialGradient id="glow-{key}" cx="{sx}" cy="{sy}" r="0.9">'
            f'<stop offset="0" stop-color="#fff4d6" stop-opacity=".24"/>'
            f'<stop offset=".55" stop-color="#fff4d6" stop-opacity=".04"/>'
            f'<stop offset="1" stop-color="#0b1220" stop-opacity=".18"/></radialGradient></defs>'
            f'<rect width="300" height="90" fill="url(#glow-{key})"/>')


def tanker(x, y, s=1.0, burning=False):
    hull = (f'<path d="M{x},{y} l{70*s},0 l{-8*s},{12*s} l{-58*s},0 z" fill="{INK}"/>'
            f'<rect x="{x+50*s}" y="{y-12*s}" width="{14*s}" height="{12*s}" fill="#3a3f47"/>'
            f'<rect x="{x+53*s}" y="{y-18*s}" width="{4*s}" height="{6*s}" fill="#3a3f47"/>')
    if burning:
        hull += (f'<path d="M{x+18*s},{y} q{6*s},{-22*s} {10*s},{-8*s} q{4*s},{-16*s} {10*s},{-2*s} '
                 f'q{5*s},{-10*s} {6*s},{10*s} z" fill="{FIRE}"/>'
                 f'<path d="M{x+24*s},{y} q{4*s},{-12*s} {6*s},{-3*s} q{3*s},{-8*s} {6*s},{3*s} z" fill="{GOLD}"/>'
                 f'<ellipse cx="{x+34*s}" cy="{y-34*s}" rx="{18*s}" ry="{8*s}" fill="#4a4a4a" opacity=".55"/>'
                 f'<ellipse cx="{x+46*s}" cy="{y-46*s}" rx="{14*s}" ry="{6*s}" fill="#4a4a4a" opacity=".4"/>')
    return hull


def hero_hormuz():
    # dusk over the strait: one tanker burning, a second listing, a mine, and the US claim of clear lanes
    body = (f'<rect width="300" height="54" fill="#e9a66a"/>'
            f'<circle cx="262" cy="20" r="10" fill="#ffd27a"/>'
            f'<path d="M0,40 q40,-12 90,-4 q30,4 60,-2 l0,20 l-150,0 z" fill="#8c6a48"/>'
            f'<rect y="54" width="300" height="36" fill="{SEA}"/>'
            + tanker(14, 66, 1.05, True) + tanker(112, 70, 0.8, True) + tanker(206, 66, 0.85, False)
            + f'<circle cx="96" cy="82" r="4" fill="{INK}"/><path d="M92,82 l-4,0 M100,82 l4,0 M96,78 l0,-4" stroke="{INK}" stroke-width="1.5"/>'
            f'<path d="M190,80 l100,0" stroke="#fff" stroke-width="1.5" stroke-dasharray="4 3"/>'
            f'<text x="240" y="76" text-anchor="middle" font-family="Noto Sans" font-size="8" font-weight="800" fill="#fff">US: LANES CLEAR</text>'
            + light("hormuz", 0.87, 0.2))
    return svg(300, 90, body)


def hero_markets():
    # trading-floor wall: three index boards over a city skyline at dusk
    sky = '<rect width="300" height="90" fill="#6d8bb0"/><rect y="60" width="300" height="30" fill="#55709a"/>'
    skyline = ('<path d="M0,90 l0,-26 l14,0 l0,-10 l10,0 l0,10 l10,0 l0,-22 l12,0 l0,22 l8,0 l0,-14 l14,0 l0,40 z" fill="#3c5274"/>'
               '<path d="M262,90 l0,-30 l10,0 l0,-12 l3,-8 l3,8 l0,12 l10,0 l0,-18 l12,0 l0,48 z" fill="#3c5274"/>')
    lights = "".join(f'<rect x="{266+(i%3)*9}" y="{66+(i//3)*7}" width="3" height="3" fill="{GOLD}"/>' for i in range(9))
    boards = ""
    for i, (lab, pct, h) in enumerate([("TAIEX", "+8.99%", 30), ("KOSPI", "+6.32%", 22), ("NIKKEI", "+3.91%", 14)]):
        x = 82 + i * 60
        boards += (f'<rect x="{x}" y="24" width="54" height="62" fill="#0f1a2b" stroke="#7ee0a1" stroke-width="1"/>'
                   f'<text x="{x+27}" y="35" text-anchor="middle" font-family="Noto Sans" font-size="8.5" font-weight="800" fill="#cfe9d8">{lab}</text>'
                   f'<text x="{x+27}" y="49" text-anchor="middle" font-family="Noto Sans" font-size="11.5" font-weight="900" fill="#7ee0a1">{pct}</text>'
                   f'<rect x="{x+15}" y="{82-h}" width="24" height="{h}" fill="{GREEN}"/>')
    return svg(300, 90, sky + skyline + lights + boards + light("markets", 0.5, 0.05))


def jet(x, y, s=1.0, color=INK):
    return (f'<path d="M{x},{y} l{22*s},{-3*s} l{6*s},{-8*s} l{4*s},0 l{-3*s},{8*s} l{8*s},{-1*s} '
            f'l{3*s},{-4*s} l{3*s},0 l{-1*s},{5*s} l{-1*s},{5*s} l{-3*s},0 l{-3*s},{-4*s} l{-8*s},{-1*s} '
            f'l{3*s},{8*s} l{-4*s},0 l{-6*s},{-8*s} z" fill="{color}"/>')


def hero_ulleung():
    # East Sea seen from above: Korean coast, the KADIZ edge, two bomber tracks passing Ulleung,
    # and the phone alert the islanders got
    body = (f'<rect width="300" height="90" fill="#7fb0cf"/>'
            f'<path d="M0,0 l46,0 q-6,18 4,34 q8,16 -2,30 q-6,14 4,26 l-52,0 z" fill="#a9c79a"/>'
            f'<text x="6" y="14" font-family="Noto Sans" font-size="8" font-weight="800" fill="#2d4a2a">KOREA</text>'
            f'<path d="M206,0 q26,44 12,90" stroke="#fff" stroke-width="1.4" stroke-dasharray="5 3" fill="none"/>'
            f'<text x="190" y="84" font-family="Noto Sans" font-size="7.5" font-weight="800" fill="#fff">KADIZ</text>'
            f'<path d="M296,8 q-90,14 -150,40 q-40,18 -60,40" stroke="{RED}" stroke-width="1.8" stroke-dasharray="3 2" fill="none"/>'
            f'<path d="M296,24 q-80,14 -140,40 q-30,14 -50,26" stroke="{RED}" stroke-width="1.8" stroke-dasharray="3 2" fill="none"/>'
            + jet(200, 26, 0.9) + jet(226, 40, 0.9)
            + f'<path d="M104,46 q6,-8 14,-4 q6,6 -2,12 q-10,2 -12,-8 z" fill="{GREEN}" stroke="#1f4a2e" stroke-width="1"/>'
            f'<text x="88" y="68" font-family="Noto Sans" font-size="8" font-weight="900" fill="#111">ULLEUNG</text>'
            f'<rect x="246" y="38" width="48" height="48" rx="5" fill="{INK}"/><rect x="250" y="44" width="40" height="36" fill="#f6efe0"/>'
            f'<rect x="250" y="44" width="40" height="10" fill="{RED}"/>'
            f'<text x="270" y="52" text-anchor="middle" font-family="Noto Sans" font-size="6.5" font-weight="900" fill="#fff">AIR RAID</text>'
            f'<text x="270" y="64" text-anchor="middle" font-family="Noto Sans" font-size="6.5" font-weight="800" fill="#111">SHELTER</text>'
            f'<text x="270" y="75" text-anchor="middle" font-family="Noto Sans Mono" font-size="8.5" font-weight="700" fill="{RED}">{ULLEUNG_TIME}</text>'
            + light("ulleung", 0.15, 0.1))
    return svg(300, 90, body)


def hero_drones():
    body = (f'<rect width="300" height="90" fill="#1c2233"/>'
            + "".join(f'<circle cx="{(i*53)%300}" cy="{(i*29)%40+4}" r="1" fill="#cfd6e4"/>' for i in range(18))
            + '<path d="M0,90 l0,-30 l20,0 l0,-12 l22,0 l0,12 l18,0 l0,-26 l30,0 l0,26 l16,0 l0,-16 l24,0 l0,46 z" fill="#2e3647"/>'
            '<path d="M170,90 l0,-52 l44,0 l0,52 z" fill="#3a4357"/>'
            + "".join(f'<rect x="{176+(i%4)*9}" y="{44+(i//4)*9}" width="5" height="5" fill="#59647d"/>' for i in range(16))
            + f'<path d="M198,38 l8,-10 l6,12 l10,-6 l-4,14 z" fill="{FIRE}"/>'
            '<path d="M230,90 l0,-36 l30,0 l0,36 z M266,90 l0,-24 l34,0 l0,24 z" fill="#2e3647"/>'
            + "".join(f'<path d="M{40+i*44},{16+(i%3)*9} l12,3 l-12,3 l3,-3 z" fill="#e6e9ef"/>'
                      f'<path d="M{20+i*44},{19+(i%3)*9} l18,0" stroke="#e6e9ef" stroke-width=".8" stroke-dasharray="2 2"/>' for i in range(5)))
    return svg(300, 90, body)


def hero_football():
    body = (f'<rect width="300" height="90" fill="#13281c"/>'
            f'<path d="M0,40 l300,0 l0,50 l-300,0 z" fill="#2f7d4f"/>'
            f'<path d="M0,40 l300,0" stroke="#e8efe9" stroke-width="1.5"/>'
            f'<ellipse cx="150" cy="66" rx="26" ry="9" fill="none" stroke="#e8efe9" stroke-width="1.2"/>'
            f'<path d="M150,40 l0,50" stroke="#e8efe9" stroke-width="1.2"/>'
            + "".join(f'<circle cx="{8+i*12}" cy="{10+(i%3)*8}" r="5" fill="#2c3b33"/>' for i in range(25))
            + '<path d="M30,0 l10,20 M270,0 l-10,20" stroke="#fff6c8" stroke-width="3" opacity=".7"/>'
            f'<circle cx="214" cy="60" r="6" fill="#fff"/><path d="M211,57 l6,6 M217,57 l-6,6" stroke="{INK}" stroke-width="1"/>')
    return svg(300, 90, body)


# ---------- card scenes (180 x 48) ----------

def card(body, bg=SKY):
    return svg(180, 48, body, bg)


def c_quake():
    return card('<path d="M0,48 l0,-14 l40,-6 l30,8 l40,-12 l70,6 l0,18 z" fill="#8d8a7a"/>'
                '<path d="M0,26 l20,0 l6,-14 l8,28 l8,-22 l6,14 l6,-6 l8,0 l120,0" stroke="#c8102e" stroke-width="2" fill="none"/>'
                '<path d="M100,14 l14,-10 l16,10 l12,-6 l14,6 l0,6 l-56,0 z" fill="#fff"/>', "#e7e2d4")


def c_rocket():
    return card('<rect width="180" height="48" fill="#1c2233"/>'
                + "".join(f'<circle cx="{(i*37)%180}" cy="{(i*13)%44+2}" r=".9" fill="#dfe3ea"/>' for i in range(14))
                + '<path d="M90,4 q8,8 8,22 l0,12 l-16,0 l0,-12 q0,-14 8,-22 z" fill="#e9ecf1"/>'
                '<path d="M82,30 l-6,10 l6,-2 z M98,30 l6,10 l-6,-2 z" fill="#c8102e"/>'
                '<path d="M84,38 q6,12 12,0 z" fill="#e8792b"/>'
                '<rect x="118" y="8" width="44" height="12" fill="#c9cdd5"/><rect x="134" y="20" width="12" height="10" fill="#c9cdd5"/>', None)


def c_gavel():
    return card('<rect x="20" y="38" width="140" height="6" fill="#6b5a45"/>'
                '<path d="M60,30 l40,-22 l6,10 l-40,22 z" fill="#3e3226"/>'
                '<rect x="94" y="2" width="16" height="22" transform="rotate(-30 102 13)" fill="#3e3226"/>'
                '<rect x="118" y="26" width="28" height="12" fill="#3e3226"/>', "#efe6d6")


def c_flag_pair(a, b):
    return card(f'<rect x="38" y="10" width="44" height="28" fill="{a}"/><rect x="98" y="10" width="44" height="28" fill="{b}"/>'
                '<path d="M86,26 l8,0" stroke="#111" stroke-width="2"/>', "#efe9df")


def c_ship():
    return card('<rect y="32" width="180" height="16" fill="#2f5d7c"/>'
                '<path d="M40,32 l100,0 l-10,10 l-80,0 z" fill="#3a3f47"/>'
                '<rect x="64" y="20" width="16" height="12" fill="#c8102e"/><rect x="82" y="20" width="16" height="12" fill="#2f7d4f"/>'
                '<rect x="100" y="20" width="16" height="12" fill="#e2b33c"/><rect x="118" y="14" width="10" height="18" fill="#e9ecf1"/>')


def c_court_building():
    return card('<path d="M40,16 l50,-12 l50,12 z" fill="#d8d2c4"/>'
                + "".join(f'<rect x="{48+i*18}" y="18" width="8" height="22" fill="#d8d2c4"/>' for i in range(6))
                + '<rect x="40" y="40" width="100" height="6" fill="#b8b0a0"/>', "#5b6b7d")


def c_pill():
    return card('<rect x="54" y="14" width="72" height="22" rx="11" fill="#6c4fc4"/>'
                '<rect x="90" y="14" width="36" height="22" rx="11" fill="#56b0e0"/><rect x="90" y="14" width="12" height="22" fill="#56b0e0"/>'
                '', "#eef0f6")


def c_blast():
    return card('<rect y="36" width="180" height="12" fill="#6e6a62"/>'
                '<path d="M30,36 l0,-18 l30,0 l0,18 z M120,36 l0,-24 l34,0 l0,24 z" fill="#4a4f59"/>'
                '<path d="M88,36 l-14,-12 l10,0 l-6,-16 l12,10 l4,-14 l6,14 l12,-8 l-6,16 l10,0 l-14,10 z" fill="#e8792b"/>'
                '<path d="M92,34 l-6,-8 l6,0 l0,-8 l6,8 l6,-4 l-4,12 z" fill="#e2b33c"/>', "#d9d4cb")


def c_chess():
    sq = "".join(f'<rect x="{50+(i%8)*10}" y="{4+(i//8)*5}" width="10" height="5" fill="{"#7b5e3b" if (i+i//8)%2 else "#e8d8b8"}"/>' for i in range(64))
    return card(sq + '<circle cx="146" cy="16" r="7" fill="#111"/><path d="M139,40 l14,0 l-3,-18 l-8,0 z" fill="#111"/>'
                '<circle cx="30" cy="16" r="7" fill="#fff" stroke="#111"/><path d="M23,40 l14,0 l-3,-18 l-8,0 z" fill="#fff" stroke="#111"/>', "#cfc6b5")


def c_crown():
    return card('<path d="M60,38 l0,-22 l14,12 l16,-20 l16,20 l14,-12 l0,22 z" fill="#e2b33c"/>'
                '<rect x="60" y="38" width="60" height="5" fill="#b8892a"/>'
                '<circle cx="90" cy="26" r="3" fill="#c8102e"/>', "#2b1e3d")


def c_chart_down():
    return card('<path d="M10,12 l30,6 l30,-2 l30,10 l30,4 l40,12" stroke="#c8102e" stroke-width="3" fill="none"/>'
                '<path d="M10,40 l160,0" stroke="#888" stroke-width="1"/>', "#f1efe8")


def c_chart_up():
    return card('<path d="M10,40 l30,-8 l30,2 l30,-12 l30,-4 l40,-14" stroke="#2f7d4f" stroke-width="3" fill="none"/>'
                '<path d="M10,42 l160,0" stroke="#888" stroke-width="1"/>', "#f1efe8")


def c_plane():
    return card('<path d="M0,48 l0,-12 q40,-20 80,-6 q40,-16 100,2 l0,16 z" fill="#3f6b3f"/>'
                '<path d="M60,14 l50,0 l10,-6 l4,0 l-4,8 l8,0 l-4,4 l-60,0 z" fill="#e9ecf1"/>'
                '<text x="128" y="24" font-family="Noto Sans" font-size="16" font-weight="800" fill="#c8102e">?</text>', "#cdd8de")


def c_storm():
    return card('<ellipse cx="60" cy="14" rx="40" ry="11" fill="#5b6470"/><ellipse cx="116" cy="12" rx="36" ry="10" fill="#4a525d"/>'
                '<path d="M96,22 l-8,12 l8,0 l-6,12" stroke="#e2b33c" stroke-width="2.5" fill="none"/>'
                + "".join(f'<path d="M{30+i*14},28 l-4,10" stroke="#7fa6c4" stroke-width="1.5"/>' for i in range(5)), "#aab4bf")


def c_phone_ban():
    return card('<rect x="74" y="4" width="32" height="40" rx="4" fill="#111"/><rect x="78" y="9" width="24" height="28" fill="#56b0e0"/>'
                '<circle cx="90" cy="24" r="20" fill="none" stroke="#c8102e" stroke-width="3"/>'
                '<path d="M76,10 l28,28" stroke="#c8102e" stroke-width="3"/>', "#efe9df")


def c_moon():
    return card('<circle cx="90" cy="24" r="17" fill="#f2e6c2"/><circle cx="84" cy="20" r="3" fill="#e0d2a6"/><circle cx="96" cy="30" r="4" fill="#e0d2a6"/>'
                + "".join(f'<circle cx="{(i*41)%180}" cy="{(i*17)%46}" r=".9" fill="#dfe3ea"/>' for i in range(12)), "#141a2b")


def c_ballot():
    return card('<rect x="64" y="20" width="52" height="24" fill="#d8d2c4"/><rect x="80" y="18" width="20" height="4" fill="#111"/>'
                '<rect x="82" y="2" width="16" height="20" fill="#fff" stroke="#111"/><path d="M85,12 l4,4 l6,-8" stroke="#2f7d4f" stroke-width="2" fill="none"/>', "#e7ecf2")


def c_building_fire():
    return card('<rect x="56" y="10" width="68" height="38" fill="#5a5f6a"/>'
                + "".join(f'<rect x="{62+(i%5)*12}" y="{14+(i//5)*10}" width="6" height="6" fill="{"#e8792b" if i in (2,3,8) else "#8e95a3"}"/>' for i in range(15))
                + '<path d="M84,10 q6,-12 12,0" fill="#e8792b"/>', "#d6dbe2")


def c_handshake():
    return card('<path d="M40,30 l30,-10 l20,6 l20,-6 l30,10 l-26,10 l-24,-4 l-24,4 z" fill="#c99a6e"/>'
                '<path d="M36,32 l-10,0 l0,-14 l14,0 z M144,32 l10,0 l0,-14 l-14,0 z" fill="#1d2b45"/>', "#efe9df")


def c_satellite():
    return card('<rect width="180" height="48" fill="#141a2b"/><rect x="82" y="18" width="16" height="12" fill="#c9cdd5"/>'
                '<rect x="46" y="20" width="34" height="8" fill="#56b0e0"/><rect x="100" y="20" width="34" height="8" fill="#56b0e0"/>'
                '<circle cx="150" cy="40" r="20" fill="#2f5d7c"/>', None)


def c_drones():
    return card('<rect width="180" height="48" fill="#8494b3"/>'
                '<path d="M0,48 l0,-16 l24,0 l0,-8 l20,0 l0,8 l14,0 l0,16 z M118,48 l0,-20 l26,0 l0,20 z" fill="#3e4a63"/>'
                '<path d="M62,48 l0,-34 l40,0 l0,34 z" fill="#3a4357"/>'
                + "".join(f'<rect x="{67+(i%4)*9}" y="{18+(i//4)*8}" width="5" height="4" fill="#59647d"/>' for i in range(12))
                + '<path d="M88,14 l6,-10 l4,10 l8,-4 l-4,10 z" fill="#e8792b"/>'
                + "".join(f'<path d="M{110+i*22},{8+(i%2)*8} l10,3 l-10,3 l2,-3 z" fill="#e6e9ef"/>' for i in range(3)), None)


def c_strike():
    return card('<rect y="34" width="180" height="14" fill="#cbbd9f"/>'
                '<path d="M30,34 l0,-16 l26,0 l0,16 z M64,34 l0,-24 l22,0 l0,24 z M128,34 l0,-14 l30,0 l0,14 z" fill="#a8997b"/>'
                '<ellipse cx="100" cy="20" rx="16" ry="12" fill="#5a5a5a" opacity=".7"/><ellipse cx="108" cy="10" rx="12" ry="8" fill="#5a5a5a" opacity=".5"/>'
                '<path d="M92,34 l6,-14 l6,8 l6,-10 l4,16 z" fill="#e8792b"/>', "#e9dcc3")


def c_oil():
    # derrick scaled down so its crown sits well inside the frame; pipeline and a flare
    return card('<rect y="40" width="180" height="8" fill="#b89a74"/>'
                '<path d="M46,40 l9,-24 l9,24 M49,32 l12,0 M51.5,25 l7,0 M50,40 l10,-12 M60,40 l-10,-12" '
                'stroke="#111" stroke-width="2" fill="none"/><rect x="52" y="13" width="6" height="4" fill="#111"/>'
                '<path d="M96,40 l0,-8 l40,0 l0,8 z" fill="#333"/><path d="M104,32 l20,-12 l18,4 l-4,6 l-14,-2 l-16,8 z" fill="#111"/>'
                '<rect x="64" y="36" width="34" height="3" fill="#555"/>'
                '<circle cx="150" cy="17" r="6" fill="#e8792b"/>', "#f1d9b8")


def c_report():
    # Alamata after artillery fire: shell-struck houses, craters in the road, smoke columns
    return card('<rect y="34" width="180" height="14" fill="#b9a98a"/>'
                '<path d="M28,34 l0,-14 l10,-7 l10,7 l0,14 z" fill="#9c8f78"/>'
                '<path d="M40,13 l8,7 l0,14 l-5,0 l-3,-6 l-2,3 z" fill="#e7e2d4"/>'
                '<path d="M58,34 l0,-18 l26,0 l0,6 l-6,4 l-4,-5 l-5,7 l-4,-4 l-3,4 z" fill="#8a7f6c"/>'
                '<rect x="62" y="21" width="5" height="5" fill="#2b2b2b"/><rect x="73" y="20" width="4" height="4" fill="#2b2b2b"/>'
                '<path d="M120,34 l0,-12 l12,-6 l14,6 l0,12 z" fill="#9c8f78"/>'
                '<path d="M128,22 l6,-4 l4,6 l-3,3 l-2,-3 l-3,4 z" fill="#e7e2d4"/>'
                '<ellipse cx="98" cy="40" rx="9" ry="2.6" fill="#5b4f3d"/><ellipse cx="98" cy="39.5" rx="5" ry="1.4" fill="#2e271d"/>'
                '<ellipse cx="152" cy="42" rx="7" ry="2.2" fill="#5b4f3d"/><ellipse cx="44" cy="43" rx="6" ry="1.8" fill="#5b4f3d"/>'
                '<path d="M88,38 l-6,-3 M108,38 l6,-4 M98,36 l0,-5" stroke="#5b4f3d" stroke-width="1.2"/>'
                '<ellipse cx="80" cy="10" rx="12" ry="6" fill="#4a4a4a" opacity=".6"/>'
                '<ellipse cx="72" cy="4" rx="9" ry="4" fill="#4a4a4a" opacity=".45"/>'
                '<ellipse cx="140" cy="10" rx="10" ry="5" fill="#4a4a4a" opacity=".55"/>'
                '<path d="M76,18 l3,-6 l3,6 z M136,18 l3,-5 l3,5 z" fill="#e8792b"/>', "#e7ddc9")


def c_trophy():
    # Senegal's flag: green, yellow, red, with the green star centred on the yellow band
    import math
    pts = []
    for k in range(10):
        r = 11 if k % 2 == 0 else 4.6
        ang = -math.pi / 2 + k * math.pi / 5
        pts.append("%.2f,%.2f" % (90 + r * math.cos(ang), 22 + r * math.sin(ang)))
    return card('<rect x="0" y="0" width="60" height="48" fill="#00853f"/><rect x="60" y="0" width="60" height="48" fill="#fdef42"/>'
                '<rect x="120" y="0" width="60" height="48" fill="#e31b23"/>'
                f'<polygon points="{" ".join(pts)}" fill="#00853f"/>', None)


SCENES = {
    "trophy": c_trophy,
    "drones": c_drones, "strike": c_strike, "oil": c_oil, "report": c_report,
    "quake": c_quake, "rocket": c_rocket, "gavel": c_gavel, "ship": c_ship, "court": c_court_building,
    "pill": c_pill, "blast": c_blast, "chess": c_chess, "crown": c_crown, "down": c_chart_down,
    "up": c_chart_up, "plane": c_plane, "storm": c_storm, "phone": c_phone_ban, "moon": c_moon,
    "ballot": c_ballot, "fire": c_building_fire, "deal": c_handshake, "satellite": c_satellite,
}

HEROES = {
    "hormuz": hero_hormuz, "markets": hero_markets, "ulleung": hero_ulleung,
    "drones": hero_drones, "football": hero_football,
}
