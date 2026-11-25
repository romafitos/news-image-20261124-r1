"""Builds render/out/page.html: the Tuesday 24 November 2026 front page.

Run:  python3 render/page.py && bash render/shoot.sh
The page is fixed at 1024x1024 CSS px so Chromium's screenshot is the entry.
"""
import html
import os

import art
import stories
from flags import flag
from worldshape import LANDS, SEAS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")

# equirectangular (plate carree): 1 px per degree on both axes, so shapes keep true proportions
MAP_W, MAP_H = 352, 130
LAT_TOP, LAT_BOT, LON_L, LON_R = 80, -50, -170, 182
LAND, SEA, COAST = "#D8D3C8", "#EEF2F5", "#6B8299"
CONT = dict(stories.CONTINENTS)

# warm newsprint grain: seeded fractal noise (same seed, same pixels every run) at ~4% under the content
GRAIN = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='256' height='256'%3E"
         "%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.7' numOctaves='1' seed='24'/%3E"
         "%3CfeColorMatrix values='0 0 0 0 .42 0 0 0 0 .33 0 0 0 0 .2 0 0 0 1.6 -.5'/%3E"
         "%3CfeComponentTransfer%3E%3CfeFuncA type='discrete' tableValues='0 0 .5 1 1'/%3E%3C/feComponentTransfer%3E"
         "%3C/filter%3E%3Crect width='256' height='256' filter='url(%23g)' opacity='.04'/%3E%3C/svg%3E")


def esc(s):
    return html.escape(s, quote=False)


