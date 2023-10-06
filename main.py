import time
import os

hora=int(input("¿En formato de 24 horas que hora del dia es? =>"))
minuto=int(input("¿Que minuto del dia es? =>"))

while True:
    for horas in range(hora,24):
        for minutos in range(minuto,60):
            for segundos in range(60):
                time.sleep(1)
                os.system("cls")
                print(f"Hora: {horas:02d}:{minutos:02d}:{segundos:02d}")
        minuto=0
    hora=0