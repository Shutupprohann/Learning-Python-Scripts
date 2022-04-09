import sys
import socket
import pyfiglet

print(pyfiglet.figlet_format('Portscanner'))
ip = sys.argv[1]
open_ports = []

port_range  = range(1,1024)

def probe_port(ip,port,result=1):
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((ip,port))
		if r == 0:
			result = r
		sock.close()
	except Exception as e:
		pass
	return result
	
for port in port_range:
	sys.stdout.flush()
	response = probe_port(ip,port)
	if response == 0:
		open_ports.append(port)

if open_ports:
	print('open ports are: ')
	print(sorted(open_ports))
else:
	print('look likes no ports are open :/')							