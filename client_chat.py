"""import socket
client = socket.socket()
client.connect(('192.168.43.5',1234))
print("connected to server\n")
while True:
    cmsg = input('\nclient-->')
    client.send(cmsg.encode())
    if cmsg.lower() == 'endofchat':
        print("\n closed")
        client.closed()
        break
    smsg = client.recv(1024).decode()
    print(f"server-->{smsg}")
    if smsg.lower() == 'endofchat':
        print('\nclosed')
        server.close()
        break
client.close()
"""

import socket
client = socket.socket()
client.connect(("192.168.43.5", 1234))
print("Connected to server\n\n")

while True:
    
    cmsg = input("client-->")
    client.send(cmsg.encode())
    if cmsg.lower() == 'endofchat':
        print("\n\nConnection closed by Client")
        client.close()
        break
    
    smsg = client.recv(1024).decode()
    print(f"server-->{smsg}".rjust(60))
    if smsg.lower() == 'endofchat':
        client.close()
        print("\n\nConnection closed by Server")
        break

