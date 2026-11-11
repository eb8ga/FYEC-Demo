# Sensor

**Part:** Adafruit BME688 on STEMMA QT (product 5046)

Role card: [01-sensor](../../docs/role-cards/01-sensor.md)

## Adafruit Learn guides

- [Adafruit BME680 / BME688 guide](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas)
- [BME688 board downloads (schematic, fab print)](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/downloads)
- [Introducing Adafruit STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt)
- [Working with I2C devices](https://learn.adafruit.com/working-with-i2c-devices)

## Datasheets

- [BME688 sensor datasheet (Bosch Sensortec)](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme688-ds000.pdf)

## Design files

- [BME688 board 3D model: STEP, Fusion, 3MF (this repo)](../../cad/adafruit/5046-bme688/)

## Library docs

- [CircuitPython BME680 library docs (works for BME688)](https://docs.circuitpython.org/projects/bme680/en/latest/)

## Note

The I2C address is 0x77. The datasheet's response-time specs help explain why breath moves humidity fast and temperature slowly.
