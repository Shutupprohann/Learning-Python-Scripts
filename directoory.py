import requests
import sys
import pyfiglet

print(pyfiglet.figlet_format('Directoory'))
sub_list = open('wordlist2.txt').read()
directories = sub_list.splitlines()

for dir in directories:
	dir_enum = f'http://{sys.argv[1]}/{dir}.html'
	r = requests.get(dir_enum)
	if r.status_code==404:
		pass

	else:
		print('valid directory:',dir_enum)
