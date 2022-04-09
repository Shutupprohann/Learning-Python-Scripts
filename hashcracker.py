import hashlib
import pyfiglet
import sys

print(pyfiglet.figlet_format('Hashker'))

wordlist_location = str(input('Enter The Wordlist Location: '))
hash_input = str(input('Enter the hash to be cracked: '))
hash_type = str(input('Enter the type of hash[md5,sha256,sha512]:'))

def md5():
		with open(wordlist_location,'r') as file:
			for line in file.readlines():
				gen_hash = hashlib.md5(line.strip().encode()).hexdigest()
				if gen_hash==hash_input:
					return f'plaintext value : {line.strip()}'


def sha256():
	with open(wordlist_location,'r') as file:
		for line in file.readlines():
			gen_hash = hashlib.sha256(line.strip().encode()).hexdigest()
			if gen_hash==hash_input:
				return f'plaintext value : {line.strip()}'


def sha512():
	with open(wordlist_location,'r') as file:
		for line in file.readlines():
			gen_hash = hashlib.sha512(line.strip().encode()).hexdigest()
			if gen_hash==hash_input:
				return f'plaintext value : {line.strip()}'


if hash_type=='md5':
	print(md5())

elif hash_type == 'sha256':
	print(sha256())

elif hash_type=='sha512':
	print(sha512())
