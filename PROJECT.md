# MIB / TU-BA — Brownfieldy na fyzickom modeli Bratislavy

**Kontextový dokument projektu** (na zdieľanie do chatu / handoff). Zhŕňa zadanie, dáta, koncept, systém a výstupy.

---

## 0. Čo to je
Zadanie na **2. kolo výberového konania** na pozíciu **Dizajnér pre dáta a interaktívne technológie** v **Metropolitnom inštitúte Bratislavy (MIB)**. Termín: **pohovor v piatok**, výstup posielať najneskôr v deň pohovoru.

Hodnotia: **spôsob uvažovania nad témou, prácu s dátami, dizajnérsky prístup, návrh UX a schopnosť premýšľať nad fyzickým modelom mesta s projekciou ako interaktívnym nástrojom vo verejnom priestore.** Nehľadajú technicky dokonalé ani produkčne finálne riešenie — hľadajú koncept a uvažovanie.

## 1. Zadanie (zhrnuté)
Navrhnúť **koncept interaktívneho výstupu pre fyzický model Bratislavy v priestore TU-BA** na tému **brownfieldy — „Od nevyužitých území k živým štvrtiam".** Komunikovať tému zrozumiteľne, vizuálne a interaktívne cez: **fyzický model + projekciu na model, tablety, dotykovú obrazovku alebo web, a samotný priestor TU-BA.** Zamerať sa na brownfieldy — ich históriu, potenciál, obmedzenia a širšie vzťahy.

Zdroje dát: **MIB Koncepcia rozvoja brownfieldov 2026** (PDF) + **ArcGIS „Odvetvové štúdie – grafická časť" (UŠ Brownfields 2022)**; doplnkovo OpenStreetMap a otvorené dáta.

## 2. TU-BA — fakty
- Centrum architektúry a urbanizmu, **otvorené jeseň 2025**, roh **Štúrovej a Medenej**, ~329 m².
- **Verejný priestor pre dialóg a konsenzus o meste** — pre mesto, developerov, odborníkov aj bežnú verejnosť.
- Fyzický **model Bratislavy v mierke 1:3000** s interaktívnou projekciou; slúži ako **spoločný nástroj pre mnohé témy** (bývanie, zeleň, školstvo…). **Model sa ešte len dobudúva — fyzicky zatiaľ nestojí.**
- Náš uvažovaný model: **~18 m², 2 projektory zhora (edge-blend).**

## 3. Dáta a kľúčové čísla (so zdrojmi)
- **113 brownfieldov, spolu 580 ha** nevyužitého tkaniva (aktualizácia 2022).
- **~polovica v širšom centre** (~290–355 ha) → potenciál kompaktného mesta.
- **Vlastníctvo:** len **13 väčšinovo mestských** vs **56 súkromných** + 8 zmiešaných (zvyšok štát/iné).
- **Kontaminácia:** len 15 zo 113, ale **~75 % zamorenej plochy = jediný areál Istrochem** (Nové Mesto).
- **Tempo premeny:** ~13 lokalít / 16 ha ročne (podľa doterajšieho tempa) → premena je otázka **dekád**.
- Monitoring MIB od 2019. Rámec EÚ: **zero net land take do 2050**.
- Menné lokality: Istrochem, Filiálka, Zimný prístav, Mlynské Nivy (už premenené), Cvernovka, Gumon, Bajkalská 31, štadión Mierová kolónia, Matadorka.
- ArcGIS vrstvy: **Veľké areály (zóny/bloky)** · **Brownfieldy nad 0,5 ha** · **Významné brownfieldy** · **Environmentálne záťaže**.

## 4. Koncept — jadro
### Metafora
**„Brownfieldy sú tmavé miesta mesta. My ich rozsvecujeme."**
Maketa je stíchnuté, tmavšie mesto — **nesvieti celá**. Brownfieldy sú v nej tmavé, prehliadané rany. Projektor na ne (na dotyk) **posvieti farebným svetlom** → odhalí ich príbeh a to, čím môžu byť. Farba svetla = stav: **mŕtve (sivá) → v premene (jantár) → živé (zelená)**.

