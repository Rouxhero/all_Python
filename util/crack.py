from os import system
from ftplib import FTP
system('cls')
system('color 18')
print "#############################################"
print "#             Hacker's tools                #"
print "#                                           #"
print "#                                           #"
print "#             By LL's Games                 #"
print "#                                           #"
print "#############################################"

def scan_ip():
	valide_ip = []
	print "IP : 192.168.a."
	ii = input('Enter number for a')
	for i in range(225):
		host = ' 192.168.'+str(ii)+'.'+ str(i)
		reponse = system('ping -n 1 -w 12'+host)
		if reponse == 0 :
			valide_ip += host,
			print '\a'
	system('cls')
	print 'Found',len(valide_ip) , ' ip on your local network :'
	for i in range (len(valide_ip)) :
		print i,'.',valide_ip[i]
	return valide_ip

def ftp_scan():
	print "\nFTP SCAN :\n\n 1.Custum host\n 2.scan local ip"
	choix = input('Enter number : ')
	if choix == 1 :
		host = input('\n\nEnter host : ')
	elif choix == 2 :
		print 'Starting scan :'
		list_os = scan_ip()
		host = input('Enter number :')
		port = input('\nEnter port(default 21,type 0 for default) : ')
		if port == 0 :
			port = 21
		host = str(host) + ':'+ str(port)
	else :
		print 'ERROR quit !'
		quit()
	user = 'root'
	password = 'pass'
	try :
		ftp = FTP(host, user, password) 
	except socket.gaierror:
		print 'Adress dosen\'t exist'