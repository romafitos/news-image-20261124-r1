"""Every story on the page, all dated Tuesday 24 November 2026 (see FACT_LEDGER.md beside the repo).

Numbering: 1-3 heroes, 4-13 picture cards, 14-35 index. Stories 1-13 are pinned on the map.
"big" is the label drawn inside each picture so the art says what happened without its headline.
Each story carries its region (for the region bar) and its field (for the field count), so the
counts printed on the page are computed from the stories themselves, never typed by hand.
"""

# region keys: Asia is split East / South-East / South inside one Asia total
REGION_ORDER = [("ASIA", ("ASIA-E", "ASIA-SE", "ASIA-S")), ("EUROPE", ("EUROPE",)), ("MIDDLE EAST", ("MIDEAST",)),
                ("N. AMERICA", ("NAM",)), ("AFRICA", ("AFRICA",)), ("LATIN AMERICA", ("LATAM",)), ("OCEANIA", ("OCEANIA",))]

DECK = ("China probes Shanghai's party chief<b>·</b>US jury convicts Huawei<b>·</b>"
        "Drone hits Riyadh's tallest tower<b>·</b>Dow tops 50,000")
FULLDAY = ("FULL DAY, TO MIDNIGHT EVERYWHERE: Wall Street's close · Chess Game 1 result · CENTCOM's answer to Iran · "
           "CAS ruling on the AFCON title")
UTC = [("01:00", "Hanoi blast"), ("01:32", "Nepal M5.3"), ("02:30", "Colombia bomb"), ("05:30", "Taiex close"),
       ("05:30", "Sanofi deal"), ("11:14", "Ariane 6"), ("14:00", "Chess G1"), ("20:44", "CENTCOM denial"), ("21:00", "Dow 50,018")]
ULLEUNG_TIME = "07:52"
NUMBERS = [("10 of 12", "counts in the Huawei verdict"), ("11", "hurt at Riyadh's PIF Tower"),
           ("13", "dead in UAE bus crash"), ("5,258", "heat deaths in England"),
           ("+8.99%", "Taiex: biggest point gain ever"), (ULLEUNG_TIME, "Ulleung alert sounds, KST")]

HEROES = [
    dict(place="SHANGHAI · CHINA", field="East Asia · politics", region="ASIA-E", topic="politics",
         tag="OFFICIAL", art="shanghai", big="UNDER INVESTIGATION",
         head="China probes Shanghai party chief Chen Jining",
         dek="Xinhua: the Politburo member, 62, is suspected of \"serious violations\" of discipline and law, "
             "the fourth member of the top body probed since 2025.",
         src="Xinhua · CCDI · Reuters · WSJ · CNN"),
    dict(place="BROOKLYN · NEW YORK", field="N. America · courts", region="NAM", topic="courts",
         tag="CONFIRMED", art="huawei", big="GUILTY · 10 OF 12 COUNTS",
         head="US jury convicts Huawei on 10 of 12 counts",
         dek="Bank fraud, Iran sanctions and trade-secret theft; cleared of racketeering. "
             "Sentencing set for 14 Sept 2027; Huawei disputes the verdict.",
         src="US Justice Dept · Reuters · CNN"),
    dict(place="RIYADH · SAUDI ARABIA", field="Middle East · war", region="MIDEAST", topic="war",
         tag="OFFICIAL", art="riyadh", big="11 INJURED",
         head="Drone hits Riyadh's tallest tower for a second time",
         dek="Saudi civil defence: 11 hurt at the PIF Tower in the King Abdullah Financial District, "
             "five days after the first strike on it.",
         src="Saudi Civil Defence · SPA · WSJ · Reuters · Bloomberg"),
]

