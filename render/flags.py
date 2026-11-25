"""Tiny country flags (14x10 px) for the index, drawn as inline SVG by hand.

Each flag is a simplified rendering at icon size: correct colours and the main
shape (stripes, canton, disc, star) so it reads as that country at a glance.
No image files are used.
"""

W, H = 14, 10


def star(cx, cy, r, fill):
    # five-point star centred on (cx, cy) with outer radius r
    import math
    pts = []
    for k in range(10):
        rad = r if k % 2 == 0 else r * 0.42
        a = -math.pi / 2 + k * math.pi / 5
        pts.append("%.2f,%.2f" % (cx + rad * math.cos(a), cy + rad * math.sin(a)))
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'


def hstripes(colors):
    h = H / len(colors)
    return "".join(f'<rect y="{i*h:.2f}" width="{W}" height="{h + .05:.2f}" fill="{c}"/>' for i, c in enumerate(colors))


def vstripes(colors):
    w = W / len(colors)
    return "".join(f'<rect x="{i*w:.2f}" width="{w + .05:.2f}" height="{H}" fill="{c}"/>' for i, c in enumerate(colors))


def ua():
    return hstripes(["#0057b7", "#ffd700"])


def fr():
    return vstripes(["#002395", "#ffffff", "#ed2939"])


def eu():
    import math
    dots = "".join(star(7 + 3.1 * math.cos(k * math.pi / 6), 5 + 3.1 * math.sin(k * math.pi / 6), .75, "#ffcc00")
                   for k in range(12))
    return f'<rect width="{W}" height="{H}" fill="#003399"/>{dots}'


def se():
    return (f'<rect width="{W}" height="{H}" fill="#006aa7"/>'
            '<rect x="4" width="2" height="10" fill="#fecc00"/><rect y="4" width="14" height="2" fill="#fecc00"/>')


def sn():
    return vstripes(["#00853f", "#fdef42", "#e31b23"]) + star(7, 5, 2.4, "#00853f")


def cd():
    return (f'<rect width="{W}" height="{H}" fill="#007fff"/>'
            '<path d="M0,10 L0,8.2 L11.6,0 L14,0 L14,1.8 L2.4,10 Z" fill="#f7d618"/>'
            '<path d="M0,10 L0,9.1 L12.8,0 L14,0 L14,.9 L1.2,10 Z" fill="#ce1021"/>'
            + star(2.6, 2.4, 1.8, "#f7d618"))


def za():
    return (f'<rect width="{W}" height="5" fill="#de3831"/><rect y="5" width="{W}" height="5" fill="#002395"/>'
            '<path d="M0,0 L5.5,5 L0,10 Z" fill="#ffb612"/>'
            '<path d="M0,1.4 L4,5 L0,8.6 Z" fill="#000"/>'
            '<path d="M0,-.4 L6,4 L14,4 L14,6 L6,6 L0,10.4 L0,9 L5.4,5 L0,1 Z" fill="#fff"/>'
            '<path d="M0,.6 L5.8,4.4 L14,4.4 L14,5.6 L5.8,5.6 L0,9.4 L0,8.2 L4.7,5 L0,1.8 Z" fill="#007a4d"/>')


def us():
    s = "".join(f'<rect y="{i*10/7:.2f}" width="{W}" height="{10/14 + .02:.2f}" fill="#b22234"/>' for i in range(7))
    return f'<rect width="{W}" height="{H}" fill="#fff"/>{s}<rect width="6.2" height="5.4" fill="#3c3b6e"/>'


def cu():
    s = "".join(f'<rect y="{i*2}" width="{W}" height="2" fill="{"#002a8f" if i % 2 == 0 else "#fff"}"/>' for i in range(5))
    return s + '<path d="M0,0 L6.6,5 L0,10 Z" fill="#cf142b"/>' + star(2.3, 5, 1.6, "#fff")


def br():
    return (f'<rect width="{W}" height="{H}" fill="#009c3b"/>'
            '<path d="M7,1.2 L12.6,5 L7,8.8 L1.4,5 Z" fill="#ffdf00"/>'
            '<circle cx="7" cy="5" r="2.2" fill="#002776"/>')


