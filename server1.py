'''#server
import socket
import datetime

when=datetime.datetime.now()
exact_time=when.strftime("%H:%M:%S")
#creat a proxy socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#get the host name and the port number of the proxy server
r=socket.gethostname()
hostp= socket.gethostbyname(r)
port=12345
#bind the socket to the host name and port number
sock.bind((hostp, port))
#listen for connections that are trying to pass it
sock.listen(1)
print("connected",hostp,port)
while True:
    #let the socket wait for a connection from the server
    Client_s, address =sock.accept()
    #receive from the client the ip address he puts
    ip=Client_s.recv(1024).decode()
    print("Client's request is received: ",ip,"time is: ", exact_time)
    #split the request sentence to get the ip address
    split_sent= ip.split()
    IP=split_sent[4]
    #connect to a website with the received ip address:
    sock_web=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock_web.connect((IP,80))
    #send ip to open the website 
    sock_web.send(ip.encode())
    print("the time of actual request: ", exact_time)
    #receicve the websit's respone 
    res=sock_web.recv(1024)
    print("response received from server: done ","@: ", exact_time) 
    #send the response to the client 
    Client_s.send(res)
    print("response was sent to client: done ","@: ",exact_time) 
    #close all sockets 
    sock_web.close()
    Client_s.close()
'''