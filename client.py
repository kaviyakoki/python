import socket
s=socket.socket()
host=socket.gethostname()
port=80
s.connect((host,port))
a=s.recv(1024)
print(a.decode(),"i am client")
s.close()