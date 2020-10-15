from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('192.168.1.51', 5000))
print("client is connected")

print("what do you want to send!")
inp = input()
mesg = inp.encode('utf-8')
s.sendto(mesg,('192.168.1.51',5000))

data = s.recv(1024)
print('Received', data)
s.close()
