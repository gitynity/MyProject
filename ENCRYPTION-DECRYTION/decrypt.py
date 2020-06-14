from cryptography.fernet import Fernet

with open('key.key','rb') as file:
	read_key = file.read()			#key is read from the file key.key

f = Fernet(read_key)		#Fernet object with read_key created

with open('encrypted_text.txt','rb') as file:
	encrypted_text = file.read()			#encrypted_text is read which is in byte form

	
decrypted = f.decrypt(encrypted_text)
print(decrypted)

with open('decrypted_text.txt','wb') as file:
	file.write(decrypted)			
