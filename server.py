import socket

server_sock = socket.socket(socket.AF_INET,     
                            socket.SOCK_STREAM,  
                            proto=0)             
print(type(server_sock))                         