[English](PRINT.md) | Română

# Bara D1 – ghid de printare și montaj

Bară de 170 × 64 × 70 mm: difuzor Ø40 | Puck | difuzor Ø40. Fără grilă la difuzoare (deschidere liberă). Alimentare printr-o mufă DC pe spate. Testat în model pentru imprimanta Anycubic Kobra 2 Neo (PETG), dar merge pe orice imprimantă cu masă ≥ 180 × 80 mm.

## Piese

| Fișier | Bucăți | Rol |
|---|---|---|
| `D1_01_corp.stl` | 1 | corpul cu cele 3 camere |
| `D1_02_capac_spate.stl` | 1 | capac plin cu gaură pentru mufa DC |
| `D1_03_inel_difuzor_x2.stl` | **2** | inelele care țin difuzoarele (se printează 2 bucăți; STL-ul conține un inel, pune-l de două ori în slicer) |

## Setări (PETG)

| Parametru | Valoare |
|---|---|
| Duză / strat | 0,4 mm / 0,2 mm |
| Pereți | 3 (minim) |
| Umplere | 15–20 %, gyroid |
| Straturi sus/jos | 4–5 |
| Duză / masă | 235–245 °C / 70–80 °C (urmează filamentul tău) |
| Ventilator | 30–50 % |
| Viteză | 40–50 mm/s la pereții exteriori |
| Adeziune | brim 3–5 mm la corp |

## Orientare
- **Corp:** fața frontală (cu tăietura de 45°) pe masă. Muchia teșită se printează fără suporturi.
- **Capac:** fața plată pe masă, „dopul" în sus.
- **Inele:** plat, pe masă.

Suporturi: de regulă nu sunt necesare. Uită-te în previzualizarea slicerului la fereastra pentru USB-C și butoane de lângă Puck: dacă tavanul ei apare ca punte lungă sau cu defecte, pune suport doar acolo (Top Z distance 0,2 mm).

## Piese de cumpărat
- 2 difuzoare Ø40 mm × 20 mm, 3 W, 4 Ω
- ESP32-S3-Zero, MAX98357 (amplificator, câte unul pentru fiecare difuzor), microfon INMP441
- 1 mufă DC de panou: **DC-022 suportă doar ~0,5 A**, deci pentru Puck + ESP + 2 amplificatoare alege o mufă și un alimentator de **5 V ≥ 3 A**, cu siguranță în linie
- 8 șuruburi M3 × 16 mm cu cap înecat, pentru capac
- 4 piciorușe de cauciuc (locașuri Ø9,2 mm pe fund)
- șuruburi mici pentru inelele difuzoarelor (verifică urechile difuzoarelor tale)
- silicon sau bandă de etanșare pentru rost

## Montaj
1. Curăță cu o freză mică orice fir de PETG din orificii (Puck, difuzoare, găuri de șuruburi).
2. Probă **fără lipici**: Puck în tubul din față, difuzoarele în locașuri.
3. Difuzoarele: pune fiecare difuzor în locaș, ține-l cu inelul și șuruburile mici. Lipește firele pe canalul care trece prin pereții despărțitori (Ø5 mm).
4. Placile ESP și MAX intră în locașurile din camera centrală; microfonul stă în coșul de sub gaura Ø1,6 de sus.
5. Mufa DC în gaura Ø12 de pe capac.
6. Etanșează rostul capacului cu silicon sau bandă de etanșare: camerele difuzoarelor trebuie să fie închise (aprox. 0,12 L fiecare), altfel scade basul.
7. Închide capacul cu cele 8 șuruburi M3.

## De verificat
Diametrul real al flanșei difuzoarelor și poziția urechilor au fost estimate. Măsoară difuzoarele înainte să printezi corpul întreg: printează întâi inelul și un test cu un disc Ø40, ca să economisești timp și filament.

Parametrii se schimbă în `bara.py` (sus în fișier), apoi rulezi `python3 bara.py 0.4` ca să regenerezi STL-urile.
