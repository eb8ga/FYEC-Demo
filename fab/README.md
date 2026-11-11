# Fabrication files

What you send to a fab house, a PCB mill or a 3D printer to make each part. 3D models are in [../cad](../cad). The KiCad source projects are in each subsystem folder.

| Part | Files | Source |
| --- | --- | --- |
| Power board | [power-board/chargingPowerConnection-GERBERS.zip](power-board/chargingPowerConnection-GERBERS.zip) | [subsystems/power/power-board](../subsystems/power/power-board/chargingPowerConnection-KiCAD.zip) |
| Enclosure | [enclosure/enclosure-v_01.3mf](enclosure/enclosure-v_01.3mf), [enclosure/cover.3mf](enclosure/cover.3mf) | [cad/enclosure](../cad/enclosure) |
| Light pipes | [enclosure/lightMCU.3mf](enclosure/lightMCU.3mf) (NeoPixel), [enclosure/lightCharge.3mf](enclosure/lightCharge.3mf) (charger) | [cad/enclosure](../cad/enclosure) |
| OLED breakout | [oled-breakout/91OLED-BOB-GERBERS.zip](oled-breakout/91OLED-BOB-GERBERS.zip) | [subsystems/human-interaction/oled-breakout](../subsystems/human-interaction/oled-breakout/91inOLED-BOB-KiCAD.zip) |

Each zip holds the Gerber layers, the drill files (`PTH`, `NPTH`) and the Gerber job file. For a fab house like JLCPCB, upload the zip as is. For a PCB mill, import the Gerber and drill files into the mill's software.

Power board: single-sided (front copper only). Prototype, cut on a PCB mill.

OLED breakout: 2-layer, 1.6 mm FR-4. Made by JLCPCB.

Enclosure: 3MF print files for the body (60 × 90 × 46 mm) and the cover. Open them in your slicer. Material: PLA. The light pipes are printed in PETG: 4.75 × 4.75 mm square, 25 mm long for the NeoPixel and 38 mm for the charger LED. They fit the 5 × 5 mm holes in the cover. Threaded inserts go in after printing. The boards mount with nylon M2.5 screws, and the cover closes with stainless steel M3 socket head cap screws (SHCS). Inserts: see [../safety/heat-set-insert-press](../safety/heat-set-insert-press/README.md).

When a part changes, add a new file with the version in its name (for example `-v2-GERBERS.zip`) instead of replacing the old one.
