#Ahaan Rajesh
#ID:1001768638

import socket
import threading



url1 = "http://localhost:8080/index.html"   # storing the correct urls for comparison
url2 = "http://localhost:8080/"         # storing the correct urls for comparison
url3 = 'http://localhost:8080/C:/Users/Test/PycharmProjects/cn/Home.html'       #storing the correct urls for comparison
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating the server side socket
serversocket.bind((socket.gethostname(), 8080))     #initialising the ip and port no to the server
serversocket.listen()

def task1(clienturl):
    if clienturl == url1 or clienturl == url2 or clienturl == url3:
        clientsocket.send(bytes("HTTP/1.1 200 OK", "UTF-8"))  # sending success header to client
        filename = 'Home.html'  # sending html page to client
        f = open(filename, 'rb')
        l = f.read(1024)
        while (l):
            clientsocket.send(l)
            print('S: Sent data to client ')
            l = f.read(1024)
        f.close()  # closing the socket once file is sent
        clientsocket.close()    #closing the socket once data is sent
    else:
        print(f'S: Failed to connect with client having address {address} ')
        clientsocket.send(bytes("HTTP/1.1 404 Not Found", "UTF-8"))  # sending failure header to client
    clientsocket.close()        #closing the socket once  data is sent



while True:
    clientsocket, address =serversocket.accept()    # assigning clientsocket, the socket of the accepted client and address is client's IP address
    print(f"S: connected to client with address {address}")
    msg = clientsocket.recv(1024)  # receiving message from client
    clienturl=msg.decode("UTF-8")
    t = threading.Thread(target=task1, name='t', args=(clienturl,))       #creating thread for every client coming in
    t.start()













