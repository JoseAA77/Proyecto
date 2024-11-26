import RPi.GPIO as GPIO
import time

class SensorInfrarrojo:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  # Mode de numeració de pins com BCM
        GPIO.setup(self.pin, GPIO.IN)  # Configura el pin del PIR com a entrada

    def detecta_obstacle(self):
        """Retorna True si detecta un obstacle, False en cas contrari."""
        if GPIO.input(self.pin) == GPIO.LOW:
            return True
        else:
            return False

    def cleanup(self):
        """Neteja la configuració de GPIO."""
        GPIO.cleanup()