#!/usr/share/python

import socket,sys

print "=============================================================================================="
print "=                                                                                            ="
print "=                                       KING WHOIS                                           ="
print "=                                                                                            ="
print "==============================================================================================\n"


if(len(sys.argv) < 2) :
	print "Modo de uso -> " + sys.argv[0] + " [DOMINIO]"
	quit()

socketIANA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketIANA.connect(("whois.iana.org", 43))

socketIANA.send(sys.argv[1] + "\r\n")

responseIANA = socketIANA.recv(1024).split()

socketIANA.close()


print "REFERENCIA: " + responseIANA[19]

socketRef = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketRef.connect((responseIANA[19], 43))

socketRef.send(sys.argv[1] + "\r\n")

responseRef = socketRef.recv(1024)

print responseRef
