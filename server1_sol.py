from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 5000))

s.listen()
print ("Server is listening...")
while True:
    (conn, addr) = s.accept()
    print("addr: ", addr)

    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data+b'*')
    conn.close()
s.close()
