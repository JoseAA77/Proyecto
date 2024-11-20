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
        self.temps_anterior = time.time()
    
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

    def pampalluga(self, temps):
        """Canvia l'estat del LED cada X segoons, sen X la cuantitat introduida."""
        start_time = time.time()
        
        if start_time - self.temps_anterior >= temps:
            self.alternar()
            self.temps_anterior = start_time
       
    def alternar(self):
        """Canvia l'estat del LED."""
        if self.state:
            self.apaga()
        else:
            self.encen()
    
    def cleanup(self):
        """Neteja la configuració de GPIO."""
        GPIO.cleanup()