def proj(lon, lat):
    x = (lon - LON_L) / (LON_R - LON_L) * MAP_W
    y = (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * MAP_H
    return round(x, 1), round(y, 1)


def poly(pts):
    return "M" + " L".join("%s,%s" % proj(lo, la) for lo, la in pts) + " Z"


def world_map(pins):
    # graticule every 30 degrees, faint, under the land so it reads across the ocean only
    grid = "".join(f'<path d="M0,{proj(0, la)[1]} L{MAP_W},{proj(0, la)[1]}"/>' for la in (60, 30, 0, -30))
    grid += "".join(f'<path d="M{proj(lo, 0)[0]},0 L{proj(lo, 0)[0]},{MAP_H}"/>' for lo in range(-150, 181, 30))
    grid = f'<g stroke="{COAST}" stroke-opacity=".12" stroke-width=".7">{grid}</g>'
    shapes = [f'<path d="{poly(pts)}" fill="{LAND}"/>' for pts in LANDS.values()]
    shapes += [f'<path d="{poly(pts)}" fill="{SEA}"/>' for pts in SEAS.values()]
    coast = "".join(f'<path d="{poly(pts)}"/>' for pts in list(LANDS.values()) + list(SEAS.values()))
    coast = f'<g fill="none" stroke="{COAST}" stroke-width=".5" stroke-linejoin="round">{coast}</g>'
    marks = []
    for n, lon, lat, cont, dx, dy in pins:
        x, y = proj(lon, lat)
        lx, ly = x + dx, y + dy
        dense = n in stories.DENSE
        r = (6.5 if dense else 7.5) if n <= 3 else (5.6 if dense else 6.5)
        fs = 8 if dense else 9
        if dx or dy:  # leader line from the true spot to a nudged label
            marks.append(f'<path d="M{x},{y} L{lx},{ly}" stroke="#111" stroke-width=".8"/>')
        marks.append(f'<circle cx="{x}" cy="{y}" r="1.7" fill="#111"/>')
        ring = "#c8102e" if n <= 3 else "#fff"
        marks.append(f'<circle cx="{lx}" cy="{ly}" r="{r}" fill="{CONT[cont]}" stroke="{ring}" stroke-width="1.3"/>'
                     f'<text x="{lx}" y="{ly + fs * 0.36:.1f}" text-anchor="middle" font-family="Noto Sans" font-size="{fs}" '
                     f'font-weight="800" fill="#fff">{n}</text>')
    return (f'<svg width="{MAP_W}" height="{MAP_H}" viewBox="0 0 {MAP_W} {MAP_H}">'
            f'<rect width="{MAP_W}" height="{MAP_H}" fill="{SEA}"/>{grid}{"".join(shapes)}{coast}{"".join(marks)}</svg>')


def pin_boxes(pins):
    # label circles as (n, x, y, r) in map px, for the overlap check
    out = []
    for n, lon, lat, cont, dx, dy in pins:
        x, y = proj(lon, lat)
        dense = n in stories.DENSE
        r = (6.5 if dense else 7.5) if n <= 3 else (5.6 if dense else 6.5)
        out.append((n, x + dx, y + dy, r + 0.65))
    return out


TAG_CSS = {"CONFIRMED": "t-c", "OFFICIAL": "t-o", "REPORTED": "t-r", "CLAIM": "t-x"}


def tag(t):
    return f'<span class="tag {TAG_CSS[t]}">{t}</span>'


def hero(i, s):
    return (f'<div class="hero"><div class="hart">{art.HEROES[s["art"]]()}'
            f'<span class="num big">{i}</span><span class="place">{esc(s["place"])}</span>'
            f'<span class="hbig">{s["big"]}</span></div>'
            f'<div class="kick"><span class="lab">{esc(s["field"])}</span>{tag(s["tag"])}</div>'
            f'<h2>{esc(s["head"])}</h2><p class="dek">{esc(s["dek"])}</p>'
            f'<p class="src">{esc(s["src"])}</p></div>')


def small(i, s):
    return (f'<div class="card"><div class="cart">{art.SCENES[s["art"]]()}<span class="num">{i}</span>'
            f'<span class="artlab">{esc(s["big"])}</span></div>'
            f'<div class="kick"><span class="lab">{esc(s["place"])}</span>{tag(s["tag"])}</div>'
            f'<h3>{esc(s["head"])}</h3><p class="cdek">{esc(s["dek"])}</p></div>')


def index_line(i, s):
    col = CONT[s["cont"]]
    return (f'<li><b class="n" style="background:{col}">{i}</b>{flag(s["code"])}'
            f'<b class="pl">{esc(s["place"])}:</b> {esc(s["head"])}'
            f' <i class="ti {TAG_CSS[s["tag"]]}">{s["tag"][0]}</i></li>')


def index_list(items, first):
    # one coloured heading per continent, items keep their running numbers
    out, cur = [], None
    for k, s in enumerate(items):
        if s["cont"] != cur:
            cur = s["cont"]
            out.append(f'<li class="ch" style="color:{CONT[cur]};border-color:{CONT[cur]}">{cur}</li>')
        out.append(index_line(first + k, s))
    return "".join(out)


def cont_legend():
    return "".join(f'<span><i style="background:{c}"></i>{n.title()}</span>' for n, c in stories.CONTINENTS)


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1024px;height:1024px;overflow:hidden;background:#F8F6F0 url("GRAINURL");color:#111111;
 font-family:'Noto Sans',sans-serif;-webkit-font-smoothing:antialiased}
.page{padding:0 12px}
.strap{height:20px;background:#111111;color:#fff;font:800 11px/20px 'Noto Sans';letter-spacing:.9px;
 display:flex;justify-content:space-between;padding:0 12px;margin:0 -12px}
