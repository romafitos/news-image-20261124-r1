# news-image-20261124-r1

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/romafitos/news-image-20261124-r1/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/romafitos/news-image-20261124-r1/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One front page for Tuesday 24 November 2026, put together only after that Tuesday had ended in every
time zone, so it can show how the day actually finished: Wall Street's close, the result of Game 1 of
the world chess championship, the court ruling on the Africa Cup of Nations title, and the US answer to
Iran's tanker-mine claims.

The page carries 35 stories from 7 regions and 20 fields, led by China's investigation of Shanghai's
party chief, the Brooklyn jury's verdict on Huawei and the drone strike on Riyadh's PIF Tower. The counts in
the strap and the region bar are computed from the story list itself. Each one happened, or was first reported, on Tuesday 24
November somewhere in the world, and each was checked against two separate sources. Stories that many
outlets were still running on Tuesday but that really belong to Monday or earlier (Nvidia bringing back
Jensen Huang, the first three-tanker claim, the Danish phone ban and others) are kept off the page and
listed in a small "date check" box with their true dates.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` uses only the Python standard library and needs no network. It checks that `entry.png` is a PNG
under 1 MiB and writes it to `$MAKEFUN_OUTPUT_DIR` (the grader's `/output` by default), byte for byte, so
two runs always give the same file.

## How the page is made

- `render/stories.py` holds every headline, number, tag and map pin. The fact ledger behind it (two
  sources and a true date for each story) was kept beside the repo while building.
- `render/art.py` draws every picture as plain SVG shapes written by hand: Shanghai's skyline under a
  magnifier, the Brooklyn courtroom with the twelve counts, the struck tower in Riyadh, and the small
  scenes on the ten cards (Ulleung's alert phone, the Taiex board, a burning tanker, the bus crash, the heat). There are
  no photographs, clip art or downloaded images.
- `render/worldshape.py` is a rough hand-placed outline of the continents for the pin map.
- `render/page.py` lays it all out as one 1024x1024 HTML page; `render/shoot.sh` screenshots it with
  headless Chromium and `render/pack.py` reduces the colours so the PNG stays near 190 KB.

Rebuild with `cd render && python3 page.py && bash shoot.sh`.

Tags on the page: CONFIRMED (two or more outlets, or a final result), OFFICIAL (on the record),
REPORTED (outlets citing sources) and CLAIM (one side's word, not verified).

---

<sub>Entered on [make.fun](https://make.fun/?ref=qeky27wz&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
