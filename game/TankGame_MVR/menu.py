ofrom Tkinter import *
from ftplib import FTP
import os
import time
main1 = Tk()

main = LabelFrame(main1, text="Loading game", padx=20, pady=20)
main.pack()
main1.title('TaNk')
co = Label(main,text='connecting to server ')
co.pack()
main1.update()
ftp = FTP('ftp.byethost22.com', 'b22_22483937', 'AscEfb753')
co.destroy()
co = Label(main,text='done')
co.pack()
main1.update()
co.destroy()
co = Label(main,text='founding data')
co.pack()
main1.update()
ftp.sendcmd('CWD htdocs')
ftp.sendcmd('CWD TaNk')
co.destroy()
co = Label(main,text='done')
co.pack()
main1.update()
co.destroy()
co = Label(main,text='geting data : 0 %')
co.pack()
main1.update()
for i in range (0,14):
	ftp.retrbinary('RETR '+str(i)+'.png', open('img/'+str(i)+'.png', 'wb').write)
	co.destroy()
	co = Label(main,text='geting data : '+str((i*100)/14)+' %')
	co.pack()
	main1.update()
co.destroy()
co = Label(main,text='done')
co.pack()
main1.update()
main.destroy()

main = LabelFrame(main1, text="Welcome on TaNk", padx=20, pady=20)
main.pack()
Button(main,text='PLay solo').pack(padx=20, pady=10)
Button(main,text='PLay multi').pack(padx=20, pady=10)
Button(main,text='Option').pack(padx=20, pady=10)



main1.mainloop()