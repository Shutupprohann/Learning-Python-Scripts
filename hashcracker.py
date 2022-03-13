import hashlib
import pyfiglet

print(pyfiglet.figlet_format('Hashker'))

wordlist_location = str(input('Enter The Wordlist Location: '))
hash_input = str(input('Enter the hash to be cracked: '))
with open(wordlist_location,'r') as file:
	for line in file.readlines():
		hash_ob = hashlib.md5(line.strip().encode()).hexdigest()
		if hash_ob == hash_input:
			print(f'Found cleartext password :{line.strip()}')
			exit()
		