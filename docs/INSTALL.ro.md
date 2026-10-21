[English](INSTALL.md) | Română

# Instalare

## Ce îți trebuie
- Home Assistant cu add-on-ul **ESPHome** (sau ESPHome instalat pe PC)
- placa Puck și un cablu USB-C de date
- opțional: Music Assistant (pentru muzică și Favorite), camera ESP32-CAM pentru sonerie

## 1. Fișierele în ESPHome
Copiază din `esphome/` în folderul `/config/esphome/` al Home Assistant:
- `puck-telecomanda.yaml`
- `puck_slot.yaml`
- `secrets.yaml` (creat de tine din `secrets.yaml.example`)

În `secrets.yaml` trebuie `wifi_ssid`, `wifi_password` și cheia API (`interfon_electra__encryption_key`; poți redenumi cheia, dar schimb-o la fel și în YAML).

## 2. Setările din YAML
La începutul `puck-telecomanda.yaml`, secțiunea `substitutions`:

| Cheie | Ce pui |
|---|---|
| `name` | numele dispozitivului (litere mici, cratime) |
| `room_label` | numele camerei afișat sus |
| `weather_entity` | entitatea de vreme din HA, ex. `weather.forecast_acasa` |
| `ha_url` | adresa HA cu port, ex. `http://homeassistant.local:8123` sau IP-ul tău |
| `art_entity` | playerul al cărui cover apare pe pagina de muzică |

## 3. Prima instalare (USB)
1. Conectează placa la calculator.
2. În ESPHome apasă **Install → Plug into this computer** (sau folosește `https://web.esphome.io`).
3. Așteaptă compilarea (prima dată durează câteva minute) și flashul.
4. Placa se conectează la WiFi și apare în Home Assistant ca dispozitiv ESPHome nou: acceptă-l (**Settings → Devices → Add**) cu cheia API din `secrets.yaml`.

Update-urile următoare se fac prin **Install → Wirelessly**.

## 4. Configurare din Home Assistant
După prima pornire, în pagina dispozitivului setezi pentru fiecare slot (1–8): nume, pictogramă, tip și entitatea controlată. Valorile din YAML sunt doar valori de start.

## 5. Automatizările
Din `homeassistant/`: **Settings → Automations → Create → Edit in YAML** și lipești conținutul.

- `puck-sincronizare.yaml` – Puck-ul cere la 5 secunde stările entităților, iar automatizarea i le trimite. Fără ea paginile nu arată starea.
- `sonerie-automatizari.yaml` – opțional, doar dacă ai camera soneriei. Face poza și o trimite pe ecran. Schimbă numele entităților de cameră și de buton cu ale tale.

Serviciile se numesc `esphome.puck_telecomanda_push_states` și `esphome.puck_telecomanda_doorbell`. Dacă schimbi `name`, schimbă-le și în automatizări (cratimele devin `_`).

## 6. Muzică
Pentru paginile de muzică și Favorite ai nevoie de Music Assistant și de un player în HA (în exemplu: `media_player.dormitorul_principal_2`). Pune-l la `art_entity`.

## Probleme frecvente
- **Pagini fără stări:** automatizarea de sincronizare nu e creată sau numele dispozitivului nu coincide.
- **Eroare la compilare:** copiază prima linie cu `error:` și caut-o în issues.
- **Nu apare coperta albumului:** verifică `ha_url` (cu `http://` și port).
- **Nu se conectează la WiFi:** verifică `secrets.yaml`; ESP32 folosește doar 2,4 GHz.
