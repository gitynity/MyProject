import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


password_provided = input("Enter the password based on which a key will be generated using SHA256 : ")	
#keep the password same to get the same key

password = password_provided.encode()	#convert string to bytes

salt_text = input("Enter salt which will be used for key generation using SHA256 :")
salt = salt_text.encode()		#salt_text was in string format , we encoded it into byte form, because salt is needed in byte format

#keep the salt same to get the same key ; b in the front of string to convert string to byte form

kdf = PBKDF2HMAC(
algorithm = hashes.SHA256(),	# Here I am using SHA256 algorithm
length = ,			# Here put a number what you like , but keep them same to get the same key. Put a multiple of 8 , say 32.
salt=salt,
iterations = ,	# Here put a number what you like , but keep them same to get the same key. Put some large number , say 100000
backend = default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))	#Can only use kdf once

print(key)		#key generated

with open('key.key','wb') as file:
	file.write(key)					#key written in byte format

with open('to_encrypt.txt','rb') as file:
	message = file.read()			#message read in byte format


f = Fernet(key)		#Fernet object with key created

encrypted = f.encrypt(message)		#message which was encoded in byte form is now encrypted
print(encrypted)

with open('encrypted_text.txt','wb') as file:
	file.write(encrypted)					#encrypted message is now written in byte format
