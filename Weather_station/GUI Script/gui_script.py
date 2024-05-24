from tkinter import *
import serial
import time

serialCom = serial.Serial('COM8', 9600)

# arduino sleep
serialCom.setDTR(False)
time.sleep(1)
serialCom.flushInput()
serialCom.setDTR(True)

# reading values
index = []


def readserial():
    s_bytes = serialCom.readline()
    decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')
    print(decoded_bytes)

    index.append(decoded_bytes)
    if len(index) == 1:  # Temperature
        Label(window, text=index[0]).place(x=0, y=0)
    elif len(index) == 2:  # Humidity
        Label(window, text=index[1]).place(x=0, y=0)
    elif len(index) == 3:  # LPG
        Label(window, text=index[2]).place(x=0, y=0)
    elif len(index) == 4:  # Air quality
        Label(window, text=index[3]).place(x=500, y=250)
    elif len(index) == 5:  # RPM
        Label(window, text=index[4]).place(x=500, y=300)
    elif len(index) == 6:  # HUmid
        Label(window, text=index[5]).place(x=500, y=350)
    elif len(index) == 7:  # Temp
        Label(window, text=index[6]).place(x=500, y=400)

    if len(index) == 7:
        print("")
        index.clear()

    time.sleep(0.0001)


window = Tk()
window.title("Digital design project")
window.geometry("1920x1080")

Label(window, text="Temperature:").place(x=150, y=10)
Label(window, text="Humidity:").place(x=150, y=60)
Label(window, text="Moisture:").place(x=150, y=110)
Label(window, text="FAN ON/OFF").place(x=400, y=60)
Label(window, text="PUMP ON/OFF").place(x=400, y=110)

fr = Frame(window).place(x=150, y=10)

lbl = Label(window, text=("Temperature:"))

while True:
    window.update()
    readserial()
