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

# window
window = Tk()
window.title("Digital design project")
window.geometry("1920x1080")

# grid
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)

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
        Label(window, text=index[3]).place(x=200, y=0)
    elif len(index) == 5:  # RPM
        text = index[4]
        rpm = float(text)
        kmh = 0.0082938*rpm
        kmh=int(kmh)
        Label(window, text=kmh).place(x=500, y=200)
    elif len(index) == 6:  # Humid
        Label(window, text=index[5]).place(x=200, y=220)
    elif len(index) == 7:  # Temp
        Label(window, text=index[6]).place(x=200, y=200)

    if len(index) == 7:
        print("")
        index.clear()

    time.sleep(0.0001)





while True:
    window.update()
    readserial()