### Deľba médií (kľúčové dizajnérske rozhodnutie)
- **Model + projekcia = priestor a emócia** (kde to je, aké veľké, susedstvá, tma→svetlo, dnes→vízia, spojnice cez mesto).
- **Dotyková obrazovka / tablet = dáta a detail** (vlastníctvo, kontaminácia, čísla, časová os, karta lokality).
- Na maketu **nedávame text** (pri 1:3000 nečitateľný) — text žije na obrazovke.

### Publikum (rozhodnuté)
**Verejnosť + aktéri spolu.** Nie CAD/plánovač budov. Laik dostane emočný čitateľný príbeh, odborník/TU-BA dátovú hĺbku na dialóg a konsenzus.

### Prečo to má zmysel pre ľudí
Brownfieldy sú skrytá páka za vecami, ktoré ľudia cítia: **bývanie a ceny** (staviame na poliach, kým 580 ha leží v centre), **vlastná štvrť** (chátrajúci areál pri dome), **zdravie/voda** (kontaminácia), **verejné rozhodovanie** (kto vlastní, kto platí obnovu). Hook nie je „pozri, brownfieldy", ale **otázka: „Kde bude Bratislava rásť — a prečo 580 ha leží mŕtvych, kým staviame na poliach?"**

## 5. Systém — ako sa všetko prepája
**Fyzický model + projekcia = spoločné plátno** (v strede). Ostatné médiá sú vstupy/výstupy:
- **Dotyková obrazovka** — riadi, čo model rozsvieti; nesie hĺbku dát a insighty.
- **Tablet + AR** — osobná lupa nad modelom (vrstvy dát, budúca zástavba v rozšírenej realite). *Ambicióznejšia vrstva, smer, nie nutnosť pre v1.*
- **Web** — „odnes si lokalitu domov", zapoj sa aj po odchode.
- **Priestor TU-BA** — ambientný pulz láka dnu; model je stôl pre spoločný rozhovor.

Princíp: **svetlo na modeli = priestor a emócia; obrazovka a tablet = dáta a detail.**

## 6. Jeden model: režimy × vrstvy
Nie viaceré modely. Jeden model, dve osi:
### 3 režimy (ako sa model správa)
1. **Pulz** — v pokoji kladie otázku a jemne pulzuje; pozýva priblížiť sa.
2. **Objav** — dotyk vyberie lokalitu → projektor stlmí mesto a posvieti na ňu; detail na obrazovke.
3. **Vízia** — časová os Dnes→2050; mŕtve územia ožívajú (sivá→jantár→zelená) a rozsvietia sa spojnice; počítadlo oživených ha.

### Dátové vrstvy (čo model ukazuje, zapínateľné)
Brownfieldy nad 0,5 ha · Významné (najväčší dopad) · Environmentálne záťaže (kontaminovaná pôda, bodkovaná textúra) · Veľké areály (veľké transformačné celky) + stavový gradient mŕtve→živé.

## 7. Insighty
1. **„Nejde o to KDE stavať, ide o to KTO drží kľúč."** Len 13/113 je mestských → mesto väčšinu nevlastní, musí sa dohodnúť. Mení to otázku z „kde a čo" na „koho treba presvedčiť".
2. **„Nie všetky brownfieldy sú rovnaké."** Istrochem sám drží ~75 % zamorenia → treba rozlíšiť ľahko oživiteľné od ťažkých. Tempo ~13/rok → premena je beh na dekády.

## 8. Zážitok — 3 momenty (storyboard)
1. **Mesto dýcha** — maketa stlmená, pár miest jemne svieti a pulzuje.
2. **Ťukneš a rozsvieti sa** — na makete sa územie rozžiari, na obrazovke sa otvorí príbeh (minulosť · obmedzenia · potenciál · kto drží kľúč).
3. **Posunieš čas** — sivé rany menia farbu na zelenú a prepoja sa; vidíš, ako by mesto ožilo.

