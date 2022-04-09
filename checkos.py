#!/usr/bin/env python3
import os 

def checkos():
	if os.name =='nt':
		operatingsys ='Windows'
	elif os.name == 'posix':
		operatingsys='Linux'
	else:
		operatingsys='Mac'
	return operatingsys

print(checkos())			