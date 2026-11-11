# Device files

`CIRCUITPY/` is laid out exactly as it goes on the board. Copy everything inside it to the CIRCUITPY drive.

```
CIRCUITPY/
  code.py              the program
  font5x8.bin          the OLED font
  lib/
    adafruit_bme680.mpy
    adafruit_framebuf.mpy
    adafruit_ssd1306.mpy
    neopixel.mpy
    adafruit_bus_device/
      __init__.py
      i2c_device.mpy
      spi_device.mpy
```

## Libraries

From the Adafruit CircuitPython library bundle.

Built for **CircuitPython 10.x** (bundle release 20261110). To check which version your board runs, open `boot_out.txt` on the CIRCUITPY drive.

| Library | Used for | Version |
| --- | --- | --- |
| `adafruit_bme680.mpy` | The BME688 sensor | [3.7.16](https://github.com/adafruit/Adafruit_CircuitPython_BME680) |
| `adafruit_ssd1306.mpy` | The OLED screen | [2.12.24](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306) |
| `adafruit_framebuf.mpy` | Drawing text on the OLED, with `font5x8.bin` | [1.6.12](https://github.com/adafruit/Adafruit_CircuitPython_framebuf) |
| `adafruit_bus_device/` (folder) | I2C for the sensor and the OLED | [5.2.17](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice) |
| `neopixel.mpy` | The color light | [6.4.2](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel) |

## If your board runs a different CircuitPython version

`.mpy` files only work on the version they were built for. On another version the program stops with an `Incompatible .mpy file` error. Replace the libraries with circup, from this `device` folder:

```
pip install circup
circup install -r requirements.txt
```

circup reads the board's version and installs matching libraries.

## License

All five libraries are © Adafruit Industries, MIT License. Each library's repository, linked above, has its license.
