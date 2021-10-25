from Function import *
from urllib.request import Request, urlopen


class loading:
    """docstring for Map"""

    def __init__(self):
        self.type = "Menu"
        self.clock = pygame.time.Clock()
        self.y = 0
        self.up = True
        self.status = ["Cheking", "Downloading", "Loading"]
        self.underStatus = {
            "Cheking": ["Files", "Updates"],
            "Downloading": ["New Files"],
            "Loading": ["Script", "Images"],
        }
        self.cmd = {
            "Files": self.chFiles,
            "Updates": self.Updat,
            "New Files": self.download,
            "Script": self.loadSc,
            "Images": self.loadIm,
        }
        self.dones = {
            "Files": False,
            "Updates": False,
            "New Files": False,
            "Script": False,
            "Images": False,
        }
        self.continu = True
        self.done = False
        self.Files = [
           "Function.py",
            "ListeFiles.llG",
            "ListePr.py",
            "Loading.py",
            "main.py",
            "maincore.py",
            "mapping.py",
            "menu.py",
            "pnjadder.py",
           "sandbox.py",
            "struc.py",
           "Update.llG",
          "Version.llG"
        ]
        self.img = [
            "logo.png",
            "menu.png",
            "Out/0.png",
            "Out/1.png",
            "Out/10.png",
            "Out/11.png",
            "Out/12.png",
            "Out/13.png",
            "Out/14.png",
            "Out/15.png",
            "Out/16.png",
            "Out/17.png",
            "Out/18.png",
            "Out/2.png",
            "Out/3.png",
            "Out/4.png",
            "Out/5.png",
            "Out/6.png",
            "Out/7.png",
            "Out/8.png",
            "Out/9.png",
            "Pnj/select.png",
            "Pnj/death.png",
            "Pnj/Citizen/0.png",
            "Pnj/Citizen/1.png",
            "Pnj/Citizen/2.png",
            "Pnj/Citizen/3.png",
            "Pnj/Citizen/4.png",
            "Pnj/Citizen/5.png",
            "Pnj/Farmer/0.png",
            "Pnj/Farmer/1.png",
            "Pnj/Farmer/2.png",
            "Pnj/Farmer/3.png",
            "Pnj/Killer/0.png",
            "Structure/0.png",
            "Structure/1.png",
            "Structure/10.png",
            "Structure/11.png",
            "Structure/12.png",
            "Structure/2.png",
            "Structure/3.png",
            "Structure/4.png",
            "Structure/5.png",
            "Structure/6.png",
            "Structure/7.png",
            "Structure/8.png",
            "Structure/9.png",
            "UI/0.png",
            "UI/1.png",
            "UI/2.png",
            "UI/3.png",
            "UI/4.png",
            "UI/5.png",
            "UI/6.png",
            "UI/7.png",
            "UI/8.png",
        ]

    def start(self):
        pygame.init()
        self.needUp = False
        pygame.font.init()
        self.header = pygame.font.Font("../Libs/head.ttf", 64)
        self.submenu = pygame.font.Font("../Libs/menu.ttf", 42)
        self.info = pygame.font.Font("../Libs/menu.ttf", 20)
        self.display = pygame.display.set_mode((768, 640))
        pygame.display.set_caption("SandStoneBox")
        pygame.display.set_icon(PyImgLoad("../img/logo.png"))

    def anime_title(self):
        if self.up:
            self.y += 1
        else:
            self.y -= 1
        if self.y > 20:
            self.up = False
        elif self.y < 0:
            self.up = True

    def Show(self):
        self.anime_title()
        self.show_bg()
        self.load()
        pygame.display.update()

    def show_bg(self):
        self.display.fill((173, 173, 173))
        self.display.blit(
            PyPrint("SandStoneBox", (80, 80, 36), self.header), (140, 158)
        )
        self.display.blit(
            PyPrint("SandStoneBox", (198, 198, 116), self.header), (140, 128 - self.y)
        )
        self.display.blit(
            PyPrint("Create by Rouxhero", (158, 255, 218), self.submenu), (390, 600)
        )

    def tick(self):
        self.clock.tick(15)

    def load(self):
        for statu in self.status:
            for underSt in self.underStatus[statu]:
                self.show_bg()
                self.display.blit(
                    PyPrint(statu + " : " + underSt, (158, 255, 218), self.submenu),
                    (250, 300),
                )
                if not self.dones[underSt]:
                    self.cmd[underSt]()

    def chFiles(self):
        i = 0
        for files in self.Files:
            self.display.blit(
                PyPrint("#", (243, 103, 194), self.info), (50 + i * 15, 350)
            )
            i += 1
            pygame.display.update()
            try:
                open(files, "r").read()
                print(files + " : good")
            except FileNotFoundError:
                print(files + " : missing !")
                self.needUp = True
        for files in self.img:
            self.display.blit(
                PyPrint("#", (243, 103, 194), self.info), (50 + i * 15, 350)
            )
            i += 1
            pygame.display.update()
            try:
                open("../img/"+files, "r")
                print(files + " : good")
            except FileNotFoundError:
                print(files + " : missing !")
                self.needUp = True
        self.dones["Files"] = True

    def Updat(self):
        url = (
            "https://gitlab.com/Rouxhero/sandstonebox/-/raw/master/Script/Update.llG?inline=false"
        )
        self.display.blit(
            PyPrint("#", (243, 103, 194), self.info), (50, 350)
        )
        pygame.display.update()
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        self.vers = open('Version.llG','r').read()
        if webpage != self.vers :
            self.vers = webpage
            self.needUp = True
            print('New update avaible')
        self.dones["Updates"] = True

    def download(self):
        if self.needUp :
            i = -1
            end = len(self.Files)+len(self.img)
            url = (
            "https://gitlab.com/Rouxhero/sandstonebox/-/raw/master/Script/ListeFiles.llG?inline=false"
            )
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            web_byte = urlopen(req).read()
            webpage = web_byte.decode("utf-8")
            okfiles = open('ListeFiles.llG','r').read()
            if okfiles == webpage:
                print('No New files !')
                for files in self.Files:
                    i+=1
                    self.display.blit(
                        PyPrint("Download", (243, 103, 194), self.info), (50, 350)
                    )
                    pygame.display.update()
                    url = (
                    "https://gitlab.com/Rouxhero/sandstonebox/-/raw/master/Script/"
                    +files
                    +"?inline=false"
                    )
                    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    print("Download : "+files +" => " +str(((i*100)/end)//1)+" %")
                    web_byte = urlopen(req).read()
                    webpage = web_byte.decode("utf-8")
                    open(files,"w").write(webpage)
                for files in self.img:
                    i+=1
                    print("Download : "+files +" => " +str(((i*100)/end)//1)+" %")
                    url = (
                    "https://gitlab.com/Rouxhero/sandstonebox/-/raw/master/img/"
                    +files
                    +"?inline=false"
                    )
                    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    web_byte = urlopen(req).read()
                open("../img/"+files,"wb").write(web_byte)
                open('Version.llG','w').write(self.vers)
                self.dones["New Files"] = True

    def loadSc(self):
        pass

    def loadIm(self):
        self.display.blit(
            PyPrint("Push a key to play", (158, 255, 218), self.submenu), (250, 370)
        )
        self.done = True


mainG = loading()
mainG.start()
while mainG.continu:
    mainG.tick()
    for event in pygame.event.get():
        if event.type == QUIT:
            mainG.continu = False
        if event.type == KEYDOWN and mainG.done == True:
            mainG.continu = False
    mainG.Show()