.strap .r{color:#ff6b7d}
.date{font:900 70px/69px 'Noto Serif',serif;letter-spacing:-1.5px;text-align:center;margin-top:0}
.deck{font:italic 600 13.5px/17px 'Noto Serif';text-align:center;color:#111;margin-bottom:2px;white-space:nowrap;padding-top:9px}
.deck b{color:#c8102e;font-style:normal;padding:0 5px}
.full{font:800 10.5px/14px 'Noto Sans';text-align:center;color:#c8102e;letter-spacing:.5px;margin:-2px 0 3px}
.utc{display:flex;background:#ece7da;border-top:1.5px solid #111;border-bottom:1px solid #111;
 font:600 10px/18px 'Noto Sans';white-space:nowrap;overflow:hidden;color:#111}
.utc .h{background:#111;color:#fff;font-weight:900;padding:0 7px;letter-spacing:.5px}
.utc span{padding:0 5px;border-right:1px solid #cfc8b6;flex:auto;text-align:center}
.utc span b{color:#c8102e;margin-right:3px;font-weight:900}
.regions{margin-top:3px;font:800 9px/14px 'Noto Sans';color:#fff;letter-spacing:.4px;background:#1d4f91;
 text-align:center;white-space:nowrap;overflow:hidden}
.nums{display:flex;border-bottom:1.5px solid #111;margin:3px 0 4px}
.nums div{flex:1;padding:1px 6px;border-left:1px solid #cfc8b6;font:600 9.5px/11px 'Noto Sans';color:#333}
.nums div:first-child{border-left:0;flex:.6;font:900 10px/12px 'Noto Sans';color:#111;padding-top:4px}
.nums b{display:block;font:900 20px/22px 'Noto Serif';color:#111}
.heroes{display:flex;gap:10px}
.hero{flex:1;width:0}
.hart{position:relative;height:100px;overflow:hidden;border:1px solid #111}
.hart svg{display:block;width:100%;height:100px}
.place{position:absolute;left:26px;top:4px;background:#111;color:#fff;font:800 9px/14px 'Noto Sans';padding:0 5px;letter-spacing:.4px}
.num{position:absolute;left:3px;top:3px;background:#c8102e;color:#fff;font:900 10px/15px 'Noto Sans';min-width:15px;text-align:center;border-radius:2px}
.num.big{font-size:11px;line-height:17px;min-width:19px}
.kick{display:flex;justify-content:space-between;align-items:center;margin:4px 0 1px;height:14px}
.lab{font:800 9.5px/12px 'Noto Sans';color:#c8102e;letter-spacing:.5px;text-transform:uppercase;white-space:nowrap;overflow:hidden}
.tag{font:800 8px/12px 'Noto Sans';padding:0 4px;border-radius:2px;color:#fff;letter-spacing:.4px}
.t-c{background:#2f7d4f}.t-o{background:#1d4f91}.t-r{background:#7a6a2f}.t-x{background:#6b3d6e}
.hero h2{font:800 22px/24px 'Noto Serif';letter-spacing:-.4px;max-height:48px;overflow:hidden}
.dek{font:500 11px/14px 'Noto Sans';color:#222;margin-top:2px;max-height:42px;overflow:hidden}
.src{font:500 8.5px/11px 'Noto Sans';color:#555;margin-top:1px}
.sec{font:900 11px/14px 'Noto Sans';letter-spacing:.8px;border-top:2px solid #111;margin-top:5px;padding-top:3px;
 display:flex;justify-content:space-between}
.sec i{font:italic 500 10px/14px 'Noto Serif';letter-spacing:0;color:#444}
.cards{display:grid;grid-template-columns:repeat(5,1fr);gap:5px 8px;margin-top:3px}
.card{border-top:1px solid #111;padding-top:3px}
.cart{position:relative;height:70px;overflow:hidden}
.cart svg{display:block;width:100%;height:70px}
.artlab{position:absolute;right:3px;bottom:3px;background:#111;color:#fff;font:900 13px/17px 'Noto Sans';padding:0 5px;border-radius:2px;letter-spacing:.2px;
 box-shadow:0 1px 2px rgba(0,0,0,.28)}
.artlab:empty,.hbig:empty{display:none}
.hbig{position:absolute;right:4px;top:4px;background:#c8102e;color:#fff;font:900 11px/14px 'Noto Sans';padding:2px 6px;border-radius:2px;text-align:right;
 box-shadow:0 1px 2px rgba(0,0,0,.28)}
.place{box-shadow:0 1px 2px rgba(0,0,0,.22)}
.card h3{font:800 13px/15px 'Noto Serif';max-height:30px;overflow:hidden}
.cdek{font:500 9.5px/12px 'Noto Sans';color:#333;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.card .kick{margin:2px 0 0;height:13px}
.card .lab{font-size:8.5px}
.bottom{display:flex;gap:12px;margin-top:5px}
.mapbox{width:352px;flex:none}
.legend{font:500 8.5px/12px 'Noto Sans';color:#333;margin-top:3px}
.legend .tag{margin-right:2px}
.index{flex:1;width:0}
.index ul{list-style:none;columns:2;column-gap:12px;font:500 10.4px/13.6px 'Noto Sans';color:#111;column-fill:auto;height:192px}
.index li{white-space:nowrap;overflow:hidden;display:flex;align-items:center;height:13.6px}
.index li.ch{font:900 8px/10px 'Noto Sans';letter-spacing:1px;height:11px;border-bottom:1px solid;margin-top:1px}
.index .n{display:inline-block;width:14px;height:14px;border-radius:50%;color:#fff;font:900 9px/14px 'Noto Sans';
 text-align:center;flex:none;margin-right:3px;letter-spacing:-.3px}
.index .flag{flex:none;margin-right:4px;display:block}
.index .pl{margin-right:3px}
.index .ti{margin-left:3px;flex:none}
.cleg{display:flex;flex-wrap:wrap;gap:2px 9px;font:700 8.5px/12px 'Noto Sans';color:#222;margin-top:3px}
.cleg span{display:flex;align-items:center}
.cleg i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:3px}
.index .pl{font-weight:800}
.ti{font:800 7px/10px 'Noto Sans';color:#fff;padding:0 2px;border-radius:2px;font-style:normal;vertical-align:1px}
.left{border:1.5px solid #c8102e;margin-top:7px;padding:4px 8px;font:500 10.5px/14px 'Noto Sans';color:#222}
.left b.h{color:#c8102e;font-weight:900;letter-spacing:.5px;margin-right:4px}
.left b{font-weight:800}
.foot{font:500 8px/11px 'Noto Sans';color:#555;margin-top:2px;display:flex;justify-content:space-between}
"""


def build():
    S = stories
    heroes = "".join(hero(i + 1, s) for i, s in enumerate(S.HEROES))
    cards = "".join(small(i + 4, s) for i, s in enumerate(S.CARDS))
    idx = index_list(S.INDEX, 14)
    utc = "".join(f'<span><b>{esc(t)}</b>{esc(w)}</span>' for t, w in S.UTC)
    regions = esc(S.REGION_BAR)
    nums = "".join(f'<div><b>{esc(a)}</b>{esc(b)}</div>' for a, b in S.NUMBERS)
    pins = [(i + 1,) + tuple(p) + ((0, 0) if len(p) == 3 else ()) for i, p in enumerate(S.PINS)]
    legend = "".join(f'{tag(t)}{esc(d)} &nbsp;' for t, d in S.LEGEND)
    page = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS.replace("GRAINURL", GRAIN)}</style></head><body><div class="page">
<div class="strap"><span>THE WORLD IN ONE DAY · FULL-DAY EDITION</span><span class="r">{esc(S.STRAP)}</span></div>
<div class="date">Tuesday 24 November 2026</div>
<div class="deck">{S.DECK}</div>
<div class="full">{esc(S.FULLDAY)}</div>
<div class="utc"><span class="h">THE DAY IN UTC</span>{utc}</div>
<div class="regions">{regions}</div>
<div class="nums"><div>THE DAY IN NUMBERS</div>{nums}</div>
<div class="heroes">{heroes}</div>
<div class="sec">TEN MORE FROM TUESDAY<i>{esc(S.CARDS_NOTE)}</i></div>
<div class="cards">{cards}</div>
<div class="sec">WHERE IT HAPPENED · ALSO ON TUESDAY 24 NOVEMBER<i>{esc(S.INDEX_NOTE)}</i></div>
<div class="bottom"><div class="mapbox">{world_map(pins)}<div class="cleg"><b>CONTINENTS</b>{cont_legend()}</div><div class="legend">{legend}</div></div>
<div class="index"><ul>{idx}</ul></div></div>
<div class="left"><b class="h">DATE CHECK · WHAT WE LEFT OUT</b>{S.LEFT_OUT}</div>
<div class="foot"><span>{esc(S.FOOT_L)}</span><span>{esc(S.FOOT_R)}</span></div>
</div></body></html>"""
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "page.html"), "w", encoding="utf-8") as f:
        f.write(page)
    total = len(S.HEROES) + len(S.CARDS) + len(S.INDEX)
    print("stories", total, "heroes", len(S.HEROES), "cards", len(S.CARDS), "index", len(S.INDEX), "pins", len(pins))
    # no two map pin labels may touch
    boxes = pin_boxes(pins)
    worst = min(((((a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5 - a[3] - b[3]), a[0], b[0])
                for i, a in enumerate(boxes) for b in boxes[i + 1:])
    print("closest pin pair %s-%s gap %.1f px" % (worst[1], worst[2], worst[0]))


if __name__ == "__main__":
    build()
