from tkinter import*
import random
import time
import tkinter as tk
import socket

#Server Setup

TCP_IP = '192.168.4.2'
TCP_PORT = 3030
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)  # echo
conn.close()

#Window Construction

root=Tk()
root.geometry("400x200")
root.title("Light v.1")
root.resizable(False, False)

#Variable Section

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

time_one=''
def update_Time():
    global time_one
    time_two=time.strftime('%H:%M:%S')
    # Update String for Time
    if time_two != time_one:
        time_one = time_two
        Info_Time.config(text=time_two)
    #Calling every 200ms
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



#Bottun Section
def getInput():
    A=int(Display1.get())
    B=Display2.get()
    C=Display3.get()
    D=Display4.get()
    print(A,B,C,D)

    global operator
    operator=[A,B,C,D]
    
    if (A>=24 and A<0):
        BG.destroy()



    
    
b1= Button(BG,text="Apply",command=getInput).grid(row=3)
    
    
    


root.mainloop()
