# -*- coding: utf-8 -*-

# Class log for consol
import time


class Logs:
    def __init__(self):
        self.history = []
        t = time.localtime()[:]
        houre = str(t[3]) + ":" + str(t[4]) + ":" + str(t[5])
        date = str(t[2]) + "-" + str(t[1]) + "-" + str(t[0])
        self.user = date + "@" + houre

    def updateTime(self):
        t = time.localtime()[:]
        houre = str(t[3]) + ":" + str(t[4]) + ":" + str(t[5])
        date = str(t[2]) + "-" + str(t[1]) + "-" + str(t[0])
        self.user = date + "@" + houre

    def addCmd(self, cmd):
        self.updateTime()
        self.history.append("$" + self.user + "#>> " + cmd)

    def addReturn(self, cmd):
        self.updateTime()
        self.history.append("-> " + cmd)

    def addLog(self, log):
        self.updateTime()
        self.history.append("$" + self.user + " : " + log)

    def clearCmd(self):
        self.history = []

    def getHistory(self):
        return self.history

    def getDate(self):
        return self.user.split("@")[0]

    def show(self):
        for line in self.history:
            print(line)