CARDS = [
    dict(place="Ulleung · S. Korea", region="ASIA-E", topic="security", tag="OFFICIAL", art="ulleung", big="07:52 KST",
         head="Russian bombers spark Ulleung air-raid alert", dek="Shelter order 07:52–07:57 KST; F-15Ks scramble"),
    dict(place="Taipei", region="ASIA-E", topic="markets", tag="CONFIRMED", art="markets", big="+8.99%",
         head="Taiwan's Taiex soars 9% as chip stocks rally", dek="Kospi +6.3%; Nikkei +3.9%"),
    dict(place="Strait of Hormuz", region="MIDEAST", topic="shipping", tag="CLAIM", art="hormuz", big="IRAN: MINE HITS",
         head="Iran claims new tanker mine hits; US: lanes clear", dek="CENTCOM rejects it; no ship named"),
    dict(place="Zaporizhzhia", region="EUROPE", topic="war", tag="CONFIRMED", art="drones", big="73/96 DOWNED",
         head="Russian strike on city kills 2", dek="44 hurt; Kyiv says 73 of 96 drones shot down"),
    dict(place="Gaza City", region="MIDEAST", topic="war", tag="CONFIRMED", art="strike", big="7+ DEAD",
         head="Israeli strike kills Hamas security boss", dek="At least 7 dead across Gaza"),
    dict(place="Paris · New Jersey", region="NAM", topic="business", tag="OFFICIAL", art="pill", big="$41BN",
         head="Sanofi to buy Insmed, $41bn", dek="$175 a share, all cash"),
    dict(place="New York", region="NAM", topic="markets", tag="CONFIRMED", art="up", big="DOW 50,018",
         head="Dow closes above 50,000 for first time", dek="Nasdaq -1.5%; Nvidia -5.9%"),
    dict(place="Ras Al Khaimah · UAE", region="MIDEAST", topic="transport", tag="OFFICIAL", art="bus", big="13 DEAD",
         head="Bus hits parked truck in Ras Al Khaimah", dek="41 aboard; 14 hurt, police say"),
    dict(place="England", region="EUROPE", topic="climate", tag="OFFICIAL", art="heat", big="5,258",
         head="England's summer heat deaths hit a record", dek="Old high 2,985 in 2022, says UKHSA"),
    dict(place="Dakar · Senegal", region="AFRICA", topic="sport", tag="OFFICIAL", art="trophy", big="SENEGAL",
         head="Court hands AFCON title back to Senegal", dek="Morocco's 3-0 forfeit win set aside"),
]

# index 14-35, grouped by region (colour = region circle); code = flag drawn by flags.py
CONTINENTS = [("EUROPE", "#1E40AF"), ("MIDDLE EAST", "#7B3F8C"), ("AFRICA", "#D9822B"), ("AMERICAS", "#B91C1C"),
              ("ASIA", "#2E7D5B"), ("OCEANIA", "#0F766E")]
INDEX = [
    dict(cont="EUROPE", region="EUROPE", topic="sport", code="CH", place="Geneva", tag="CONFIRMED",
         head="World chess title opens with a draw"),
    dict(cont="EUROPE", region="EUROPE", topic="diplomacy", code="UA", place="Uzhhorod", tag="OFFICIAL",
         head="Hungary's Magyar meets Zelensky"),
    dict(cont="EUROPE", region="EUROPE", topic="courts", code="FR", place="Versailles", tag="CONFIRMED",
         head="Nahel officer sent to murder trial"),
    dict(cont="EUROPE", region="EUROPE", topic="migration", code="EU", place="Brussels", tag="REPORTED",
         head="EU pact to relocate just 1,283 migrants"),
    dict(cont="MIDDLE EAST", region="MIDEAST", topic="energy", code="IQ", place="Baghdad", tag="OFFICIAL",
         head="Iraq orders takeover of Kurdish oilfields"),
    dict(cont="AFRICA", region="AFRICA", topic="rights", code="ET", place="Tigray", tag="OFFICIAL",
         head="Amnesty: shelling may be war crimes"),
    dict(cont="AFRICA", region="AFRICA", topic="migration", code="SN", place="Dakar", tag="REPORTED",
         head="~175 missing on Europe-bound boat"),
    dict(cont="AFRICA", region="AFRICA", topic="health", code="CD", place="DR Congo", tag="OFFICIAL",
         head="Gavi deal for 1.5M Ebola vaccine doses"),
    dict(cont="AMERICAS", region="LATAM", topic="crime", code="CO", place="Villavicencio", tag="CONFIRMED",
         head="Car bomb at governor's office"),
    dict(cont="AMERICAS", region="NAM", topic="economy", code="US", place="New York", tag="OFFICIAL",
         head="Consumer confidence leaps to 103.3"),
    dict(cont="AMERICAS", region="LATAM", topic="health", code="CU", place="Havana", tag="OFFICIAL",
         head="WHO gives $2M, urges end to blockade"),
    dict(cont="AMERICAS", region="LATAM", topic="economy", code="BR", place="Brasília", tag="REPORTED",
         head="Lula backs 2nd spending curb; real +2%"),
    dict(cont="AMERICAS", region="LATAM", topic="space", code="FR", place="Kourou", tag="OFFICIAL",
         head="Ariane 6 lofts 36 Amazon Leo satellites"),
    dict(cont="ASIA", region="ASIA-SE", topic="disaster", code="VN", place="Hanoi", tag="CONFIRMED",
         head="Gas blast at hotpot eatery kills 6"),
    dict(cont="ASIA", region="ASIA-S", topic="disaster", code="NP", place="Taplejung", tag="CONFIRMED",
         head="M5.3 quake jolts east Nepal; no damage"),
    dict(cont="ASIA", region="ASIA-E", topic="space", code="CN", place="Jiuquan", tag="CONFIRMED",
         head="Pakistani named to Shenzhou-24 crew"),
    dict(cont="ASIA", region="ASIA-SE", topic="economy", code="SG", place="Singapore", tag="OFFICIAL",
         head="Q3 GDP +6.1%; 2026 outlook now ~6%"),
    dict(cont="ASIA", region="ASIA-SE", topic="migration", code="MY", place="Kuala Lumpur", tag="OFFICIAL",
         head="6,803 Myanmar nationals to go home"),
    dict(cont="ASIA", region="ASIA-S", topic="politics", code="BD", place="Dhaka", tag="CONFIRMED",
         head="Hasina plans 16 Dec return; 'handcuffs'"),
    dict(cont="ASIA", region="ASIA-E", topic="diplomacy", code="KP", place="Pyongyang", tag="OFFICIAL",
         head="Kim Yo Jong threatens Swiss office"),
    dict(cont="OCEANIA", region="OCEANIA", topic="security", code="SB", place="Honiara", tag="REPORTED",
         head="Solomons to let China security pact lapse"),
    dict(cont="OCEANIA", region="OCEANIA", topic="tech", code="AU", place="Canberra", tag="CONFIRMED",
         head="Labor-Greens deal: 5% big-tech fines"),
]

