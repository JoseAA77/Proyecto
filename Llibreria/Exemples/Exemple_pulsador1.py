from classe_LED import *
from classe_pulsador import *

led = LED(17, 5)
led2 = LED(27, 0)
pulsador = Pulsador(4, False)

try:
    while True:
        if pulsador.temps_pulsat(5):
            led.treu_intensitat()
            led2.aumenta_intensitat()
            time.sleep(0.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()