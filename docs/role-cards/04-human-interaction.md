# Role card: Human Interaction

**Your part:** The screen, the color light, light pipes, and how people use the device

**In one sentence:** It decides how people use the device and what they need from it.

## Reference guide

- Start with the question: what environment are we trying to measure, and who needs to know about it?
- The answer drives what people see and touch: the screen, the lights, the shape of the case, where it sits, what data it keeps.

## Only you know

- The OLED's I2C address is **0x3C**. It must differ from the sensor's 0x77, or the board cannot tell them apart.
- The screen plugs into the sensor's second STEMMA QT port, not into the microcontroller.
- Two light pipes: one over the QT Py's NeoPixel, one over the charger's charge LED. Each sits in a 5 × 5 mm square hole in the cover, right over its LED. A pipe that misses its LED stays dark.
- On battery there is no laptop console. The screen and the lights are the only readout.

## Design question

What environment are you trying to measure? Who uses this device, where, and what do they need to know? Decide what goes on the screen, what goes on a light, what data is worth keeping, and what shape the device should be.

## Interfaces

- **You give:** The requirements: what people need to see, what data matters, where the device lives. Then the screen and lights themselves.
- **You need:** The sensor's free port from Sensor. Microcontroller + Code to draw the screen and keep the data. Mechanical to build the shape, window and light pipe holes.

## Your build task

Plug a STEMMA QT cable from the sensor's free port into the OLED. Seat the OLED behind the display window. Fit the light pipes into their holes over the LEDs.

## If something goes wrong

Screen blank: reseat the OLED cable. Light pipe dark: check it sits right over its LED.

## Check yourself

The device moves to a greenhouse. What would you change on the screen, and why?
