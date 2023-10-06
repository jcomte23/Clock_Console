import time
import os
print()
print(" ___________________")
print("|                   |")
print("|   Clock Console   |")
print("|___________________|")
print()

try:
    hora=int(input("In 24 hour format what time of day is it? =>"))
    minuto=int(input("What minute of the day is it? =>"))

    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
        print("Hour or minute out of range.")
        exit()

    while True:
        for horas in range(hora,24):
            for minutos in range(minuto,60):
                for segundos in range(60):
                    time.sleep(1)
                    os.system("cls")
                    print(f"Hora: {horas:02d}:{minutos:02d}:{segundos:02d}")
            minuto=0
        hora=0
except:
    print("Invalid hour or minute entered.")
