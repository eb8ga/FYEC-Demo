# Role card: Sensor

**Your part:** BME688 sensor board (the small board with two STEMMA QT plugs)

**In one sentence:** It measures the air around it and reports temperature and humidity when the microcontroller asks.

## Reference guide

- It measures four things: temperature, humidity, air pressure and gas. We use temperature and humidity only.
- It talks over I2C. That is two signal wires plus power and ground, all inside one plug-in cable.
- It has to touch open air. Sealed inside the box, it measures the box, not the room.

## Only you know

- Its I2C address is **0x77**. A few boards use 0x76. The code tries both.
- Humidity reacts to a breath in seconds. Temperature is slow. A warm hand works better than breath for temperature.
- It reads a little warm because it sits near the circuit board. The code has a setting for this: `TEMP_OFFSET_C`.
- Its two STEMMA QT ports are the same. One goes to the microcontroller. The other passes the bus on to the OLED screen.

## Interfaces

- **You give:** Temperature (°C) and humidity (%) to Microcontroller + Code.
- **You need:** Power and the I2C bus from Microcontroller + Code, through one cable. A spot at the vent from Mechanical. Tell Human Interaction which port is free.

## Your build task (Step 1)

With Microcontroller + Code: plug one end of a STEMMA QT cable into the sensor and the other end into the microcontroller's STEMMA QT port. The plug fits one way only. Do not force it.

## If something goes wrong

The console says `Sensor not found - check the cable and the address`: reseat both ends of the cable.

## Check yourself

Why might our device read 1 to 2 °C warmer than the thermostat on the wall?
