import matplotlib, numpy
import serial
import time
import threading
from multiprocessing import Process
matplotlib.use('TkAgg')

class Raam:
    def __init__(self, name, port):
        self.name = name
        self.port = port
        self.mode = True
        self.status = "In"
        self.uitrolstand = 50
        self.connectDevice(self.name, self.port)
        self.isRequesting = False

    def connectDevice(self, name, port):
        global ser
        self.ser = serial.Serial("COM" + "%s" % str(port), 19200, timeout=1)
        time.sleep(1)
        self.handshake()

    def statusthreader(self):
        self.brightnessthread = threading.Thread(None, self.getBrightness)
        self.brightnessthread.start()
        self.temperaturethread = threading.Thread(None, self.getTemp)
        self.temperaturethread.start()
        self.distthread = threading.Thread(None, self.getDistance)
        self.distthread.start()

    def statusprocessor(self):
        self.statusprocess = Process(target=self.statusthreader())
        self.statusprocess.start()

    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True

    def getName(self):
        return self.name

    def getMode(self):
        return self.mode

    def getStatus(self):
        return self.status

    def getPoort(self):
        return self.port

    def getUitrolstand(self):
        return self.uitrolstand

    def requestInfo(self, command):
        self.ser.write((command + "\n").encode('ascii'))
        extra_info = "Succesvol uitgevoerd"
        returnvalue = self.ser.readline().decode('ascii').strip()
        if returnvalue not in ["Valide commando", "Echo"]:
            extra_info = returnvalue
            returnvalue = self.ser.readline().decode('ascii').strip()
            if returnvalue not in ["Valide commando", "Echo"]:
                returnvalue = "echo"
        return returnvalue, extra_info

    # Request the current level of brightness every 60 seconds
    def getBrightness(self):
        time.sleep(3)
        while True:
            if self.isRequesting == False:
                self.isRequesting = True
                r = self.requestInfo("2")
                # self.brightnessLabel.config(text="Brightness: %s" % r[1])
                brightnessFinal = int(r[1]) / 10.24
                print("Brightness: " + str(round(brightnessFinal, 2)))
                self.isRequesting = False
            time.sleep(9)

    def getTemp(self):
        time.sleep(6)
        while True:
            if self.isRequesting == False:
                self.isRequesting = True
                r = self.requestInfo("1")
                # self.brightnessLabel.config(text="Brightness: %s" % r[1])
                tempFinal = int(r[1]) / 100
                print("Temp: " + str(tempFinal))
                self.isRequesting = False
            time.sleep(9)

    def getDistance(self):
        time.sleep(9)
        while True:
            if self.isRequesting == False:
                self.isRequesting = True
                r = self.requestInfo("3")
                # self.brightnessLabel.config(text="Brightness: %s" % r[1])
                print("Distance: " + str(r[1]))
                self.isRequesting = False
            time.sleep(9)

    # Creates the handshake, provided by Simon van der Meer
    def handshake(self):
        tries_left = 3
        while tries_left > 0:
            r = self.requestInfo("handshake")
            if r[1] == "Hand shaked!":
                tries_left = 0
                print("Connected to device")
                self.statusprocessor()
            else:
                tries_left -= 1
                print("Failed")
                if tries_left == 0:
                    print("Hand not shaken")
                    sys.exit(1)

    def setName(self, name):
        self.name = name

    def setStatus(self, val):
        self.status = val

    def setPoort(self, val):
        self.port = val

    def setUitrolstand(self, val):
        self.uitrolstand = val

    def setStatus(self):
        if self.status == "In":
            self.status = "Uit"
            # in
            if self.isRequesting == False:
                self.isRequesting = True
                r = self.requestInfo("4")
                print("val is " + r[1])
                if r[1] == "4444":
                    print(self.getName() + " is opening..")
                self.isRequesting = False
        else:
            self.status = "In"
            # uit
            if self.isRequesting == False:
                self.isRequesting = True
                r = self.requestInfo("5")
                print("val is " + r[1])
                if r[1] == "5555":
                    print(self.getName() + " is closing..")
                self.isRequesting = False

