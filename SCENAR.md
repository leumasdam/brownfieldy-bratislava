# Scenár prezentácie + obhajoba na pohovor
**Brownfieldy Bratislavy — interaktívny model pre TU-BA**

---

## 0. Pitch v 30 sekundách (ako otvoriť)
> „Bratislava nosí **113 brownfieldov, 580 hektárov** mŕtvej zeme — polovicu priamo v centre, a väčšinu ani nevnímame. Navrhol som, ako túto tému **rozsvietiť na fyzickom modeli v TU-BA**: model ukazuje **kde** to je a **v akom stave**, obrazovka **príbeh a dáta**, a spolu z toho spravia nástroj na verejný rozhovor o meste. A aby to nebolo len na papieri — celé to beží na **reálnych dátach MIB** ako živý prototyp.“

Drž sa jednej vety, ktorá to celé drží: **„Model svieti priestorom, obrazovka nesie dáta — a spolu ukážu, kde má mesto rásť a kto drží kľúč.“**

---

## 1. Scenár po slidoch (čo povedať)
1. **Titul** — kto som, čo ukážem: koncept interaktívneho výstupu pre model v TU-BA, téma brownfieldy.
2. **TU-BA** — „Najprv som pochopil, čím TU-BA je: verejný priestor pre dialóg, model 1:3000 pre mnohé témy. Brownfieldy sú prvá, ktorá ho rozsvieti.“
3. **Problém — 580 ha** — veľkosť problému, emočne. „Chodíme okolo a nevšímame si to.“
4. **Nápad (metafora)** — „Mesto spí, brownfieldy rozsvecujeme. Farba = stav, a ten čítam z dát.“
5. **Legenda** — ako sa to číta: farba+vzor = stav, tvar (logo/zámok) = vlastník, textúra = záťaž. „Navrhol som to tak, aby to čítal aj farboslepý.“
6. **Ako funguje projekcia** — dva projektory zhora premietajú priestor; text ostáva na obrazovke.
7. **Kto čo robí** — deľba médií: maketa svieti · obrazovka zadáva · tablet = osobná AR lupa · web = domov.
8. **Obrazovka** — „Ťuk na obrazovke rozsvieti to isté územie na modeli a otvorí kartu.“
9. **Detail** — životopis územia: minulosť → dnes → plán → vízia.
10. **Insight — kto drží kľúč** — najsilnejší moment: „Nejde o to *kde* stavať, ale *kto* to musí odklepnúť. Len 13 zo 113 je mestských.“
11. **V číslach** — 12 % drží mesto, 88 % zamknuté u iných; 33 % plochy zamorenej. „Toto je ten insight v hektároch.“
12. **Porovnanie** — Istrochem (spí) vs Filiálka a Gumon (prebúdzajú sa) — nie sú rovnaké.
13. **Vízia** — časová os Dnes → 2050; mŕtve ožívajú, mesto sa prepája.
14. **Ovládanie** — „Na model sa nesiaha; ovládaš od kraja, cez obrazovku či tablet. Aj z vozíka.“
15. **Informačná architektúra** — jedna appka, jeden spoločný stav.
16. **Technická architektúra** — obrazovka/tablet → web app → WebSocket → TouchDesigner → 2 projektory → model.
17. **Živý dôkaz** — „Model TU-BA sa ešte stavia, tak som ho odsimuloval. Toto beží na reálnych dátach z ich geoportálu.“ (spusti appku)
18. **Design system** — jeden vizuálny jazyk cez projekciu, obrazovku aj prezentáciu.
19. **Záver** — vzor sa dá použiť aj na bývanie, zeleň, školstvo. Poďakovanie.

---

## 2. Obhajoba — najčastejšie otázky komisie + odpovede

**„Ako určuješ, či územie spí / prebúdza sa / žije?“**
Z reálnych polí dát: *Má súčasné využitie?* → žije. *Má evidovaný zámer/plán?* → prebúdza sa. *Nič z toho?* → spí. Dnes 23 / 56 / 34. Priznávam, že tri stavy sú moja klasifikácia — polygóny, vlastníctvo aj záťaž sú oficiálne z MIB.

**„Aký je rozdiel medzi obrazovkou a tabletom?“**
Obrazovka je **spoločný ovládač** pri modeli — mení, čo vidia všetci. Tablet je **osobná AR lupa** — namieriš na maketu a vidíš navyše (budúca zástavba), nikomu nič nemeníš.

**„Čo znamená ‚kto drží kľúč‘?“**
Kto musí povedať áno, aby sa územie pohlo. Z 113 je len 13 mestských, 56 súkromných — mesto priamo drží len **12 % plochy**. Preto sa to roky nehýbe; problém nie je *kde*, ale *dohoda*.

**„Sú tie dáta správne?“**
Áno — stiahnuté 1:1 z oficiálnej vrstvy MIB (geoportal.bratislava.sk, UŠ Brownfieldy 2022). Overené: 113 území, 15 kontaminovaných, 13/56 vlastníctvo — sedí s verejnými číslami MIB.

**„Prečo TouchDesigner?“**
Je to štandard pre real-time projekčný mapping na fyzický objekt — kalibrácia z rohových bodov, edge-blend dvoch projektorov. Web appka len posiela príkazy (JSON cez WebSocket), TouchDesigner ich mapuje na maketu.

**„Ako sa to ovláda pri takom veľkom modeli (18 m²)?“**
Na model sa nesiaha — je to projekčná plocha a do stredu nedočiahneš. Ovládaš od kraja cez obrazovku/tablet; dá sa aj z vozíka.

**„Je to prístupné pre farbosleposť?“**
Áno — nespolieham sa len na farbu: stav má **vzor** (plná/šrafa/bodky) aj **tvar** (☾/↑/✿), vlastníctvo má **tvar** (logo/zámok), a na obrazovke je vždy aj **názov** textom.

**„Prečo spomínaš Istrochem, keď sa nepredáva?“**
Práve preto — je to **emblém bariéry**: najväčší kontaminovaný areál (138 ha), súkromný, bez zámeru, spor kto zaplatí sanáciu. Ukazuje, prečo brownfield roky leží. Nie príležitosť, ale výstraha.

**„Čo je reálne a čo koncept?“**
Reálne: dáta a živá appka na 3D modeli mesta. Koncept (jasne označený): réžia projekcie na fyzickej makete, tablet+AR, réžia priestoru (18 m², 2 projektory — predpoklady).

---

## 3. Čo úprimne priznať (posilní to dôveru)
- **Stav (spí/prebúdza/žije)** je moja odvodenina z dát MIB, nie ich oficiálny label.
- **Réžia priestoru** (rozmery, počet projektorov) je na rozumných predpokladoch — model TU-BA sa ešte len dobudúva.
- **Tablet + AR** je ambicióznejšia vrstva — smer, nie nutnosť pre prvú verziu.
- Poctivosť pri dátach a limitoch je súčasť dizajnu — nie slabina.

---

## 4. Súbory k výstupu
- `deck.html` — prezentácia (šípky ← →).
- `index.html` — živá appka (spusti `python serve_range.py 8099`, potom `localhost:8099/index.html`).
- `design-system.html` — vizuálny jazyk. · `PROJECT.md` — kontext. · `data/bf_real.geojson` — reálna vrstva MIB.
