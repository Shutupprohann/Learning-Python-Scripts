import socket
import argparse
import sys 


target_host="127.0.0.1"
target_port=8888

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))

client.send(b"how are you!")
response=client.recv(4096)
client.close()
print(response)
