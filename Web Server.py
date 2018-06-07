#!/usr/bin/env python

import socket


TCP_IP = '192.168.4.2'
TCP_PORT = 3030
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    conn.send(b'Hallo')  # echo
conn.close()
