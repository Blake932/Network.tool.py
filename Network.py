#Imports sockets // networking 
import socket
import threading 
import os, requests, time, random, sys


# Defines 

class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.options()
        while self.gg == True:
            choose = input(str('Enter option: '))
            if(choose == str("1")):
            	Local_info()
            elif(choose == str("2")):
              DOM_lookup()
            elif(choose == str("3")):
              URL_lookup()

    def options(self):
    	print(self.r + " \n [1] Local machine \n")
    	print(self.c + " [2] IP Domain lookup \n")
    	print(self.rr + ''' [3] URL IP lookup
            
            
███╗   ██╗███████╗████████╗
████╗  ██║██╔════╝╚══██╔══╝
██╔██╗ ██║█████╗     ██║   
██║╚██╗██║██╔══╝     ██║   
██║ ╚████║███████╗   ██║   
╚═╝  ╚═══╝╚══════╝   ╚═╝   
                           
\n''')     

def URL_lookup():
  host_name1 = input("Enter URL: ")
  print(f'The {host_name1} IP: {socket.gethostbyname(host_name1)}')

def DOM_lookup():
  try:
    ipdom = input("Enter domain: ")
    IP = socket.gethostbyname(ipdom)
    print("IP: " + IP)
  except:
    print("Invalid Domain")
    
# Defining local info as a call 
def Local_info():
# Defines and calls python // network to give both IP and local machine name 
		try:
			h_name = socket.gethostname()
		except:
			print("Invalid machine")

		try:
			IP_addres = socket.gethostbyname(h_name)
		except:
			print("Invalid local machine")
			# Displaying both 
		print("Host Name is: " + h_name)
		print("Computer IP Address is: " + IP_addres)

Main()
