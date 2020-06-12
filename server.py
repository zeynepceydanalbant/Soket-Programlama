#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
from socket import *
import random

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('',12345)) #UDP NO 12345 
    while True:
    i = random.randint(0,10) 
    b, address = serverSocket.recvfrom(1024)
    b = b.upper()
    
    if i < 4:

    	  print(j + 'drop')
	  continue
    	
    if (j.decode().startswith("PING")):	

	  serverSocket.sendto("PONG".encode(), address) 
