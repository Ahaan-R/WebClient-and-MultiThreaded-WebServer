#Ahaan Rajesh
#ID:1001768638


import socket    #for socket connection
import os       #for renaming files
import webbrowser         #for opening webpages
import random       #to generate random numbers

url = input()
csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating client socket
csocket.connect((socket.gethostname(), 8080))   # connecting to server

csocket.send(bytes(url, "UTF-8"))  # sending data to server


msg = csocket.recv(1024)  # receiving message from client
message = msg.decode("UTF-8")
print("C: ", message)
check = "HTTP/1.1 200 OK"
if message == check:
    num=random.randint(1, 100)  #  creating a random number for file
    msg = csocket.recv(1024)  # receiving message from server
    filecontent = msg.decode("UTF-8")  # decoding message
    f = open("index%s.txt" %num, 'w')
    f.write(filecontent)    # writing contents into text file
    f.close()
    os.rename("index%s.txt" %num, "index%s.html" %num) # renaming text file to html file
    webbrowser.open("index%s.html" %num, new=2)  # open in new tab
    csocket.close()
else:
    csocket.close()



