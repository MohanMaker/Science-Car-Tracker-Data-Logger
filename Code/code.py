# import libraries
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar

# setup internal dotstar LED
led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.5

# set up hall effect sensor
switch = DigitalInOut(board.D0)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# initialize variables
lastreading = 0
i = 1

# get start time
start = time.monotonic()

# find an availabe file name for storing readings
if i <= 25:
    filename = "/readings" + str(i) + ".txt"
    try:
        open(filename, "r")
    except:
        break
    i += 1
else:
    # create neopixel error if 25 files exist already (storage)
    led[0] = (255, 0, 0)
    time.sleep(10000)

while lastreading == 0:
    led[0] = (0, 255, 0)
    try:  # handles OS Errors
        with open(filename, "a") as fp:  # creates a file for writing data
            while True:  # forever loop
                timenow = time.monotonic()  # set time variable
                if timenow - start >= 10 and lastreading != 0:  # if no readings in more than ten seconds, and some readings have been made, then stop
                    led[0] = (0, 0, 255)
                    break  # stop
                if switch.value is False:  # if hall effect sensor is on/True
                    lastreading = time.monotonic()  # get the time now
                    if lastreading - start >= 0.06:  # only take a reading if the car is actually moving/hall effect sensor is not continuously triggered
                        led[0] = (255, 0, 0)
                        time.sleep(0.05)  # edit if double or skipped readings
                        led[0] = (0, 255, 0)
                        fp.write("{0:f}\n".format(lastreading))  # write reading to disk
                        fp.flush()  # make data write to disk
                        start = lastreading  # update start
    except OSError as e:  # handle errors
        delay = 0.5
        if e.args[0] == 28:
            led[0] = (255, 0, 0)
            delay = 0.25