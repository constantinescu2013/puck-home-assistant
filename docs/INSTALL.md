English | [Română](INSTALL.ro.md)

# Installation

## What you need
- Home Assistant with the **ESPHome** add-on (or ESPHome on a PC)
- the Puck board and a USB-C data cable
- optional: Music Assistant (music and Favorites pages), an ESP32-CAM for the doorbell

## 1. Copy the files into ESPHome
From `esphome/` copy into `/config/esphome/` on Home Assistant:
- `puck-telecomanda.yaml`
- `puck_slot.yaml`
- `secrets.yaml` (created by you from `secrets.yaml.example`)

`secrets.yaml` needs `wifi_ssid`, `wifi_password` and the API key (`interfon_electra__encryption_key`). You can rename the key, but then change it in the YAML as well.

## 2. YAML settings
At the top of `puck-telecomanda.yaml`, in `substitutions`:

| Key | What to set |
|---|---|
| `name` | device name (lowercase, dashes) |
| `room_label` | room name shown at the top |
| `weather_entity` | weather entity in HA, e.g. `weather.forecast_acasa` |
| `ha_url` | HA address with port, e.g. `http://homeassistant.local:8123` or your IP |
| `art_entity` | the player whose album cover appears on the music page |

## 3. First install (USB)
1. Plug the board into your computer.
2. In ESPHome click **Install → Plug into this computer** (or use `https://web.esphome.io`).
3. Wait for the build (several minutes the first time) and the flash.
4. The board joins WiFi and shows up in Home Assistant as a new ESPHome device. Accept it (**Settings → Devices → Add**) using the API key from `secrets.yaml`.

Later updates: **Install → Wirelessly**.

## 4. Configure from Home Assistant
After first boot, on the device page set each slot (1–8): name, icon, type and the controlled entity. The values in the YAML are only defaults.

## 5. Automations
From `homeassistant/`: **Settings → Automations → Create → Edit in YAML**, then paste the content.

- `puck-sincronizare.yaml` – the Puck asks for entity states every 5 seconds and the automation sends them. Without it the pages show no states.
- `sonerie-automatizari.yaml` – optional, only if you have a doorbell camera. It takes a snapshot and sends it to the screen. Replace the camera and button entity names with yours.

The services are `esphome.puck_telecomanda_push_states` and `esphome.puck_telecomanda_doorbell`. If you change `name`, change them in the automations too (dashes become `_`).

## 6. Music
The music and Favorites pages need Music Assistant and a media player in HA (the example uses `media_player.dormitorul_principal_2`). Put it in `art_entity`.

## Troubleshooting
- **Pages without states:** the sync automation is missing or the device name does not match.
- **Build error:** copy the first line containing `error:` and search for it in the issues.
- **No album cover:** check `ha_url` (with `http://` and port).
- **Cannot join WiFi:** check `secrets.yaml`; the ESP32 only supports 2.4 GHz.
