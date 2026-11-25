"""Every story on the page, all dated Tuesday 24 November 2026 (see FACT_LEDGER.md beside the repo).

Numbering: 1-3 heroes, 4-13 picture cards, 14-35 index. Stories 1-13 are pinned on the map.
"big" is the label drawn inside each picture so the art says what happened without its headline.
"""

STRAP = "35 STORIES · 7 REGIONS · EVERY ONE DATED TUESDAY 24 NOVEMBER 2026"
DECK = ("Iran claims more Hormuz mine hits; US says lanes clear<b>·</b>"
        "Taiwan stocks soar 9%<b>·</b>Russian bombers spark Korean island alert<b>·</b>Dow tops 50,000")
FULLDAY = ("FULL DAY, TO MIDNIGHT EVERYWHERE: Wall Street's close · chess Game 1 result · CENTCOM's answer to Iran · "
           "CAS ruling on the AFCON title")
UTC = [("01:00", "Hanoi blast"), ("01:32", "Nepal M5.3"), ("02:30", "Colombia bomb"), ("05:30", "Taiex close"),
       ("05:30", "Sanofi deal"), ("11:14", "Ariane 6"), ("14:00", "Chess G1"), ("20:44", "CENTCOM denial"), ("21:00", "Dow 50,018")]
REGIONS = [("ASIA", 10, "#1d4f91", "ASIA 10 · EAST 5 · SOUTH-EAST 3 · SOUTH 2"), ("EUROPE", 7, "#2f5d7c"), ("AFRICA", 5, "#2f7d4f"), ("N. AMERICA", 4, "#6b3d6e"),
           ("LATIN AMERICA", 4, "#8a5a00"), ("MIDDLE EAST", 3, "#7a4a1e"), ("OCEANIA", 2, "#3b6b6b")]
NUMBERS = [("+8.99%", "Taiex: biggest point gain ever"), ("50,018", "Dow's first close above 50k"),
           ("$41bn", "Sanofi's cash bid for Insmed"), ("07:52", "Ulleung alert sounds, KST"),
           ("~175", "migrants missing off Senegal"), ("103.3", "US consumer confidence")]

HEROES = [
    dict(place="STRAIT OF HORMUZ", field="Middle East · war", tag="CLAIM", art="hormuz",
         big="NAVY: 2 TANKERS HIT<br>IRGC: ANOTHER HIT",
         head="Iran claims new tanker mine hits; US: lanes are clear",
         dek="Iran's navy says two tankers struck mines east of the strait and the IRGC says another hit one; "
             "CENTCOM rejects the claims. No ship named.",
         src="IRIB · Tasnim · Reuters · CENTCOM via National Security Journal"),
    dict(place="TAIPEI · SEOUL · TOKYO", field="East Asia · markets", tag="CONFIRMED", art="markets", big="",
         head="Taiwan's Taiex soars 9% as Asia's chip stocks rally",
         dek="Record 3,310-point gain to 40,122 with TSMC limit-up; Kospi +6.3% to 5,006 after a buy sidecar; "
             "Nikkei +3.9% to 58,645.",
         src="Focus Taiwan · Yonhap · Nikkei Indexes"),
    dict(place="ULLEUNG ISLAND, S. KOREA", field="East Asia · security", tag="OFFICIAL", art="ulleung", big="",
         head="Russian bombers spark Ulleung's first air-raid alert",
         dek="Shelter order 07:52-07:57 KST as Tu-160s and escorts fly through KADIZ; F-15Ks scramble; "
             "Seoul summons Russia's attaché.",
         src="JCS · Defence Ministry · JoongAng Daily · AJP"),
]

CARDS = [
    dict(place="Zaporizhzhia", tag="CONFIRMED", art="drones", big="73/96 DOWNED",
         head="Russian strike on city kills 2", dek="44 hurt; Kyiv says 73 of 96 drones shot down"),
    dict(place="Paris · New Jersey", tag="OFFICIAL", art="pill", big="$41BN",
         head="Sanofi to buy Insmed, $41bn", dek="$175 a share, all cash"),
    dict(place="Gaza City", tag="CONFIRMED", art="strike", big="7+ DEAD",
         head="Israeli strike kills Hamas security boss", dek="At least 7 dead across Gaza"),
    dict(place="New York", tag="CONFIRMED", art="up", big="DOW 50,018",
         head="Dow closes above 50,000 for first time", dek="Nasdaq -1.5%; Nvidia -5.9%"),
    dict(place="Baghdad", tag="OFFICIAL", art="oil", big="KURDISH OIL",
         head="Iraq orders takeover of Kurdish oilfields", dek="Erbil: \"in no way acceptable\""),
    dict(place="Hanoi", tag="CONFIRMED", art="fire", big="6 DEAD",
         head="Gas blast at hotpot eatery kills 6", dek="10 more in intensive care"),
    dict(place="Villavicencio", tag="CONFIRMED", art="blast", big="23 HURT",
         head="Car bomb at Colombian governor's office", dek="No deaths; went off 02:30 UTC"),
    dict(place="Alamata, Ethiopia", tag="OFFICIAL", art="report", big="14 KILLED",
         head="Amnesty: Tigray shelling may be war crimes", dek="14 civilian deaths verified"),
    dict(place="CAS · Senegal", tag="OFFICIAL", art="trophy", big="SENEGAL",
         head="Court hands AFCON title back to Senegal", dek="Morocco's 3-0 forfeit win set aside"),
    dict(place="Geneva", tag="CONFIRMED", art="chess", big="½-½ G1",
         head="World chess title opens with a draw", dek="Sindarov-Gukesh, 38 moves"),
]

