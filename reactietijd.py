
import random
import datetime
import time
from getch import getch, pause
import sys



def reactie_tijd():
    wacht_tijd = random.randint(3,12)

    time.sleep( wacht_tijd )
    led_aan_tijd = datetime.datetime.now()

    # maak een beeo geluidje
    sys.stdout.write('\a')
    sys.stdout.flush()

    # wacht op een toets
    pause('BEEEP LEDJE AAAN PIEPPPP')
    knop_indruk_tijd= datetime.datetime.now()
    reactie_tijd = knop_indruk_tijd-led_aan_tijd
    ## Alle ledjes 3.3 sec
    ## 3.3 / 33 = 0.1 sec per led

    ledjes_aan = int(reactie_tijd.total_seconds() / 0.1)
    print("Reactietijd: {}ms is {} leds".format(reactie_tijd.total_seconds() *1000, ledjes_aan))

    if ledjes_aan > 33:
        ledjes_aan = 33
        
    print("* " * ledjes_aan)



print("Druk zo snel mogelijk op de spatiebalk wanneer je het signaal ziet ....")
while True:
    reactie_tijd()
