# Subsystems

One folder per subsystem. Each has the Adafruit Learn guides, datasheets and design files for its parts. Microcontroller and Code have separate folders, but they are one role.

| Folder | Parts |
| --- | --- |
| [Sensor](sensor/README.md) | Adafruit BME688 on STEMMA QT (product 5046) |
| [Microcontroller](microcontroller/README.md) | Adafruit QT Py RP2040 (product 4900) |
| [Power](power/README.md) | 2000 mAh 3.7 V LiPo, Adafruit Micro-Lipo USB-C charger (product 4410), power board, slide switch |
| [Code](code/README.md) | code.py on the CIRCUITPY drive |
| [Human Interaction](human-interaction/README.md) | MakerFocus 0.91" 128x32 SSD1306 I2C OLED module on a custom STEMMA QT breakout board, the QT Py's NeoPixel, and two 3D-printed PETG light pipes |
| [Mechanical](mechanical/README.md) | 3D-printed case: body and cover, 60 × 90 × 46 mm |

## About the datasheets

The datasheets are linked, not stored here. Manufacturers hold the copyright, and links stay current when a datasheet is revised.
To keep local copies for offline use, run `tools/fetch-datasheets.sh`. It saves the PDFs into a `datasheets/` folder inside each subsystem. Those folders are ignored by git.
