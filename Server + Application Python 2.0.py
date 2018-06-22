import threading
import socket
#Server Thread 
##In dieser Funktion wird der Server aufgebaut.
#@param A Startstunde
#@param B Startminute
#@param C Endstunde
#@param D Endminute
#@param H Aktuelle Stunde
#@param M Aktuelle Minute
#
##Die Parameter befinden sich in der while Schleife, damit sie sich dauerhaft aktualisieren und sich die Funktion nicht nur auf die am Anfang eingegebenen Werte bezieht.
def Server_Function():
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)		
	ip = socket.gethostbyname(socket.gethostname())					#IP des Servers wird direkt vom Host bezogen.
	port = 3030
	address = (ip,port)
	server.bind(address)
	server.listen(1)												#Der Server kann maximal 1 aktive Verbindung haben
	print (" Suche clients ",ip,":",port)
	client,addr = server.accept()
	print (" Verbindung mit Smart Home ",addr[0],":",addr[1])
	#A,B,C,D = getInput()
	#H,M = Uhrzeit()
	while True:
		A,B,C,D = getInput()										#In der While Schleife, damit sich die eingegebenen Werte immer wieder aufs neue aktualisieren.
		H,M = Uhrzeit()
		data = client.recv(1024)
		print (" Folgende Eingabe wurde getätigt : ",data," vom client ")
		print (" Verarbeite Eingabe ")
		if data==b'Z':
				if A > int(H) and C <= int(H):						#Fertig
					print( "Licht aus")
					client.send(b'f')
				if A > int(H) and C >= int(H):                   	#Fertig
					print(" Licht aus")
					client.send(b'f')
				if A < int(H) and C >= int(H):						#Fertig
					if B < int(M) and D < int(M):
						print( "Licht an" )
						client.send(b'n')
					if B < int(M) and D > int(M):
						print( "Licht an" )
						client.send(b'n')
					if B == int(M) and D == int(M):
						print( "Licht an" )
						client.send(b'n')
					if B > int(M) and D < int(M):
						print( "Licht an" )
						client.send(b'n')
					if B > int(M) and D > int(M):
						print( "Licht an")
						client.send(b'n')
				if A <= int(H) and C <= int(H):						#Fertig
					if B < int(M) and D < int(M):
						print( "Licht an" )
						client.send(b'n')
					if B < int(M) and D > int(M):
						print( "Licht an" )
						client.send(b'n')
					if B == int(M) and D == int(M):
						print( "Licht an" )
						client.send(b'n')
					if B > int(M) and D < int(M):
						print( "Licht aus" )
						client.send(b'f')
					if B > int(M) and D > int(M):
						print( "Licht aus")
						client.send(b'f')
				if A ==int(H) and C<= int(H):
					if B <= int(M) and D<= int(M):
						print( "Licht an" )
						client.send(b'n')
					if B > int(M) and D<= int(M):
						print( "Licht aus" )
						client.send(b'f')
				if A == int(H) and C>= int(H):
					if B <= int(M) and D<= int(M):
						print( "Licht an" )
						client.send(b'n')
					if B <= int(M) and D>= int(M):
						print( "Licht an" )
						client.send(b'n')
					if B > int(M) and D<= int(M):
						print( "Licht aus" )
						client.send(b'f')
				#else:
					#print( "Ungültige Zeit")
				print ("Verarbeitung erledigt.\n[*] Antwort gesendet")
		elif data==b"Disconnected":
				client.send(b" Goodbye ")
				client.close()
				break
		else:
				client.send(b"Invalid data")
				print (" Verarbeite ungültige Daten.\n[*] Antwort gesendet ")
				
##Hier wird der Server Thread gestartet
t = threading.Thread(target = Server_Function, name = 'Server Thread', args =())

t.start()
##Diese Funktion übermittel die aktuelle Uhrzeit + Minute und returned diese, damit andere Funktionen sich auf diese Werte beziehen können.
#@param H Aktuelle Stunde
#@param M Aktuelle Minute
def Uhrzeit():												#Funktion übermittelt die aktuelle Stunde + Minute.
	H = time.strftime("%H")
	M = time.strftime("%M")
	return H,M
#GUI Main Programm

from tkinter import*
import random
import time
import tkinter as tk
#Window Construction
root=Tk()
root.geometry("400x200")
root.title("Light v.1")
root.resizable(False, False)
#Variable Section
##Background
BG = Frame(root,width=400,height=200)
BG.pack(side=TOP)
Panel1 = Frame(root,width=200,height=100)
Panel1.pack(side=LEFT)
Info=Label(BG,font=('arial',20,'bold'),text="Time Settings",fg="black",bd=10,anchor='w')
Info.grid(row=0,column=0)
#Clock Section
time_one=''
Info_Time=Label(BG,font=('arial',20,'bold'),fg="green",bd=10,anchor='w')
Info_Time.grid(row=1,column=0)
## Time_one muss leer sein, da sonst die Funktion update_Time nicht funktionieren würde
time_one=''
##Diese Funktion erzeugt die im GUI zusehende Zeitangabe. 
def update_Time():												#Funktion für die UHR im GUI. Zeit wird alle 200ms aktualisiert.
	global time_one
	time_two=time.strftime('%H:%M:%S')
	# Überschreibung des Time Strings
	if time_two != time_one:
		time_one = time_two
		Info_Time.config(text=time_two)
	#Alle 200ms wird die Zeit aktualisiert.
	Info_Time.after(200, update_Time)
update_Time()
#Entry Section
Display1=Entry(Panel1,font=('comic sans',10,'bold'))
Display1.grid(row=1,column=1)
Display2=Entry(Panel1,font=('arial',10,'bold'))
Display2.grid(row=1,column=2)
Display3=Entry(Panel1,font=('arial',10,'bold'))
Display3.grid(row=2,column=1)
Display4=Entry(Panel1,font=('arial',10,'bold'))
Display4.grid(row=2,column=2)
#Text Section
Text1=Label(Panel1,text="Von").grid(row=1,column=0)
Text2=Label(Panel1,text="Bis").grid(row=2,column=0)
Text_Min=Label(Panel1,text="Stunden").grid(row=0,column=1)
Text_Min=Label(Panel1,text="Minuten").grid(row=0,column=2)
#Button Section	
##Diese Funktion schaut welche Eingaben der User in die Displays getätigt hat und returned diese, damit sich andere Funktionen darauf beziehen können.
#@param A Startstunde
#@param B Startminute
#@param C Endstunde
#@param D Endminute
def getInput():														#Funktion um die eingebenen Werte auszulesen.
	A=int(Display1.get())
	B=int(Display2.get())
	C=int(Display3.get())
	D=int(Display4.get())
	global operator
	operator=[A,B,C,D]
	return A,B,C,D
#b1= Button(BG,text="Reset",command=getInput).grid(row=3)
##Eine Debug Funktion
def Test():															#Test Funktion 
	A,B,C,D = getInput()
	print(A,B,C,D)
#b1= Button(BG,text="Test",command=Test).grid(row=3,column=1)
root.mainloop()
