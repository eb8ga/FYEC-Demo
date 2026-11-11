# Microcontroller

**Part:** Adafruit QT Py RP2040 (product 4900)

Role card: [02-microcontroller-and-code](../../docs/role-cards/02-microcontroller-and-code.md)

## Adafruit Learn guides

- [Adafruit QT Py RP2040 guide](https://learn.adafruit.com/adafruit-qt-py-2040)
- [Pinouts (5V pin, 3V pin, STEMMA QT)](https://learn.adafruit.com/adafruit-qt-py-2040/pinouts)
- [Downloads (schematic and fab print)](https://learn.adafruit.com/adafruit-qt-py-2040/downloads)
- [Built-in NeoPixel LED](https://learn.adafruit.com/adafruit-qt-py-2040/built-in-neopixel-led)

## Datasheets

- [RP2040 microcontroller chip datasheet (Raspberry Pi)](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- [AP2112 3.3 V LDO regulator datasheet (Diodes Inc.)](https://www.diodes.com/assets/Datasheets/AP2112.pdf)

## Design files

- [EagleCAD PCB files](https://github.com/adafruit/Adafruit-QT-Py-RP2040-PCB)
- [PrettyPins pinout PDF](https://github.com/adafruit/Adafruit-QT-Py-RP2040-PCB/blob/main/Adafruit%20QT%20Py%20RP2040%20Pinout.pdf)
- [3D model: STEP, Fusion, STL (this repo)](../../cad/adafruit/4900-qtpy-rp2040/)

## Note

The AP2112 is the regulator that turns the 5V line into 3.3 V. Its dropout is small at this board's low current, so the 3.4 to 3.9 V battery line still gives close to 3.3 V. Near empty, the output sags a little below 3.3 V.
