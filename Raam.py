import matplotlib, numpy
matplotlib.use('TkAgg')

class Raam:
    def __init__(self, name, port):
        self.name = name
        self.port = port
        self.mode = True
        self.status = "In"
        self.uitrolstand = 50

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
        else:
            self.status = "In"

