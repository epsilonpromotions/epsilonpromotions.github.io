import socket
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("""  _          _      _   _    ____   _               _   
 | |        / \    | \ | |  / ___| | |__     __ _  | |_ 
 | |       / _ \   |  \| | | |     | '_ \   / _` | | __|
 | |___   / ___ \  | |\  | | |___  | | | | | (_| | | |_ 
 |_____| /_/   \_\ |_| \_|  \____| |_| |_|  \__,_|  \__|
 """)

print("""
 __     __  ____         ___  
 \ \   / / |___ \       / _ \ 
  \ \ / /    __) |     | | | |  A simple chat client
   \ V /    / __/   _  | |_| |   © Cole Gosney 2015
    \_/    |_____| (_)  \___/ 
""")

print("Socket Created")

host = input("Please enter a host address: ")

port = int(input("Please enter the port number: "))

name = input("Screen name: ")

s.connect((host, port))

print("Connected to " + str(host) + ":" + str(port))

print("Type 'has left' to leave the chat!")

while True:
    message = input(">>>  ")    
    s.sendall(base64.encodebytes(bytes(name + ": " + message, 'UTF-8')))
    if message == 'has left':
        exit()