def np():
    # Nepal's double pennant on a light ground
    return (f'<rect width="{W}" height="{H}" fill="#f4f1ea"/>'
            '<path d="M4,.3 L10.6,5 L6.6,5 L10.6,9.7 L4,9.7 Z" fill="#003893"/>'
            '<path d="M4.7,1.5 L8.6,4.3 L5.2,4.3 L9,9 L4.7,9 Z" fill="#dc143c"/>'
            '<circle cx="6" cy="3.4" r=".7" fill="#fff"/><circle cx="6" cy="7.2" r=".9" fill="#fff"/>')


def cn():
    return (f'<rect width="{W}" height="{H}" fill="#de2910"/>' + star(2.8, 2.7, 1.9, "#ffde00")
            + star(5.4, 1.1, .55, "#ffde00") + star(6.2, 2.4, .55, "#ffde00")
            + star(6.2, 3.9, .55, "#ffde00") + star(5.4, 5.1, .55, "#ffde00"))


def sg():
    return (f'<rect width="{W}" height="5" fill="#ef3340"/><rect y="5" width="{W}" height="5" fill="#fff"/>'
            '<circle cx="3.2" cy="2.5" r="1.8" fill="#fff"/><circle cx="3.9" cy="2.5" r="1.6" fill="#ef3340"/>'
            '<circle cx="5.2" cy="1.5" r=".35" fill="#fff"/><circle cx="6" cy="2.2" r=".35" fill="#fff"/>'
            '<circle cx="5.7" cy="3.2" r=".35" fill="#fff"/><circle cx="4.7" cy="3.2" r=".35" fill="#fff"/>'
            '<circle cx="4.4" cy="2.2" r=".35" fill="#fff"/>')


def my():
    s = "".join(f'<rect y="{i*10/14:.2f}" width="{W}" height="{10/14 + .02:.2f}" fill="{"#cc0001" if i % 2 == 0 else "#fff"}"/>'
                for i in range(14))
    return (s + '<rect width="7" height="5.7" fill="#010066"/>'
            '<circle cx="2.8" cy="2.85" r="2" fill="#fc0"/><circle cx="3.4" cy="2.85" r="1.7" fill="#010066"/>'
            + star(5.2, 2.85, 1.3, "#fc0"))


def bd():
    return f'<rect width="{W}" height="{H}" fill="#006a4e"/><circle cx="6.2" cy="5" r="2.9" fill="#f42a41"/>'


def kp():
    return (f'<rect width="{W}" height="{H}" fill="#024fa2"/><rect y="1.7" width="{W}" height="6.6" fill="#fff"/>'
            '<rect y="2.3" width="14" height="5.4" fill="#ed1c27"/><circle cx="4.8" cy="5" r="2" fill="#fff"/>'
            + star(4.8, 5.1, 1.8, "#ed1c27"))


def jp():
    return f'<rect width="{W}" height="{H}" fill="#fff"/><circle cx="7" cy="5" r="3" fill="#bc002d"/>'


def au():
    return (f'<rect width="{W}" height="{H}" fill="#012169"/>'
            '<path d="M0,0 L7,5 M7,0 L0,5" stroke="#fff" stroke-width="1.1"/>'
            '<path d="M0,0 L7,5 M7,0 L0,5" stroke="#e4002b" stroke-width=".45"/>'
            '<path d="M3.5,0 L3.5,5 M0,2.5 L7,2.5" stroke="#fff" stroke-width="1.5"/>'
            '<path d="M3.5,0 L3.5,5 M0,2.5 L7,2.5" stroke="#e4002b" stroke-width=".8"/>'
            + star(3.5, 7.6, 1.3, "#fff") + star(10.6, 2, .7, "#fff") + star(12.3, 4.4, .6, "#fff")
            + star(10.6, 8, .7, "#fff") + star(9.2, 4.6, .6, "#fff"))


FLAGS = {"UA": ua, "FR": fr, "EU": eu, "SE": se, "SN": sn, "CD": cd, "ZA": za, "US": us, "CU": cu,
         "BR": br, "NP": np, "CN": cn, "SG": sg, "MY": my, "BD": bd, "KP": kp, "JP": jp, "AU": au}


def flag(code):
    return (f'<svg class="flag" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{FLAGS[code]()}'
            f'<rect x=".25" y=".25" width="{W - .5}" height="{H - .5}" fill="none" stroke="#CCC" stroke-width=".5"/></svg>')
