# =============================================================================
#  Temperature & Humidity Set-Point Monitor
# =============================================================================
#  WHAT THIS PROGRAM DOES
#    1. Reads temperature and humidity from a BME688 sensor.
#    2. Compares each reading to a "good range" (the set points below).
#    3. Shows the result on the OLED screen and on the board's built-in
#       color light (called a NeoPixel):
#           GREEN = both readings are inside their range
#           BLUE  = something is too LOW  (and nothing is too high)
#           RED   = something is too HIGH
#
#  HARDWARE
#    Adafruit QT Py RP2040 board, BME688 sensor, 128x32 OLED display.
#
#  LANGUAGE
#    CircuitPython (a beginner-friendly version of Python for small boards).
#
#  FILES THAT MUST BE ON THE CIRCUITPY DRIVE
#    code.py        this file
#    font5x8.bin    the font the OLED uses to draw letters
#                   (top level of the drive, not inside lib)
#    lib/           folder of helper code: adafruit_bme680, adafruit_ssd1306,
#                   adafruit_framebuf, adafruit_bus_device, neopixel
# =============================================================================


# -----------------------------------------------------------------------------
#  1. IMPORTS
#     "import" loads code that someone else already wrote so we can use it.
# -----------------------------------------------------------------------------
import time                    # lets us pause the program (time.sleep)
import board                   # names for the pins and parts on our board
import neopixel                # controls the built-in color light
import adafruit_bme680         # talks to the BME688 sensor
import adafruit_ssd1306        # talks to the OLED display


# -----------------------------------------------------------------------------
#  2. SET POINTS  <-- THIS IS THE PART YOU EDIT
#     A set point is a limit we care about. Each reading gets a "good range"
#     between a minimum and a maximum. Outside that range = LOW or HIGH.
#     Names in CAPITAL LETTERS are settings: values we choose once and reuse.
# -----------------------------------------------------------------------------
TEMP_MIN_C = 20.0       # temperature below this is LOW   (degrees Celsius)
TEMP_MAX_C = 26.0       # temperature above this is HIGH  (degrees Celsius)

HUM_MIN_PCT = 40.0      # humidity below this is LOW      (percent)
HUM_MAX_PCT = 60.0      # humidity above this is HIGH     (percent)

# The sensor sits close to the warm circuit board, so it can read a little
# high. If a trusted thermometer disagrees, put the difference here.
# Example: sensor reads 1.5 too high -> use -1.5.
TEMP_OFFSET_C = 0.0

# How long to wait between readings (in seconds).
READ_INTERVAL_S = 0.5


# -----------------------------------------------------------------------------
#  3. OTHER SETTINGS (you normally do not need to change these)
# -----------------------------------------------------------------------------
# Every I2C device has an address, like a house number on a street.
OLED_ADDRESS = 0x3C                # address of the OLED display
SENSOR_ADDRESSES = (0x77, 0x76)    # the BME688 uses one of these two addresses

# Colors are (red, green, blue), each from 0 (off) to 255 (full).
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


# -----------------------------------------------------------------------------
#  4. CONNECT TO THE HARDWARE
# -----------------------------------------------------------------------------

# The sensor and the OLED talk to the board using "I2C": a two-wire connection
# that lets several devices share the same wires (called a "bus"). The board
# tells each device apart by its address.
# The small STEMMA QT connector on the QT Py is one I2C bus, so we use it.
try:
    i2c = board.STEMMA_I2C()
except AttributeError:
    i2c = board.I2C()          # fall back to the pins on the edge of the board

# Ask the bus "who is connected?" and print the addresses we find.
# Expect two: 0x3c (OLED) and 0x77 (sensor). Handy for troubleshooting!
while not i2c.try_lock():      # take control of the bus before using it
    pass
print("I2C devices found:", [hex(address) for address in i2c.scan()])
i2c.unlock()                   # give the bus back

# Connect to the sensor. We try each possible address until one works.
sensor = None
for address in SENSOR_ADDRESSES:
    try:
        sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=address)
        break                  # it worked, so stop trying
    except Exception:
        pass                   # it did not work, try the next address
