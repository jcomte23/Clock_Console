import time
import os

print()
print(" ___________________")
print("|                   |")
print("|   Clock Console   |")
print("|___________________|")
print()

try:
    hour = int(input("In 24 hour format what time of day is it? =>"))
    minutes = int(input("What minute of the day is it? =>"))

    if hour < 0 or hour > 23 or minutes < 0 or minutes > 59:
        print(" _________________________________________________")
        print("|                                                 |")
        print("|    / \\                                          |")
        print("|   / | \\     Hour or minute out of range.        |")
        print("|  /  *  \\                                        |")
        print("| /_______\\                                       |")
        print("|_________________________________________________|")
        print("")
        exit()

    while True:
        for horas in range(hour, 24):
            for minutes in range(minutes, 60):
                for seconds in range(60):
                    time.sleep(1)
                    os.system("clear")
                    print(f"Hora=> {horas:02d}:{minutes:02d}:{seconds:02d}")
            minutes = 0
        hour = 0
except ValueError as ve:
    print(" _________________________________________________")
    print("|                                                 |")
    print("|    / \\                                          |")
    print("|   / | \\    Invalid hour or minute entered.      |")
    print("|  /  *  \\                                        |")
    print("| /_______\\                                       |")
    print("|_________________________________________________|")
    print()
    print(f"ERROR => {ve}")
    print()

