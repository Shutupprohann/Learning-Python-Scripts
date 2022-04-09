import socket
import threading 

ip='127.0.0.1'
port=8888

def main():
    try:

        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((ip,port))
        server.listen(5)
        print("[*] listening on {0}:{1}".format(ip,port))

        def handle_client(client_socket):
             with client_socket as sock:
                request=sock.recv(4096)
                print('[*] Received:{0}'.format(request.decode("utf-8")))
                sock.send(b'ACK')

        while True:
           client, address = server.accept() 
           print(f'[*] Accepted connection from {address[0]}:{address[1]}')
           client_handler = threading.Thread(target=handle_client, args=(client,))
           client_handler.start() 


    except KeyboardInterrupt:
        print("[*] User Interrupted,Quiting..")
main()          