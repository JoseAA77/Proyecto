import socket
import time
import os
from classe_WIFI_bidireccional_Pi_ESP32_20241201_2 import *


wifi = WIFI()

wifi.WIFI_reinicia()

envia = "Juanfri, espavila!! \n\nxDDDDDDDDDD"


try:
    while True:
        print(wifi.WIFI_comunicacio(envia))
except KeyboardInterrupt:
    print(f"Interromput per l'usiari")

