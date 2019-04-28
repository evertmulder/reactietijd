
Niets geselecteerd

Spring naar content
Mail van Familiemulder.eu gebruiken met schermlezers
Bureaubladmeldingen inschakelen voor Mail van Familiemulder.eu.   OK  Nee, bedankt
Conversaties
0,12 GB (0%) van 15 GB gebruikt
Beheren
Programmabeleid
Mogelijk gemaakt door Google
Laatste accountactiviteit: 24 minuten geleden
Details

import random
import datetime
import time
from getch import getch
import sys
from neopixel import *
import argparse
import RPi.GPIO as GPIO

# LED strip configuration:
LED_COUNT      = 33      # Number of LED pixels.
#LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN        = 18      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        led=strip.numPixels() -i 
        strip.setPixelColor(led -1, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def ledReactietijd(strip, score):
    lampjes_aan = score

    if lampjes_aan > strip.numPixels():
      lampjes_aan = strip.numPixels()

    wait_ms = 25

    # RGB https://www.rapidtables.com/web/color/RGB_Color.html
    for i in range(lampjes_aan):
        if i < 17:
           color = Color(255,0,0) #green
        elif i < 27:
           color = Color(255,255,0) # yellow
        else:
           color = Color(0,255,0) #red

        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def reactie_tijd():
    wacht_tijd = random.randint(1,8)

    time.sleep( wacht_tijd )
    led_aan_tijd = datetime.datetime.now()


    GPIO.output(22,GPIO.HIGH)
    time.sleep(.02)
    GPIO.output(22,GPIO.LOW)

    print('BEEEP LEDJE AAAN PIEPPPP')

    # wacht op een toets
    char = getch()
    knop_indruk_tijd= datetime.datetime.now()
    reactie_tijd = knop_indruk_tijd-led_aan_tijd

    ledjes_aan = int(reactie_tijd.total_seconds() / 0.05)
    print("Reactietijd: {}ms is {} leds".format(reactie_tijd.total_seconds() *1000, ledjes_aan))

    if ledjes_aan > 33:
        ledjes_aan = 33
        
    print("* " * ledjes_aan)
    ledReactietijd(strip, ledjes_aan)
    # slaap 1 sec
    time.sleep(1)
    # uit
    colorWipe(strip, Color(0, 0, 0))



# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
colorWipe(strip, Color(0, 0, 0))
print("Druk zo snel mogelijk op de spatiebalk wanneer je het signaal ziet ....")
while True:
    reactie_tijd()

reactietijd.py
reactietijd.py wordt weergegeven.
