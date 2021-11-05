import time
import os

while True:
    os.system("cls")
    
    print("ADİTTİON")
    print("EXTRACTİON")
    print("MULTIPLICATION")
    print("DIVISION")

    x = int(input("Select Transaction..."))
    y = int(input("Select First Number..."))
    z = int(input("Select Second Number..."))

    if x == 1:
        print(y + z)
        time.sleep(2.0)

    if x == 2:
        print(y - z)
        time.sleep(2.0)

    if x == 3:
        print(y * z)
        time.sleep(2.0)

    if x == 4:
        print(y / z)
        time.sleep(2.0)