# index 14-35, grouped by continent (colour = continent circle); code = flag drawn by flags.py
CONTINENTS = [("EUROPE", "#1E40AF"), ("AFRICA", "#D97706"), ("AMERICAS", "#B91C1C"),
              ("ASIA", "#047857"), ("OCEANIA", "#0F766E")]
INDEX = [
    dict(cont="EUROPE", code="UA", place="Uzhhorod", tag="OFFICIAL", head="Hungary's Magyar meets Zelensky"),
    dict(cont="EUROPE", code="FR", place="Versailles", tag="CONFIRMED", head="Nahel officer sent to murder trial"),
    dict(cont="EUROPE", code="EU", place="Brussels", tag="REPORTED", head="EU pact to move just 1,283 migrants"),
    dict(cont="EUROPE", code="SE", place="Stockholm", tag="CONFIRMED", head="PM vote on Kristersson set for 30 Nov"),
    dict(cont="AFRICA", code="SN", place="Dakar", tag="REPORTED", head="~175 missing on Europe-bound boat"),
    dict(cont="AFRICA", code="CD", place="DR Congo", tag="OFFICIAL", head="Gavi deal for 1.5M Ebola vaccine doses"),
    dict(cont="AFRICA", code="ZA", place="Gauteng", tag="OFFICIAL", head="Level 4 storm warning for Johannesburg"),
    dict(cont="AMERICAS", code="US", place="Washington", tag="REPORTED", head="US readies tariffs on 16 partners"),
    dict(cont="AMERICAS", code="US", place="New York", tag="OFFICIAL", head="Consumer confidence leaps to 103.3"),
    dict(cont="AMERICAS", code="US", place="Nasdaq", tag="CONFIRMED", head="Anthropic closes below $83 IPO price"),
    dict(cont="AMERICAS", code="CU", place="Havana", tag="OFFICIAL", head="WHO gives $2M, urges end to blockade"),
    dict(cont="AMERICAS", code="BR", place="Brasília", tag="REPORTED", head="Lula backs 2nd spending curb; real +2%"),
    dict(cont="AMERICAS", code="FR", place="Kourou", tag="OFFICIAL", head="Ariane 6 lofts 36 Amazon Leo satellites"),
    dict(cont="ASIA", code="NP", place="Taplejung", tag="CONFIRMED", head="M5.3 quake jolts east Nepal; no damage"),
    dict(cont="ASIA", code="CN", place="Jiuquan", tag="CONFIRMED", head="Pakistani named for China's station"),
    dict(cont="ASIA", code="SG", place="Singapore", tag="OFFICIAL", head="Q3 GDP +6.1%; 2026 outlook now ~6%"),
    dict(cont="ASIA", code="MY", place="Kuala Lumpur", tag="OFFICIAL", head="6,803 Myanmar nationals to go home"),
    dict(cont="ASIA", code="BD", place="Dhaka", tag="CONFIRMED", head="Hasina plans 16 Dec return; 'handcuffs'"),
    dict(cont="ASIA", code="KP", place="Pyongyang", tag="OFFICIAL", head="Kim Yo Jong threatens Swiss office"),
    dict(cont="ASIA", code="JP", place="Tokyo", tag="CONFIRMED", head="Takaichi orders 2nd extra budget"),
    dict(cont="OCEANIA", code="AU", place="Canberra", tag="CONFIRMED", head="Labor-Greens deal: 5% big-tech fines"),
    dict(cont="OCEANIA", code="AU", place="Canberra", tag="OFFICIAL", head="Visiting Singapore PM: no chip 'conduit'"),
]

# lon, lat for stories 1-13, with an optional label nudge (dx, dy) in map px
# real lon, lat for stories 1-13 + continent (pin colour), with an optional label nudge (dx, dy) in map px
PINS = [(56.4, 26.6, "ASIA", 9, 6), (121.5, 25.0, "ASIA", 6, 6), (130.9, 37.5, "ASIA", 9, -3),
        (35.1, 47.8, "EUROPE", 7, -9), (2.3, 48.9, "EUROPE", -10, -9), (34.4, 31.5, "ASIA", -10, 3),
        (-74.0, 40.7, "AMERICAS", 8, -6), (44.4, 33.3, "ASIA", 9, -7), (105.8, 21.0, "ASIA", -2, 9),
        (-73.6, 4.1, "AMERICAS", 5, 5), (39.6, 12.4, "AFRICA", 0, 0), (-16.2, 14.6, "AFRICA", 10, 2),
        (6.1, 46.2, "EUROPE", -11, 7)]
LEGEND = [("CONFIRMED", "2+ outlets or a final result"), ("OFFICIAL", "on the record"),
          ("REPORTED", "outlets citing sources"), ("CLAIM", "one side, unverified")]
CARDS_NOTE = "stories 1-13 are pinned on the map"
INDEX_NOTE = "14-35 · grouped by continent · hard news only · letters = tag"
LEFT_OUT = ("Nvidia reinstates Jensen Huang (Mon 23) · IRGC's first three-tanker claim (Mon 23 night) · "
            "US sanctions Iran's shadow banks (Mon 23) · Denmark school phone ban (Mon 23) · US states sue over Grok images (Mon 23) · "
            "Mediazona war-dead count (Mon 23) · Rutte's space-defence speech (Mon 23) · DR Congo plane lost (Sun 22) · "
            "Cikande factory fire (Sat 21) · Honda recall (Fri 20). "
            "<b>Not yet:</b> Shenzhou-24 launch (Wed 25 Beijing) · Australian Senate vote (Wed 25) · Swedish PM vote (30 Nov).")
FOOT_L = "Made after Tuesday ended in every time zone: closing prices, final results, late statements. Drawings are our own; no photographs."
FOOT_R = "Times UTC unless marked"
