import RPi.GPIO as GPIO
import time

class Buzzer:
    def __init__(self, buzzer_pin):
        self.buzzer_pin = buzzer_pin
        GPIO.setmode(GPIO.BCM)  # Mode de numeració de pins
        GPIO.setup(self.buzzer_pin, GPIO.OUT)  # Configura el pin del buzzer com a sortida

    def encendre(self):
        """Activa el buzzer (so)."""
        GPIO.output(self.buzzer_pin, GPIO.HIGH)
        

    def apagar(self):
        """Desactiva el buzzer (sense so)."""
        GPIO.output(self.buzzer_pin, GPIO.LOW)
       
    def sonar_durant(self, segons):
        """Fa sonar el buzzer durant un cert temps (en segons)."""
        self.encendre()
        time.sleep(segons)
        self.apagar()

    def cleanup(self):
        """Neteja la configuració de GPIO."""
        GPIO.cleanup()









#####################

        #### Exemple amb un Buzzer Passiu
 Un buzzer passiu necessita una freqüència específica. Amb aquest exemple es generen diferents
 sons.
    # Importa els mòduls necessaris
 import RPi.GPIO as GPIO
 import time
 GPIO.setmode(GPIO.BCM)
 BUZZER_PIN = 17
 GPIO.setup(BUZZER_PIN, GPIO.OUT)
    # Defineix una freqüència (en Hz) i la durada (en segons)
 pwm = GPIO.PWM(BUZZER_PIN, 440)  # Freqüència inicial de 440Hz
 pwm.start(50)  # Duty cycle al 50%
 try:
    pwm.ChangeFrequency(523)  # Nota Do
    time.sleep(0.5)
    pwm.ChangeFrequency(587)  # Nota Re
    time.sleep(0.5)
    pwm.ChangeFrequency(659)  # Nota Mi
    time.sleep(0.5)
    pwm.ChangeFrequency(698)  # Nota Fa
    time.sleep(0.5)
    pwm.stop()
 finally:
    GPIO.cleanup()
 ### Explicació- **GPIO.output**: s'usa per controlar el buzzer actiu amb un senyal de corrent contínua.- **GPIO.PWM**: permet generar senyals d'ona quadrada amb diferents freqüències, ideal per a
 buzzers passius.
