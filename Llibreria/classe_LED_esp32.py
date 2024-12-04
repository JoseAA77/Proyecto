from machine import Pin
import time

class LED:
    intensitats = [5, 15, 30, 50, 75, 100]
    
    def __init__(self, pin, intensitat, platform):
        """Constructor del Objeto"""
        self.pin = pin
        self.intensitat = intensitat
        self.platform = platform
        self.state = False
        self.temps_anterior = time.time()

        self.pin = Pin(self.pin, Pin.OUT)
        self.pwm = Pin.PWM(self.pin)  # Usamos PWM en la Raspberry Pi Pico
        self.pwm.freq(1000)  # Establecemos la frecuencia a 1kHz
        self.cambia_intensitat(self.intensitats[intensitat])  # Inicializa el PWM con la intensidad deseada

    def encen(self):
        """Enciende el LED."""
        self.cambia_intensitat(self.intensitats[self.intensitat])
        self.state = True

    def apaga(self):
        """Apaga el LED."""
        self.cambia_intensitat(0)
        self.state = False

    def cambia_intensitat(self, intensitat):
        """Cambia la intensidad del LED, el rango es de 0 a 100."""
        duty_value = int(intensitat * 655.35)
        self.pwm.duty(duty_value)

    def aumenta_intensitat(self):
        """Aumenta la intensidad del LED."""
        if self.intensitat < len(self.intensitats) - 1:
            self.intensitat += 1
            self.cambia_intensitat(self.intensitats[self.intensitat])

    def treu_intensitat(self):
        """Disminuye la intensidad del LED."""
        if self.intensitat > 0:
            self.intensitat -= 1
            self.cambia_intensitat(self.intensitats[self.intensitat])

    def pampalluga(self, temps):
        """Cambia el estado del LED cada X segundos, siendo X la cantidad introducida."""
        current_time = time.time()

        if current_time - self.temps_anterior >= temps:
            self.alterna()
            self.temps_anterior = current_time

    def alterna(self):
        """Cambia el estado del LED."""
        if self.state:
            self.apaga()
        else:
            self.encen()

    def cleanup(self):
        """Limpia la configuración de GPIO."""
        self.pwm.deinit()