## 9. Argumentačná kostra decku (poradie slidov)
Titul → TU-BA (najprv nástroj, potom obsah) → Problém (580 ha) → **Prečo to má zmysel (pre koho/načo)** → Metafora → Storyboard (3 momenty) → Insight 1 (kto drží kľúč) → Insight 2 (nie sú rovnaké) → **Systém (prepojenie médií)** → **Štruktúra/sitemap (režimy × vrstvy)** → Réžia projekcie (3 režimy) → Dotyková obrazovka → Tablet + AR → Živý dôkaz (prototyp) → Škálovanie/záver.

## 10. Výstupy / súbory + ako spustiť
Priečinok: `C:\Users\samue\mib-brownfields\`
- **`deck.html`** — hlavná prezentácia (slidy, animácie, šípky ←→).
- **`design-system.html`** — systém znázornenia (farby, sémantika stavov, vrstvy, komponenty).
- **`prototype.html`** — funkčný interaktívny prototyp na 3D modeli mesta (3 režimy). *Vyžaduje server s HTTP Range (pmtiles).*
- **`data/brownfields.geojson`** — ilustračné lokality + reálne atribúty.
- **`data/buildings.pmtiles`** — 3D model budov BA (z projektu bratislava-3d, OSM/ODbL).
- **`serve_range.py`** — statický server s podporou Range.

**Spustenie:** v priečinku `python serve_range.py 8099`, potom:
- prezentácia: `http://localhost:8099/deck.html`
- prototyp: `http://localhost:8099/prototype.html`
- design system: `http://localhost:8099/design-system.html`

Deep-linky prototypu (na screenshoty): `?intro=0&mode=vizia&t=100`, `?intro=0&sel=istrochem`, `?proj=1`.
Deep-link decku na slide: `deck.html?s=7`.

Vizuálny jazyk (brand MIB): font **Overused Grotesk**, indigo **#30287B**, levanduľovo-biela **#eeedf4**; stavy: sivá `#8b88a3` / jantár `#f4b860` / zelená `#29b826`; pozornosť červená `#e4564f`, dáta modrá `#4ec5f9`.

## 11. Citlivá téma: Istrochem / vlastníctvo
Istrochem je vo vlastníctve **Agrofertu (A. Babiš)**, s obrovskou environmentálnou záťažou; beží spor, či má **štát zaplatiť sanáciu (350–700 mil. €)** Babišových pozemkov. Doložené (Pravda, Denník N, Bratislavské noviny, odpady-portal).
**Postoj v deliverable:** použiť ako **doložený fakt a emblém bariéry** („kto drží kľúč, čo blokuje"), **nie ako politické obvinenie**. Žiadne netvrdené celoštátne tézy. Politický kontext nechať na ústny rozhovor, artefakt držať triezvy a sourcnutý.

## 12. Otvorené / TODO
- Dokončiť sweep decku — doplniť 💡 vysvetlivky ku každému faktu/pojmu (rozpracované).
- Voliteľné: vygenerovať koncept-render náhľady (image generator) a vložiť do decku ako „ako to bude vyzerať".
- Voliteľné: doladiť vizuál prototypu (výška/sýtosť svetelných objemov, kamera).
- Réžia priestoru TU-BA je na predpokladoch (18 m², 2 projektory) — jasne označené.

## 13. Zdroje
- MIB Koncepcia rozvoja brownfieldov 2026 (mib.sk).
- ArcGIS „Odvetvové štúdie – grafická časť", UŠ Brownfields 2022.
- TU-BA: mib.sk, tuba.mib.sk.
- Istrochem/kontaminácia: Wikipédia, Pravda, Denník N, Bratislavské noviny, odpady-portal.sk.
- Model budov: OpenStreetMap (ODbL) cez projekt bratislava-3d.
