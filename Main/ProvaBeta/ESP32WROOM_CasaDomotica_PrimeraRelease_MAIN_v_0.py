'''
Arxiu anterior: 
    1-main_BetaPasaPas_20241208.py -> wifi funcions funcional
      main_WIFI_BetaPasaPas_20241208.py -> ni puta idea, crec q es el mateix
    1bis- canvi de nom de main_CasaDomotica_PrimeraRelease_v_0.py a main_ESP32WROOM_CasaDomotica_PrimeraRelease_v_1.py
    2- main_ESP32WROOM_CasaDomotica_PrimeraRelease_v_1.py -> res funciona, es refa de nou la classe (classe_WIFI_ESP32WROOM.py) i es procedeix a seguir en aquesta versió
    3- 
'''
'''
Accions en aquest ongoing:
    seguint feina de l'arxiu 2- amb la nova classe -> classe_WIFI_ESP32WROOM.py
'''
from machine import *
import ujson  # per a MicroPython
#import json # per a Python

from classe_WIFI_ESP32WROOM import *
from classe_Buzzer_Passiu_EPS32VROOM import *
from classe_MQ2_esp32 import *
from classe_pca9685_esp32 import *
from classe_pulsador_esp32 import *



                ###### Assignació PINs ######


                ###### Assignació variables ######
missatge_enviar = '{}'       
                
                ###### Creació de funcions ######
                
                ###### Creació objectes ######
COMs = WIFI()                
                
                ###### MAIN ######    


try:
    while True:
        missatge_enviar = str(time.time())
        print(missatge_enviar)
        print(COMs.WIFI_comunicacio(missatge_enviar))

        time.sleep(0.01)

except Exception as e:
    print(f"Error: {e}")






'''
Arxiu anterior: 
    1-main_BetaPasaPas_20241208.py -> wifi funcions funcional
    2-
    3- 
'''
'''
Accions en aquest ongoing:
    passant a classe
'''
'''

import network
import socket
import time

# Configura l'ESP32 com a punt d'accés
ssid = 'ESP32_AP'
password = '12345678'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password, authmode=network.AUTH_WPA_WPA2_PSK)

print("Punt d'accés actiu")
print("SSID:", ssid)
print("IP:", ap.ifconfig()[0])  # Mostra la IP del punt d'accés

# Configura el servidor TCP de l'ESP32
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.4.1', 12345))  # IP del punt d'accés i port
server_socket.listen(1)

print("Servidor TCP actiu a 192.168.4.1:12345")

# IP de la Raspberry Pi dins de la xarxa ESP32_AP
raspberry_ip = '192.168.4.2'
raspberry_port = 12346  # Port del servidor TCP de la Raspberry Pi

while True:
    try:
        # Com a servidor: escolta i rep missatges de la Raspberry Pi
        print("Esperant connexió de la Raspberry Pi...")

        # Estableix un temps d'espera manual per la connexió
        start_time = time.time()
        conn = None
        while (time.time() - start_time) < 10:  # Temps màxim d'espera: 10 segons
            try:
                conn, addr = server_socket.accept()
                break
            except OSError as e:
                pass  # Cap connexió encara

        if conn is None:
            print("Timeout esperant connexió.")
            continue

        print(f"Connexió establerta amb: {addr}")

        # Rep el missatge
        data = conn.recv(1024).decode('utf-8')
        print(f"Missatge rebut de la Raspberry Pi: {data}")

        conn.close()

        # Com a client: envia missatges a la Raspberry Pi
        print("Connectant com a client al servidor de la Raspberry Pi...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((raspberry_ip, raspberry_port))

        message = "Hola Raspberry"
        client_socket.send(message.encode('utf-8'))
        print(f"Missatge enviat a la Raspberry Pi: {message}")

        client_socket.close()

        time.sleep(1)  # Espera 5 segons abans del següent cicle

    except Exception as e:
        print(f"Error: {e}")
'''