# Human Interaction

**Part:** MakerFocus 0.91" 128x32 SSD1306 I2C OLED module on a custom STEMMA QT breakout board, the QT Py's NeoPixel, and two 3D-printed PETG light pipes

Role card: [04-human-interaction](../../docs/role-cards/04-human-interaction.md)

## Adafruit Learn guides

- [Introducing Adafruit STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt)
- [Adafruit NeoPixel Uberguide](https://learn.adafruit.com/adafruit-neopixel-uberguide)
- [QT Py RP2040: built-in NeoPixel](https://learn.adafruit.com/adafruit-qt-py-2040/built-in-neopixel-led)

## Datasheets

- [0.91" 128x32 OLED module user manual (MC091GX)](https://www.lcdwiki.com/res/MC091GX/0.91inch_IIC_OLED_Module_MC091GX_User_Manual_EN.pdf)
- [SSD1306 display controller chip datasheet](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/791/SSD1306-Datasheet-for-096-OLED-_2800_1_2900_.pdf)

## Design files

- [OLED breakout board README (this repo)](oled-breakout/README.md)
- [OLED breakout KiCad project, archived (this repo)](oled-breakout/91inOLED-BOB-KiCAD.zip)
- [Light pipes: print files, 3MF (this repo)](../../fab/enclosure/)
- [Light pipes: 3D models, STEP (this repo)](../../cad/enclosure/)
- [OLED breakout Gerbers for fabrication (this repo)](../../fab/oled-breakout/91OLED-BOB-GERBERS.zip)
- [OLED breakout 3D model: STEP (this repo)](../../cad/oled-breakout/91inOLED-BOB-CAD.step)
- [MakerFocus 0.91" OLED module (tested with the breakout)](https://www.makerfocus.com/products/2pcs-i2c-oled-display-module-0-91-inch-i2c-ssd1306-oled-display-module-1)

## Library docs

- [CircuitPython SSD1306 library docs](https://docs.circuitpython.org/projects/ssd1306/en/latest/)

## Note

Human Interaction covers how people use the device: the screen, the indicator lights, what data it keeps, its shape and where it lives. It starts with one question: what environment are we trying to measure? The breakout board adapts the module's pin header to a STEMMA QT connector, so the display plugs into the sensor's free port. The OLED uses I2C address 0x3C; the controller datasheet's I2C section shows where that comes from.
