import matplotlib, numpy
import serial
import time
import threading
from multiprocessing import Process
matplotlib.use('TkAgg')

class Raam:
    def __init__(self, name, port, mode):
        self.name = name
        self.port = port
        if mode == 0:
            self.mode = "Handmatig"
        elif mode == 1:
            self.mode = "Licht"
        elif mode == 2:
            self.mode = "Temp"
        else:
            self.mode = "Handmatig"
        self.status = "In"
        self.uitrolstand = 50
        self.connected = False
        self.tempList = []
        self.brightList = []
        self.lichtDrempel = 90;
        self.tempDrempel = 30;
        try:
            self.connectDevice(self.name, self.port)
            self.connected = True
        except:
            print(self.name + " not connected.")
        self.isRequesting = False

    def connectDevice(self, name, port):
        global ser
        self.ser = serial.Serial("COM" + "%s" % str(port), 19200, timeout=1)
        time.sleep(1)
        self.handshake()

    def getConnected(self):
        return self.connected
    def getBrightList(self):
        return self.brightList
    def getTempList(self):
        return self.tempList
    def getId(self):
        return self.id;

    def setConnected(self):
        if self.connected == True:
            self.connected = False
        else:
            try:
                self.connectDevice(self.name, self.port)
                self.connected = True
            except:
                print(self.name + " not connected.")

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
        if self.mode == "Handmatig":
            self.mode = "Licht"
        elif self.mode == "Licht":
            self.mode = "Temperatuur"
        else:
            self.mode = "Handmatig"

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

    def getLichtDrempel(self):
        return self.lichtDrempel;

    def getTempDrempel(self):
        return self.tempDrempel;

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
        time.sleep(1)
        while True:
            #try:
                if self.isRequesting == False:
                    self.isRequesting = True
                    r = self.requestInfo("2")
                    # self.brightnessLabel.config(text="Brightness: %s" % r[1])
                    b = r[1]
                    if r[1] == "":
                        b = 0
                        brightnessFinal = int(b) / 10.24
                    else:
                        brightnessFinal = int(b) / 10.24
                        if(len(self.brightList) > 22):
                            del self.brightList[0];
                        self.brightList.append(round(brightnessFinal, 2))
                    print(self.name + ": Brightness: " + str(round(brightnessFinal, 2)))
                    #Check brightness value
                    if int(brightnessFinal) > self.lichtDrempel and self.mode == "Licht" and int(brightnessFinal) > 0:
                        time.sleep(2);
                        r = self.requestInfo("4")
                        print("val is " + r[1])
                        if r[1] == "4444":
                            print(self.getName() + " is opening..")
                    elif self.mode == "Licht":
                        time.sleep(2);
                        r = self.requestInfo("5")
                        print("val is " + r[1])
                        if r[1] == "5555":
                            print(self.getName() + " is closing..")
                    self.isRequesting = False
                time.sleep(18)
            #except:
            #    print(self.name + "disconnected")
             #   self.connected = False

    def getTemp(self):
        time.sleep(6)
        while True:
            #try:
                if self.isRequesting == False:
                    self.isRequesting = True
                    r = self.requestInfo("1")
                    b = r[1]
                    if r[1] == "":
                        b = 0
                        tempFinal = int(b) / 100
                    else:
                        tempFinal = int(b) / 100
                        if (len(self.tempList) > 22):
                            del self.tempList[0];
                        self.tempList.append(round(tempFinal, 2))
                    # self.brightnessLabel.config(text="Brightness: %s" % r[1])
                    # Check brightness value
                    if int(tempFinal) > self.tempDrempel and self.mode == "Temperatuur" and int(tempFinal) > 0:
                        time.sleep(2);
                        r = self.requestInfo("4")
                        print("val is " + r[1])
                        if r[1] == "4444":
                            print(self.getName() + " is opening..")
                    elif self.mode == True:
                        time.sleep(2);
                        r = self.requestInfo("5")
                        print("val is " + r[1])
                        if r[1] == "5555":
                            print(self.getName() + " is closing..")
                    print(self.name + ": Temp: " + str(tempFinal))
                    self.isRequesting = False
                time.sleep(18)
            #except:
             #   print(self.name + " is gedisconnect")
            #    self.connected = False

    def getDistance(self):
        time.sleep(10)
        while True:
            #try:
                if self.isRequesting == False:
                    self.isRequesting = True
                    r = self.requestInfo("3")
                    b = r[1]
                    if r[1] == "":
                        b = 0
                    # self.brightnessLabel.config(text="Brightness: %s" % r[1])
                    print(self.name + ": Distance: " + str(b))
                    self.isRequesting = False
                time.sleep(18)
            #except:
            #    print(self.name + " is gedisconnect")
            #    self.connected = False

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
        self.uitrolstand = val;
        if self.isRequesting == False:
            self.isRequesting = True
            F = "6" + str(val);
            r = self.requestInfo(F)
            b = r[1]
            if r[1] == "":
                b = 0
            # self.brightnessLabel.config(text="Brightness: %s" % r[1])
            print(self.name + ": " + str(b))
            self.isRequesting = False

    def setLichtDrempel(self, val):
        self.lichtDrempel = val;

    def setTempDrempel(self, val):
        self.tempDrempel = val;

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

