# CAD models

3D models of the boards inside the device. Use them to lay out the enclosure: check the vent, the display window, the light pipe holes and the USB-C opening against where the parts really sit.

| Part | Folder | Role | Source |
| --- | --- | --- | --- |
| QT Py RP2040 | [adafruit/4900-qtpy-rp2040](adafruit/4900-qtpy-rp2040) | Microcontroller + Code | [Adafruit_CAD_Parts](https://github.com/adafruit/Adafruit_CAD_Parts/tree/main/4900%20QTPy%20RP2040) |
| BME688 sensor | [adafruit/5046-bme688](adafruit/5046-bme688) | Sensor | [Adafruit_CAD_Parts](https://github.com/adafruit/Adafruit_CAD_Parts/tree/main/5046%20BME688%20Sensor) |
| Micro-Lipo USB-C charger | [adafruit/4410-micro-lipo-usbc](adafruit/4410-micro-lipo-usbc) | Power | [Adafruit_CAD_Parts](https://github.com/adafruit/Adafruit_CAD_Parts/tree/main/4410%20Micro%20Lipo%20USBC) |
| OLED module | `CAD/OLED_0.91_128x32.stp` inside the [OLED breakout KiCad zip](../subsystems/human-interaction/oled-breakout/91inOLED-BOB-KiCAD.zip) | Human Interaction | [GrabCAD, by RDusak](https://grabcad.com/library/oled-0-91-128x32-1) |
| Power board | [power-board](power-board) | Power | [KiCad project in this repo](../subsystems/power/power-board/chargingPowerConnection-KiCAD.zip) |
| Enclosure cover | [enclosure/cover.step](enclosure/cover.step) | Mechanical | Our design |
| Enclosure body | [enclosure/enclosure-v_01.step](enclosure/enclosure-v_01.step) | Mechanical | Our design |
| Light pipe, NeoPixel (25 mm) | [enclosure/lightMCU.step](enclosure/lightMCU.step) | Human Interaction | Our design |
| Light pipe, charger (38 mm) | [enclosure/lightCharge.step](enclosure/lightCharge.step) | Human Interaction | Our design |
| OLED breakout | [oled-breakout](oled-breakout) | Human Interaction | [KiCad project in this repo](../subsystems/human-interaction/oled-breakout/91inOLED-BOB-KiCAD.zip) |

Every model is in the repo so you can work offline. The source column links to where each one came from.

## Which file to open

| File | Use it in |
| --- | --- |
| `.step` | Any CAD program: Fusion, Onshape, SolidWorks, FreeCAD. Start here. |
| `.f3d` | Fusion only. Keeps Adafruit's original design history. |
| `.stl` / `.3mf` | Mesh only. Good for a quick look or a slicer, hard to measure from. |
| `.jpg` / `.gif` | Preview picture. |

Units are millimeters.

## Assembling

1. Import each board's `.step` file into one assembly.
2. Place the boards where they will sit in the case.
3. Draw the enclosure around them. Leave room for the cables and the battery.
4. Check every opening against the part it serves.

## Our own boards

The power board and the OLED breakout are KiCad designs. Their STEP files are full board assemblies exported from KiCad, with the terminal blocks, diode and connectors in place. The KiCad projects are archived as zip files in each subsystem folder.

## License

The OLED module model is from [GrabCAD](https://grabcad.com/library/oled-0-91-128x32-1), by RDusak, used under the GrabCAD Community terms.

The models in `adafruit/` are from [Adafruit_CAD_Parts](https://github.com/adafruit/Adafruit_CAD_Parts), © Adafruit Industries, MIT License. See [adafruit/LICENSE](adafruit/LICENSE).
