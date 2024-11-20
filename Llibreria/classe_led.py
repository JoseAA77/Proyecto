import RPi.GPIO as GPIO
import time
from machine import Pin, PWM

class LED:
    def __init__(self, pin):
        """Constructor del Objeto"""
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(self.pin, GPIO.OUT) 
        self.state = False  
    
    def encen(self):
        """Encén el LED."""
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = True
        
    
    def apaga(self):
        """Apaga el LED."""
        GPIO.output(self.pin, GPIO.LOW)
        self.state = False
    

    def intensitat(self, intensitat):
        """Canvia l'intensitat del LED."""
        self.pwm = PWM(Pin(self.pin))
        self.pwm.freq(1000)

        self.pwm.duty_u16(intensitat)

    def parpelleig(self, temps):
        """Canvia l'intensitat del LED."""
        start_time = time.time()

        while True:
            self.alternar()
            time.sleep(1)
            if time.time() - start_time >= temps:
                break
       
    def alternar(self):
        """Canvia l'estat del LED."""
        if self.state:
            self.apaga()
        else:
            self.encen()
    
    def cleanup(self):
        """Neteja la configuració de GPIO."""
        GPIO.cleanup()