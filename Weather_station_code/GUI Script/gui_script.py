from tkinter import *
import serial
import time

serialCom = serial.Serial('COM5', 9600)

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
        Label(window, text=index[0]).place(x=250, y=10)
    elif len(index) == 2:  # Humidity
        Label(window, text=index[1]).place(x=250, y=60)
    elif len(index) == 3:  # Moisture
        Label(window, text=index[2]).place(x=250, y=110)
    elif len(index) == 4:  # FAN TOGGLE
        Label(window, text=index[3]).place(x=500, y=60)
    elif len(index) == 5:  # PUMP TOGGLE
        Label(window, text=index[4]).place(x=500, y=110)


    if len(index) == 5:
        print("Done")
        index.clear()

    time.sleep(0.0001)


window = Tk()
window.title("Digital design project")
window.geometry("700x200")

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
