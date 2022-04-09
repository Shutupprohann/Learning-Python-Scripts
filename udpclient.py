import socket 

target_addr='vnit.ac.in'
target_port=80

udp_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#udp_client.connect(()
udp_client.send(b"123",(target_addr,target_port))
response=udp_client.recvfrom(4096)
udp_client.close()
print(response)