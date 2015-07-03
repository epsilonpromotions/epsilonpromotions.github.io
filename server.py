import socket, select

print("""  _          _      _   _    ____   _               _   
 | |        / \    | \ | |  / ___| | |__     __ _  | |_ 
 | |       / _ \   |  \| | | |     | '_ \   / _` | | __|
 | |___   / ___ \  | |\  | | |___  | | | | | (_| | | |_ 
 |_____| /_/   \_\ |_| \_|  \____| |_| |_|  \__,_|  \__|
 """)

print("""
 __     __  ____         ___  
 \ \   / / |___ \       / _ \ 
  \ \ / /    __) |     | | | |  A simple chat server
   \ V /    / __/   _  | |_| |   © Cole Gosney 2015
    \_/    |_____| (_)  \___/ 
""")


host = socket.gethostbyname(socket.gethostname())

connections = []

print("The local IP for connecting to this server is :" + host)

port = int(input("Enter your desired port (go higher than 1800 to reduce chances of overlap, but stay below 10,000): ")) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Socket created")

s.bind((host, port))

print("Socket bound")

s.listen(10)

print("Socket listening for requests")

def test_connection():
    global connection, connections
    print("testing connection")
    read_list = [s]
    readable, writable, errored = select.select(read_list, [], [], 0.2)
    for a in readable:
        if a is s:
            connection, addr = s.accept()
            connections.append(connection)
            print("Connection from ", addr)

while True:
    test_connection()
    for i in connections:
        print("looking for data for ", i)
        read_list = [i]
        readable, writable, errored = select.select(read_list, [], [], 0.2)
        for a in readable:
            if a is i: 
                try:
                    data = i.recv(1024)
                except socket.error:
                    print("There has been an error. Removing causation socket.")
                    connections.remove(i)
                    break
                if not data or data.decode('UTF-8') == "":
                    print("no data")
                    break
                for k in connections:
                    print("sending ", data, " to ", k)
                    k.sendall(data)
                print(data.decode('UTF-8'))

for i in connections:
    connection.close()
    
s.close()