ALL = HEROES + CARDS + INDEX
N_STORIES = len(ALL)
N_FIELDS = len({s["topic"] for s in ALL})


def region_count(keys):
    return sum(1 for s in ALL if s["region"] in keys)


def _region_bar():
    parts = []
    for name, keys in REGION_ORDER:
        n = region_count(keys)
        if name == "ASIA":
            e, se, so = (region_count((k,)) for k in keys)
            parts.append(f"ASIA {n} (East {e}, South-East {se}, South {so})")
        else:
            parts.append(f"{name} {n}")
    return " · ".join(parts)


REGION_BAR = _region_bar()
N_REGIONS = len(REGION_ORDER)
STRAP = (f"{N_STORIES} STORIES · {N_REGIONS} REGIONS · {N_FIELDS} FIELDS · "
         f"ALL HAPPENED OR FIRST REPORTED TUESDAY 24 NOVEMBER 2026")

# real lon, lat for stories 1-13 + map colour group, with an optional label nudge (dx, dy) in map px
# #9 sits on Insmed's home, Bridgewater NJ; #2 Brooklyn and #10 Wall Street share New York, so labels fan out
PINS = [(121.5, 31.2, "ASIA", -10, -4), (-73.9, 40.7, "AMERICAS", -2, -12), (46.7, 24.7, "MIDDLE EAST", -2, 10),
        (130.9, 37.5, "ASIA", 9, -4), (121.5, 25.0, "ASIA", 8, 6), (56.4, 26.6, "MIDDLE EAST", 10, -6),
        (35.1, 47.8, "EUROPE", 7, -8), (34.4, 31.5, "MIDDLE EAST", -11, 3), (-74.6, 40.6, "AMERICAS", -13, 4),
        (-74.0, 40.7, "AMERICAS", 12, 2), (55.9, 25.6, "MIDDLE EAST", 12, 7), (-0.1, 51.5, "EUROPE", -10, -6),
        (-17.4, 14.7, "AFRICA", -6, 9)]
# pins in the crowded clusters are drawn a little smaller
DENSE = {2, 3, 6, 7, 8, 9, 10, 11}
LEGEND = [("CONFIRMED", "2+ outlets or a final result"), ("OFFICIAL", "on the record"),
          ("REPORTED", "outlets citing sources"), ("CLAIM", "one side, unverified")]
CARDS_NOTE = "stories 1-13 are pinned on the map"
INDEX_NOTE = "14-35 · grouped by region · letters = tag"
LEFT_OUT = ("Nvidia reinstates Jensen Huang (Mon 23) · IRGC's first three-tanker claim (Mon 23 night) · "
            "first drone strike on the PIF Tower (Thu 19) · Houthi claim for Tuesday's strike (Wed 25) · US sanctions Iran's shadow banks (Mon 23) · "
            "DR Congo plane lost (Sun 22) · Cikande factory fire (Sat 21). "
            "<b>Not yet:</b> Shenzhou-24 launch (Wed 25 Beijing) · Australia–Solomons treaty signing (Wed 25).")
FOOT_L = ("Every story happened or was first reported on Tuesday 24 November 2026 · made after the day ended everywhere · "
          "drawings our own, no photographs")
FOOT_R = "Times UTC unless marked"
