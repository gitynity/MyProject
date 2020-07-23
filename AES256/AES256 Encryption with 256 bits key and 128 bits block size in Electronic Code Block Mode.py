from Crypto.Cipher import AES
from Crypto.Hash import SHA256

password = input("Enter password: ")	#To encrypt the message. AES256 requires that the encryption key to be 256 bits i.e 32 bytes 
hashed_key = SHA256.new(password.encode('utf-8')).digest()	#The password entered might not be 32 bytes long, so we use SHA256 which gives 32 bit hashed_key
															#Now we will use this 32 bit hashed_key to encrypt our message
def shakeme(data):
	msg=data
	bs = 16		#The block size of AES256 is 128 bits. 16 characters or 16 bytes = 128 bits. 
	pad = '*'
	padding = pad*(bs - len(data)%bs)
	padded_msg = msg+padding							#The message might not be completly broken down into 16 bytes blocks.So padding.
	cipher = AES.new(hashed_key,AES.MODE_ECB)			#cipher object of AES256 Electronic Code Block Mode having our hashed_key for encryption
	result = cipher.encrypt(padded_msg.encode('utf-8'))	#utf-8 encoding is neccessary i.e. Mesaage is needed in Byte format 
	return result

cipher_text = shakeme(input("Enter message to encrypt: "))
print("The encrypted text is",cipher_text)

def unshakeme(encrypted_msg):
	msg=encrypted_msg
	pad='*'
	decipher = AES.new(hashed_key,AES.MODE_ECB)
	deciphered_text = decipher.decrypt(msg).decode('utf-8')	#utf-8 encoding is neccessary.
	pad_index = deciphered_text.find(pad)				#finds the index of first pad character
	ans = deciphered_text[:pad_index]
	return ans
	
plain_text = unshakeme(cipher_text)
print("The plain text is",plain_text)

#AES256 Encryption with 256 bits key and 128 bits block size in Electronic Code Block Mode 
