import RPi.GPIO as GPIO
import time

class Pulsador:
    def __init__(self, pin, state):
        """Constructor del Objeto"""
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(self.pin, GPIO.IN)

        self.state = False  

    def detecta_pulsacio(self):
        """Retorna True si detecta pulsacio, False en cas contrari."""
        if GPIO.input(self.pin) == GPIO.HIGH:
            return True
        else:
            return False
        
    def mesura_pulsacio(self):
        """Mesura el temps de pulsacio."""
        temps = 0
        while self.detecta_pulsacio() == GPIO.HIGH:
            temps += 1
            time.sleep(1)
        
        return temps

 
    def cleanup(self):
        """Neteja la configuració de GPIO."""
        GPIO.cleanup()