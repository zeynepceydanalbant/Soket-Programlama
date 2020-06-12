#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import socket

with open("hosts.txt","r") as acilacakDosya: 
   for satirlar in acilacakDosya:
	
	print('Hedef :' + satirlar)
	        
	host = satirlar 
	ping = 5 
	kayip = 1 
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	clientSocket.settimeout(kayip)
	gonderi = 'ping'
	for i in range(ping):
	    try:
		
		baslangic = time.time()
		clientSocket.sendto(gonderi, (host, 12345))
		c, server = clientSocket.recvfrom(1024)
		bitis = time.time() 
		rtt = (bitis - baslangic) * 100000
		print('User Datagram Protocol:' + satirlar)
		print( 'Round Trip Time: ' + str(rtt) )
	    except socket.timeout :		
		print('Paket Kayboldu!') 


