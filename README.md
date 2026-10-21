English | [Română](README.ro.md)

# Puck – Home Assistant remote (ESP32-S3, 1.28" round display)

A round touch-screen remote for Home Assistant, built on ESPHome. It has a voice assistant (Jarvis), clock, alarm, music control (Music Assistant) and a doorbell popup with a camera snapshot. The repo also contains the 3D-printable enclosures.

## Hardware

**The "Puck" board:** DeepSeek AI Voice Chat Robot BOX 1.28inch TouchScreen ESP32-S3 Development Board 1.28 inch Round LCD N16R8 for XiaoZhi (Spotpear). ESP32-S3 N16R8 (16 MB flash, 8 MB PSRAM), 240×240 round touch display, microphone and speaker.

**For the speaker bar (D1):** ESP32-S3-Zero, MAX98357 amplifier, INMP441 microphone, two Ø40 mm 3 W 4 Ω speakers, DC-022 power jack (see `3d/bara-d1/PRINT.md`).

## Repository layout

| Folder | Contents |
|---|---|
| `esphome/` | Puck firmware (`puck-telecomanda.yaml`, `puck_slot.yaml`, `secrets.yaml.example`) |
| `homeassistant/` | automations: state sync and doorbell |
| `3d/` | printable enclosures: `bara-d1`, `cutia-c2`, `ecran-dsi-pi4` (STL + parametric Python script) |
| `docs/` | `INSTALL.md` – step by step |

## Quick start

1. Read `docs/INSTALL.md`.
2. Copy `esphome/secrets.yaml.example` to `secrets.yaml` and fill in your values.
3. Flash over USB; later updates go over WiFi (OTA).

## Features

- 8 swipeable pages, one entity per page, colored ring around the edge (lights yellow, temperature blue to red)
- music page with album cover, volume and sleep timer
- Favorites page (3 radio stations + 1 Music Assistant playlist)
- alarm with gradual volume ramp-up
- analog watch face in standby, with outdoor temperature and weather
- doorbell popup with a camera snapshot (optional)
- automatic night dimming and a diagnostics page
- everything configurable from Home Assistant (name, icon, type and entity per slot)

Note: comments inside the YAML files are in Romanian.

## License

Pick one (for example MIT for code, CC BY 4.0 for the 3D models) and add a `LICENSE` file.
