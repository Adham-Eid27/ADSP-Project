from tkinter import *
import serial
import time
import csv
import datetime

serialCom = serial.Serial('COM8', 9600)

# arduino sleep
serialCom.setDTR(False)
time.sleep(1)
serialCom.flushInput()
serialCom.setDTR(True)

# reading values
index = []

# csv
f = open("data.csv", "w", newline='')
f.truncate()

# window
window = Tk()
window.title("Digital design project")
window.geometry("1920x1080")

# grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)


def readserial():
    s_bytes = serialCom.readline()
    decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')
    print(decoded_bytes)

    index.append(decoded_bytes)
    if len(index) == 1:  # Temperature
        Label(window, text=index[0])
    elif len(index) == 2:  # Humidity
        Label(window, text=index[1])
    elif len(index) == 3:  # LPG
        Label(window, text=index[2])
    elif len(index) == 4:  # Air quality
        Label(window, text=index[3], font="30").place(x=200, y=350)
    elif len(index) == 5:  # RPM
        text = index[4]
        rpm = float(text)
        kmh = 0.0082938 * rpm
        kmh = int(kmh)
        index[4] = kmh
        Label(window, text=kmh, font="30").place(x=500, y=200)
    elif len(index) == 6:  # Humid
        Label(window, text=index[5], font="30").place(x=200, y=200)
    elif len(index) == 7:  # Temp
        Label(window, text=index[6], font="30").place(x=200, y=230)

    if len(index) == 7:
        now = datetime.datetime.now()
        index.append(now)
        writer = csv.writer(f, delimiter=",")
        writer.writerow(index)
        print("")
        print(index)
        index.clear()

    time.sleep(0.0001)

    Label(window, text="Temperature:", font="30").place(x=100, y=200)
    Label(window, text="Humidity:", font="30").place(x=100, y=230)
    Label(window, text="Air Quality:", font="30").place(x=100, y=350)
    Label(window, text="Wind Speed (KM/H)", font="30").place(x=350, y=200)



while True:
    window.update()
    readserial()


