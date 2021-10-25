# -*- coding: utf-8 -*-

# Class to create SaveApp

class Files:
    def __init__(self, name, bools):
        if bools:
            self.name = "../Data/" + name
        else:
            self.name = name
        self.file = """#Configuration files\n"""

    def init(self):
        try:
            f = open(self.name, "r")
        except FileNotFoundError:
            open(self.name, "w")
            return "[File][Error] : Files doesn't exist! => File created"
        return "[File][Succes] Files " + self.name + " open !"

    def addOption(self, name, value, *com):
        """
        format : addOption("Key","Value","Tips") or addOption("Key","Value")
        /!\\ no Value while create a empty key on file
        """
        if len(com) > 0:
            self.file += "#" + com[0] + "\n-" + name + "\n" + value + "\n"
        else:
            self.file += "-" + name + "\n" + value + "\n"
        return "[File][Succes] Option added !"

    def getAllOption(self):
        option = {}
        key = None
        lines = open(self.name, "r").read().split("\n")
        for line in lines:
            if len(line) > 1:
                if line[0] != "#":
                    if line[0] == "-":
                        key = line[1:]
                    else:
                        if key != None:
                            line = self.uncode(line)
                            option[key] = line
                            key = None
        return ["[File][Succes]" + str(len(option)) + " option loaded", option]

    def uncode(self, line):
        booleanDic = {
            "True": True,
            "true": True,
            "False": False,
            "false": False,
        }
        if line in booleanDic:
            return booleanDic[line]
        else:
            try:
                return int(line)
            except ValueError:
                return line

    def saveFiles(self):
        open(self.name, "w").write(self.file)
        return "[File][Succes] Config files saved at : " + self.name


if __name__ == "__main__":
    save = Files("data.tmp", False)
    logs = log.Logs()
    logs.addLog(save.init())
    logs.addLog(save.addOption("Scale", "451x152", "Screen scale for windows"))
    logs.addLog(save.addOption("age", "20", "Age of user"))
    logs.addLog(save.addOption("FirstL", "true", "To show tips"))
    logs.addLog(save.addOption("DbConnected", "false"))
    logs.addLog(save.addOption("DbisConfig", "true"))
    logs.addLog(save.saveFiles())
    res = save.getAllOption()
    logs.addLog(res[0])
    print(res[1])

    logs.show()
