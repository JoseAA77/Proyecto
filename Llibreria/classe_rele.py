import RPi.GPIO as GPIO
import time

class Rele:
    def __init__(self, pin):
        """Constructor del Objeto"""
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(self.pin, GPIO.OUT) 
        self.state = False  
    
    def encendre(self):
        """Encén el Rele."""
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = True
        
    
    def apagar(self):
        """Apaga el Rele."""
        GPIO.output(self.pin, GPIO.LOW)
        self.state = False

 
    def cleanup(self):
        """Neteja la configuració de GPIO."""
        GPIO.cleanup()