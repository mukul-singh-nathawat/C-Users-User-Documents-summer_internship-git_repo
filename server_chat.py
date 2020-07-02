"""import socket
server = socket.socket()
server.bind(('192.168.43.5',1234))
server.listen()
print("server: 192.168.43.5 : 1234")
client, addr = server.accept()
print(f"\n client:{addr[0]}:{addr[1]}")

while True:
    cmsg = server.recv(1234).decode()
    print(f"client--->{cmsg}\n")
    if cmsg.lower() == 'endofchat':
        print('closed')
        client.close()
        break
    smsg = input("server--->").encode()
    client.send(smsg)
    if smsg.decode().lower() == 'endofchat':
        print('closed')
        client.close()
        break
server.close()
"""
import socket
server = socket.socket()
server.bind(('192.168.43.5', 1234))
server.listen()
print("Server: 192.168.43.5:1234")
client, addr = server.accept()
print(f"\nClient: {addr[0]}:{addr[1]}")


while True:
    
    cmsg = client.recv(1024).decode()
    print(f"Client-->{cmsg}".rjust(60))
    if cmsg.lower() == 'endofchat':
        print("Client has closed chat session")
        client.close()
        break

    smsg  = input("server-->").encode()
    client.send(smsg)
    if smsg.decode().lower() == 'endofchat':
        print("server has closed chat session")
        client.close()
        break

server.close()
