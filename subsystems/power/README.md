# Power

**Part:** 2000 mAh 3.7 V LiPo, Adafruit Micro-Lipo USB-C charger (product 4410), power board, slide switch

Role card: [03-power](../../docs/role-cards/03-power.md)

## Adafruit Learn guides

- [Adafruit MicroLipo and MiniLipo chargers guide (see Charge Rate and Changing the Rate)](https://learn.adafruit.com/adafruit-microlipo-and-minilipo-battery-chargers)
- [Charger downloads (schematic, fab print)](https://learn.adafruit.com/adafruit-microlipo-and-minilipo-battery-chargers/downloads)
- [Li-Ion and LiPoly batteries (care and safety)](https://learn.adafruit.com/li-ion-and-lipoly-batteries)
- [QT Py RP2040 pinouts: power section](https://learn.adafruit.com/adafruit-qt-py-2040/pinouts)

## Datasheets

- [LiPo battery, 2000 mAh 3.7 V, datasheet (Adafruit)](https://cdn-shop.adafruit.com/datasheets/LiIon2000mAh37V.pdf)
- [MCP73831 charger chip datasheet (Microchip)](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP73831-Family-Data-Sheet-DS20001984H.pdf)
- [1N5818 diode datasheet (STMicroelectronics)](https://www.st.com/content/ccc/resource/technical/document/datasheet/26/db/14/60/52/47/47/5b/CD00001625.pdf/files/CD00001625.pdf/jcr:content/translations/en.CD00001625.pdf)

## Design files

- [Charger EagleCAD files](https://github.com/adafruit/Adafruit-MicroLipo-PCB)
- [Charger 3D model: STEP, Fusion, STL (this repo)](../../cad/adafruit/4410-micro-lipo-usbc/)
- [Power board KiCad project, archived (this repo)](power-board/chargingPowerConnection-KiCAD.zip)
- [Power board Gerbers for fabrication (this repo)](../../fab/power-board/chargingPowerConnection-GERBERS.zip)
- [Power board 3D model: STEP (this repo)](../../cad/power-board/chargingPowerConnection-CAD.step)
- [Power board schematic, picture (this repo)](power-board/power-board-schematic.png)
- [Power board 3D view, picture (this repo)](power-board/power-board-3d.png)

## Note

The numbers that matter for the 1N5818 are its forward drop (about 0.3 V at this current) and its 30 V reverse rating. The MCP73831 sets its charge current with one resistor on its PROG pin: 10 kΩ gives 100 mA, 2 kΩ gives about 500 mA. The charger's rate jumper switches between them. Design question for the team: which rate, and why? Use the charger and battery datasheets.
