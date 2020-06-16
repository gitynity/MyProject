
#abcdefghijklmnopqrstuvwxyz
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#0123456789
#~`!@#$%^&*()-=_+{}[]|\:;"',.<>/
#length atleast 8

import string

special = '~`!@#$%^&*()-=_+{}[]|\:;"\',.<>/'

length = int(input("How many characters long password do you want? "))

if not length or length < 0:
	exit()
import random

password = ''

if length < 4:
	while True:
		password+=random.choice(string.ascii_lowercase)
		length-=1
		if not length:
			break
		password+=random.choice(string.ascii_uppercase)
		length-=1
		if not length:
			break
		password+=random.choice(string.digits)
		length-=1
		if not length:
			break
		password+=random.choice(special)
		length-=1
		if not length:
			break	
	
	print(password)
	
elif length >=4:
	from_each_list = length//4
	remaining = length%4


	for i in range(0,from_each_list):
		password+=random.choice(string.ascii_uppercase)
		password+=random.choice(string.ascii_lowercase)
		password+=random.choice(string.digits)
		password+=random.choice(special)
		

	if remaining and from_each_list:
		for i in range(0,remaining+1):
			password+=random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+special)
	print(password)
