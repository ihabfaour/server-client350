'''#client
import socket
import time
import uuid
import datetime

when=datetime.datetime.now()
exact_time=when.strftime("%H:%M:%S")
macAddres= uuid.getnode()

start_time = time.time()
#creat a socket for the client
Client_s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
#get the host name and port of the proxy server
r=socket.gethostname()
hostp= socket.gethostbyname(r)
port=12345
dest_ip= input("enter ip of website: ")
#connect to the proxy server
Client_s.connect((hostp,port))
#send the messege including the ip address to the server
Cl_req= "GET / HTTP/1.1\r\nHost: " + dest_ip + "\r\n\r\n"
print("the request is: ", Cl_req)
Client_s.send(Cl_req.encode())
print("need data from the website of ip: ", dest_ip, "time is: ", exact_time) 
#receive the response of the website from the proxy server
cl_res=Client_s.recv(1024)
print("response is: ", cl_res) 
end_time=time.time()
total_time= end_time - start_time
hrs, sec_remaining= divmod(total_time,3600)
mints,sec = divmod(sec_remaining,60)
print("round trip time is: ",int(hrs), int(mints), int(sec))
print("MAC ADDRESS IS: ".join(format(s,'02x') for s in macAddres.to_bytes(6, byteorder='big')))
Client_s.close()

'''
