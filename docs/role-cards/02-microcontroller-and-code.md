# Role card: Microcontroller + Code

**Your part:** Adafruit QT Py RP2040, and `code.py` on the CIRCUITPY drive

**In one sentence:** The brain and its rules. It reads the sensor, decides LOW / OK / HIGH, and drives the screen and the color light, twice a second.

## Reference guide

- The board runs CircuitPython. When it gets power it runs `code.py` on its own.
- Each reading has a good range between a minimum and a maximum: the set points. Below is LOW, above is HIGH, in between is OK.
- One USB-C port programs it, powers it and charges the battery.

## Only you know

- The STEMMA QT connector is the I2C bus we use. The edge pads are a separate bus. Nothing goes there.
- Power comes in on the **5V** pin. The **3V** pin is an output only. Never connect power to it. Leave the back jumper open.
- Set points now: `TEMP_MIN_C = 20.0`, `TEMP_MAX_C = 26.0`, `HUM_MIN_PCT = 40.0`, `HUM_MAX_PCT = 60.0`.
- Light rule: GREEN both OK. BLUE something LOW, nothing HIGH. RED anything HIGH. HIGH wins.
- At startup the console prints the I2C scan. **0x3c** and **0x77** means the wiring is right.

## Interfaces

- **You give:** Power and the I2C bus to Sensor and Human Interaction. The LOW / OK / HIGH decision and the color.
- **You need:** The 5V line at the 5V block and ground at the GND block, from Power. Readings from Sensor. What to show and what data to keep, from Human Interaction.

## Your build task (Step 1, 2 and 5)

Step 1: take the sensor cable into the STEMMA QT port. Step 2: red wire from your 5V pin into the 5V block, black from your GND pin into the GND block. Step 5: plug in USB-C. Set the four set points for the application your team chose, and save. Then breathe on the sensor and watch the light.

## If something goes wrong

The light never changes: check that the file saved and the console shows new readings.

## Check yourself

Humidity is LOW and temperature is HIGH at the same time. What color is the light, and why?