if sensor is None:
    raise RuntimeError("Sensor not found - check the cable and the address")

# Connect to the OLED. If it is missing, the program still runs and sends
# its results to the serial console instead of stopping.
try:
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=OLED_ADDRESS)
except Exception as error:
    oled = None
    print("OLED not found, continuing without it:", error)

# Connect to the built-in color light. Brightness goes from 0 to 1.
# We use 0.2 because full brightness is very bright up close.
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)


# -----------------------------------------------------------------------------
#  5. FUNCTIONS
#     A function is a named, reusable piece of code. We "define" it here with
#     "def", then "call" it by name later in the main loop.
# -----------------------------------------------------------------------------

def classify(value, low, high):
    """Compare a reading to its range. Returns "LOW", "OK" or "HIGH"."""
    if value < low:
        return "LOW"
    elif value > high:
        return "HIGH"
    else:
        return "OK"


def show_on_oled(temp_c, humidity, temp_state, hum_state):
    """Draw four short lines of text on the OLED screen."""
    if oled is None:
        return                      # no display connected, nothing to do

    oled.fill(0)                    # clear the screen (0 = all pixels off)

    # oled.text(words, x, y, color): x and y are in pixels from the top-left.
    # Each line of text is 8 pixels tall, so the lines are at y = 0, 8, 16, 24.
    # In an f-string, {temp_c:4.1f} means "show temp_c as a number that is
    # 4 characters wide with 1 digit after the decimal point".
    oled.text(f"T {temp_c:4.1f}C {temp_state}", 0, 0, 1)
    oled.text(f" set {TEMP_MIN_C:.0f}-{TEMP_MAX_C:.0f}", 0, 8, 1)
    oled.text(f"H {humidity:3.0f}%  {hum_state}", 0, 16, 1)
    oled.text(f" set {HUM_MIN_PCT:.0f}-{HUM_MAX_PCT:.0f}", 0, 24, 1)

    oled.show()                     # send everything we drew to the screen


def update_light(temp_state, hum_state):
    """Set the color light. If both problems exist, HIGH wins over LOW."""
    if temp_state == "HIGH" or hum_state == "HIGH":
        pixel[0] = RED
    elif temp_state == "LOW" or hum_state == "LOW":
        pixel[0] = BLUE
    else:
        pixel[0] = GREEN                    # both readings are "OK"


# -----------------------------------------------------------------------------
#  6. MAIN LOOP
#     "while True" repeats forever: read, decide, display, wait, repeat.
# -----------------------------------------------------------------------------
while True:

    # Step 1: READ the sensor.
    # try/except means: "attempt this, and if it fails, do not crash."
    # If a reading fails, we wait and start the loop over.
    try:
        temp_c = sensor.temperature + TEMP_OFFSET_C
        humidity = sensor.relative_humidity
    except Exception as error:
        print("Sensor read error:", error)
        time.sleep(READ_INTERVAL_S)
        continue                            # skip to the next time around

    # Step 2: DECIDE. Is each reading LOW, OK or HIGH?
    temp_state = classify(temp_c, TEMP_MIN_C, TEMP_MAX_C)
    hum_state = classify(humidity, HUM_MIN_PCT, HUM_MAX_PCT)

    # Step 3: DISPLAY the result.
    show_on_oled(temp_c, humidity, temp_state, hum_state)
    update_light(temp_state, hum_state)
    print(f"{temp_c:.1f} C {temp_state}, {humidity:.0f} % {hum_state}")

    # Step 4: WAIT before reading again.
    time.sleep(READ_INTERVAL_S)


# -----------------------------------------------------------------------------
#  TRY THIS (extensions for after your device works)
#    1. Change the set points so the light turns red when you breathe on the
#       sensor. Which reading trips first, temperature or humidity? Why?
#    2. Change the colors so LOW is yellow (255, 150, 0) instead of blue.
#    3. Right now the light can flicker when a reading hovers at a limit.
#       How could you add a small "buffer" (called hysteresis) so it only
#       changes after the reading moves a little past the limit?
#    4. The BME688 can also measure air pressure (sensor.pressure). How would
#       you add a third set point and a third line on the display?
# -----------------------------------------------------------------------------
