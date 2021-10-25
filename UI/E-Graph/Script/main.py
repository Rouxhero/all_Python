# -*- coding: utf-8 -*-

import tkinter as tk
from utile.file import Files

def alert():
    print('ee')
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Liste des Frame
        self.option = Files("config.lg",True).getAllOption()[1]
        self.geometry(self.option["Screen"])
        self.bind("<F12>", self.toggleFullScreen)
        self.attributes('-fullscreen', self.option["fullscreen"])  
        # Definition du menu deroulant
        self.setMenu()
        # Init de l'app
        self.start()
        self.update()
    def toggleFullScreen(self, event):
        self.option["fullscreen"] = not self.option["fullscreen"]
        self.attributes("-fullscreen", self.option["fullscreen"])
    def toggleFullScreenB(self):
        self.option["fullscreen"] = not self.option["fullscreen"]
        self.attributes("-fullscreen", self.option["fullscreen"])
    def start(self):
        self.main = tk.LabelFrame(self,text="Welcome")
        tk.Label(self.main,text="Choisisez le mode de lancement").grid(row=0,column=2)
        tk.Button(self.main,text="New",command=alert).grid(row=1,column=0,padx=5, pady=5)
    def update(self):
        self.main.pack(side=tk.TOP)

    def setMenu(self):
        menubar = tk.Menu(self)
        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Open", command=alert)
        menu1.add_command(label="new", command=alert)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.destroy)
        menubar.add_cascade(label="Fichier", menu=menu1)
        menu2 = tk.Menu(menubar, tearoff=0)
        menu2.add_command(label="Copier", command=alert)
        menu2.add_command(label="Load", command=alert)
        menu2.add_separator()
        menu2.add_command(label="Export", command=alert)
        menubar.add_cascade(label="Editer", menu=menu2)
        menu3 = tk.Menu(menubar, tearoff=0)
        menu3.add_command(label="Show", command=alert)
        menubar.add_cascade(label="Calcul", menu=menu3)
        menu4 = tk.Menu(menubar, tearoff=0)
        menu4.add_command(label="Show", command=alert)
        menubar.add_cascade(label="Graph", menu=menu4)
        menu5 = tk.Menu(menubar, tearoff=0)
        menu5.add_command(label="Show", command=alert)
        menubar.add_cascade(label="Tableau", menu=menu5)
        menu6 = tk.Menu(menubar, tearoff=0)
        menu6.add_command(label="Theme", command=alert)
        menu6.add_command(label="Fullscreen", command=self.toggleFullScreenB)
        menubar.add_cascade(label="View", menu=menu6)
        menu7 = tk.Menu(menubar, tearoff=0)
        menu7.add_command(label="A propos", command=alert)
        menubar.add_cascade(label="Aide", menu=menu7)

        self.config(menu=menubar)

if __name__ == "__main__":
    app = Application()
    app.title("E-Graph")
    ##----- Programme principal -----##
    app.mainloop()  # Boucle d'attente des événements
