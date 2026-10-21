English | [Română](PRINT.ro.md)

# Bar D1 – print and assembly guide

A 170 × 64 × 70 mm bar: Ø40 speaker | Puck | Ø40 speaker. No grille on the speakers (open cutouts). Powered through a DC jack on the back. Modelled for the Anycubic Kobra 2 Neo (PETG), but any printer with a bed of at least 180 × 80 mm works.

## Parts

| File | Qty | Purpose |
|---|---|---|
| `D1_01_corp.stl` | 1 | body with the 3 chambers |
| `D1_02_capac_spate.stl` | 1 | solid back cover with a hole for the DC jack |
| `D1_03_inel_difuzor_x2.stl` | **2** | rings that hold the speakers (the STL contains one ring; place it twice in the slicer) |

## Settings (PETG)

| Parameter | Value |
|---|---|
| Nozzle / layer | 0.4 mm / 0.2 mm |
| Walls | 3 (minimum) |
| Infill | 15–20 %, gyroid |
| Top/bottom layers | 4–5 |
| Nozzle / bed | 235–245 °C / 70–80 °C (follow your filament) |
| Fan | 30–50 % |
| Speed | 40–50 mm/s on outer walls |
| Adhesion | 3–5 mm brim on the body |

## Orientation
- **Body:** front face (the 45° chamfer) on the bed. The chamfered edge prints without supports.
- **Cover:** flat face on the bed, the plug facing up.
- **Rings:** flat on the bed.

Supports are normally not needed. In the slicer preview check the window for the USB-C port and buttons next to the Puck: if its ceiling shows as a long bridge or defects, add support only there (Top Z distance 0.2 mm).

## Parts to buy
- 2 speakers Ø40 mm × 20 mm, 3 W, 4 Ω
- ESP32-S3-Zero, MAX98357 amplifier (one per speaker), INMP441 microphone
- 1 panel DC jack: **a DC-022 is rated only ~0.5 A**, so for the Puck + ESP + two amplifiers choose a jack and a **5 V ≥ 3 A** power supply, with an inline fuse
- 8 M3 × 16 mm countersunk screws for the cover
- 4 rubber feet (Ø9.2 mm recesses on the bottom)
- small screws for the speaker rings (check the mounting ears of your speakers)
- silicone or sealing tape for the seam

## Assembly
1. Clean any PETG strings from the openings (Puck, speakers, screw holes) with a small file.
2. Dry fit **without glue**: Puck in the front tube, speakers in their seats.
3. Speakers: place each one in its seat and hold it with the ring and the small screws. Run the wires through the channel in the dividers (Ø5 mm).
4. The ESP and MAX boards sit in the recesses of the middle chamber; the microphone sits in the cup under the Ø1.6 mm hole on top.
5. DC jack into the Ø12 mm hole on the cover.
6. Seal the cover seam with silicone or sealing tape. The speaker chambers must be airtight (about 0.12 L each), or the bass drops.
7. Close the cover with the 8 M3 screws.

## To verify
The real speaker flange diameter and ear positions were estimated. Measure your speakers before printing the whole body: print the ring and a Ø40 test disc first to save time and filament.

Parameters are at the top of `bara.py`; run `python3 bara.py 0.4` to regenerate the STLs.
