import RPi.GPIO as GPIO
import time
from classe_Buzzer_Passiu import Buzzer_Passiu
from classe_MQ2 import MQ2

# Configuración de pines GPIO
# Pines para sensores magnéticos
SENSOR_MAG_ventanas = 17  # Pines para los 3 sensores magnéticos en serie
SENSOR_MAG_puerta = 27  # Sensor magnético independiente

# Pines para sensores IR
SENSORES_IR = [22, 23, 24, 25]  # Pines GPIO para los 4 sensores IR

# Pin para el buzzer
BUZZER_PIN = 18

# Pin para el sensor MQ2
SENSOR_MQ2_PIN = 4

# Configuración inicial del buzzer
buzzer = Buzzer_Passiu(BUZZER_PIN)

# Configuración inicial del sensor MQ2
sensor_gas = MQ2(SENSOR_MQ2_PIN, platform="pi_3")

# Configuración inicial GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_MAG_ventanas, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SENSOR_MAG_puerta, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for sensor in SENSORES_IR:
    GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Función para verificar sensores
def verificar_sensores(modo):
    if modo == "perimetral":
        # Solo verifica sensores magnéticos
        if not GPIO.input(SENSOR_MAG_ventanas) or not GPIO.input(SENSOR_MAG_puerta):
            return True
    elif modo == "integral":
        # Verifica todos los sensores
        if not GPIO.input(SENSOR_MAG_ventanas) or not GPIO.input(SENSOR_MAG_puerta):
            return True
        for sensor in SENSORES_IR:
            if not GPIO.input(sensor):
                return True
    return False

# Función para monitorear el sensor de gas
def verificar_gas():
    if sensor_gas.detecta_particules():
        print("¡Gas detectado!")
        buzzer.melodia("alarma_gas")  # Reproduce la melodía de gas detectado

# Función principal de la alarma
def alarma(modo):
    print(f"Alarma activada en modo: {modo.upper()}")
    buzzer.melodia("to_armat")  # Reproducir tono de armado
    try:
        while True:
            verificar_gas()  # Monitorear el sensor de gas continuamente
            if verificar_sensores(modo):
                print("¡Alarma activada!")
                buzzer.melodia("alarma_intrusio")  # Reproducir tono de intrusión
                time.sleep(2)  # Pausa para evitar repeticiones constantes
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nDesactivando sistema...")
        buzzer.melodia("to_desarmat")  # Reproducir tono de desarmado
    finally:
        GPIO.cleanup()
        sensor_gas.cleanup()

# Selección del modo
print("Selecciona el modo de la alarma:")
print("1 - Perimetral (sensores magnéticos)")
print("2 - Integral (todos los sensores)")
modo = input("Ingresa el número del modo: ").strip()

if modo == "1":
    alarma("perimetral")
elif modo == "2":
    alarma("integral")
else:
    print("Modo inválido. Apagando sistema.")
