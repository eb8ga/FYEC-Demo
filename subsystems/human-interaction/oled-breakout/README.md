# 0.91" OLED SSD1306 STEMMA QT Breakout Board

A small breakout board (BoB) for common **0.91" 128×32 I²C OLED display modules**
based on the **SSD1306** controller.  
This board adapts the standard **1×4 2.54 mm OLED header** to a
**STEMMA QT / Qwiic–compatible JST‑SH 1.0 mm connector**, making these tiny OLEDs
easy to integrate into modern I²C-based projects.

---

## Features

- ✅ Designed for **0.91" 128×32 OLED modules**
- ✅ **SSD1306** controller (I²C mode)
- ✅ Breakout from **2.54 mm header → STEMMA QT (JST‑SH 1.0 mm)**
- ✅ Passive board (no regulators, no level shifting)
- ✅ Clear front & back silkscreen labeling
- ✅ 2‑layer PCB, 1.6 mm thickness
- ✅ Designed in **KiCad 9**
- ✅ Open hardware

---

## Tested Display Module

This breakout was tested with:

- **MakerFocus 0.91" I²C OLED Display Module**
- Resolution: **128×32**
- Controller: **SSD1306**
- Interface: **I²C**

Product link (for reference):  
https://www.makerfocus.com/products/2pcs-i2c-oled-display-module-0-91-inch-i2c-ssd1306-oled-display-module-1

Other 0.91" SSD1306 I²C modules with the same 1×4 pinout should also work.

---

## Electrical Interface

### OLED Header (J1 – 2.54 mm, Through‑Hole)

| Pin | Signal | Description |
|----:|--------|-------------|
| 1 | GND | Ground |
| 2 | VCC | Logic supply |
| 3 | SCL | I²C clock |
| 4 | SDA | I²C data |

The OLED module is intended to solder directly onto this header on the back side
of the display.

---

### STEMMA QT Connector (J2 – JST‑SH 1.0 mm)

STEMMA QT / Qwiic standard pin order:

| Pin | Signal |
|----:|--------|
| 1 | GND |
| 2 | VCC |
| 3 | SDA |
| 4 | SCL |

This allows direct connection to:
- Adafruit STEMMA QT boards
- SparkFun Qwiic boards
- Any JST‑SH I²C cable

---

## Power Notes ⚠️

- **No voltage regulation on this board**
- VCC is passed straight through from the STEMMA QT connector to the OLED module
- Most SSD1306 OLED modules use:
  - **VDD (logic): 1.65–3.3 V**
  - Internal charge pump to generate panel voltage

✅ Recommended:
- Power from **3.3 V**
- Ensure MCU I/O voltage matches OLED logic voltage

⚠️ Always verify your specific OLED module’s requirements.

---

## I²C Address

Typical SSD1306 I²C addresses:

- `0x3C` (most common)
- `0x3D` (depends on module configuration)

`code.py` uses `0x3C` (the `OLED_ADDRESS` setting in section 3). If your module answers at `0x3D`, the startup I²C scan shows it, and you change that one line.

---

## Mechanical

- Board designed to mount cleanly behind the OLED module
- Rounded corners
- Mounting holes included
- Board outline defined in `Edge.Cuts`

Silkscreen includes:
- Signal labels
- Orientation guidance
- Version and author marking

---

## Repository Contents

- `91inOLED-BOB-KiCAD.zip` – archived KiCad project: schematic, PCB layout, board outline (DXF), JST connector model and library
  - includes `OLED_0.91_128x32.stp`, the OLED module model by RDusak on [GrabCAD](https://grabcad.com/library/oled-0-91-128x32-1). Credit file alongside it in the zip.
- `../../../fab/oled-breakout/91OLED-BOB-GERBERS.zip` – fabrication outputs (Gerbers, drills)
- `../../../cad/oled-breakout/91inOLED-BOB-CAD.step` – 3D model of the assembled board
- OLED reference datasheet: [0.91" OLED module user manual (MC091GX)](https://www.lcdwiki.com/res/MC091GX/0.91inch_IIC_OLED_Module_MC091GX_User_Manual_EN.pdf)
- `README.md` – This file

---

## Fabrication Notes

- 2‑layer PCB
- 1.6 mm FR‑4
- ENIG or HASL finish acceptable
- No fine‑pitch or controlled‑impedance requirements

Key footprints:
- `PinHeader_1x04_P2.54mm_Vertical`
- `JST_SH_BM04B‑SRSS‑TB (1.0 mm)`

---

## Usage

Typical workflow:

1. Solder OLED module to J1
2. Plug JST‑SH cable into J2
3. Connect to MCU via STEMMA QT / Qwiic
4. Run [`code.py`](../../../device/CIRCUITPY/code.py). It drives the OLED with `adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)`. Text needs `adafruit_framebuf` in `lib` and `font5x8.bin` at the top of the CIRCUITPY drive. Both are in this repo.

If the OLED is unplugged or not found, `code.py` keeps running and prints `OLED not found, continuing without it`.

---

## Revision History

- **v0.3**
  - STEMMA QT support
  - Verified with MakerFocus 0.91" OLED
  - Improved silkscreen and labeling

---

## Author

**Eric Bredder**  
December 2025
