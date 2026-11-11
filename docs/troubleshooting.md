# Troubleshooting

## Open the serial console

Mac:

```
ls /dev/tty.usbmodem*
screen /dev/tty.usbmodemXXXX 115200
```

Ctrl-C stops the program. Ctrl-D reloads it. Ctrl-A, then K, then Y exits `screen`.

Mu, Thonny and [code.circuitpython.org](https://code.circuitpython.org) also work.

## What a good start looks like

```
I2C devices found: ['0x3c', '0x77']
23.4 C OK, 38 % LOW
```

Two addresses means both I2C devices are wired right.

## Problems we hit, and the fixes

| What you see | Cause | Fix |
| --- | --- | --- |
| Program stops at startup with an import error | A library missing from `lib` | Copy the repo's whole `lib` folder to the board. |
| `Incompatible .mpy file` | Board runs a different CircuitPython version than 10.x | Run circup. See `device/README.md`. |
| `OSError: No such file/directory: font5x8.bin` | Font file missing or inside `lib` | Put `font5x8.bin` at the top level, next to `code.py`. |
| `Sensor not found - check the cable and the address` | Cable loose, or sensor on another address | Reseat the cable. The code tries 0x77 and 0x76. |
| `OLED not found, continuing without it` | OLED cable loose | Reseat the cable from the sensor's free port. |
| Scan on the edge pads says "No pull up found" | Nothing is attached to that bus | Expected. We use the STEMMA QT bus. |
| Program fails with no message | Error before the console opened | Run it by hand in the REPL: `exec(open("/code.py").read())` |
| Light flickers at a limit | Reading hovers on the set point | Move the set point, or add hysteresis. |
| Temperature reads warm | Sensor near the board's heat | Set `TEMP_OFFSET_C`. Sensor reads 1.5 high → use -1.5. |
| Device dead on battery, fine on USB | Switch off, yellow wire not in the BAT block, or diode reversed | Check the switch, then that yellow is in the BAT block, then the diode stripe. |
| 5V line reads negative | Red and black swapped | Turn off and disconnect. Red goes in the 5V block, black in the GND block. |
| A light pipe is dark | Pipe not over its LED | Reseat it right over the LED. |
