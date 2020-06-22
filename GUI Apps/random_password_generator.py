import string
import random

import tkinter as tk

import tkinter.simpledialog

from tkinter import messagebox

password = ''

class CustomDialog(tk.simpledialog.Dialog):		#class to create a custom dialog-box which is copiable and editable

    def __init__(self, parent, title=None, text=None):
        self.data = text
        tk.simpledialog.Dialog.__init__(self, parent, title=title)

    def body(self, parent):
        self.text = tk.Text(self, width=40, height=4)
        self.text.pack(fill="both", expand=True)
        self.text.insert("1.0", self.data)
        return self.text

def show_dialog():
	some_text = "Your password is : "
	CustomDialog(root, title="Password", text=some_text+password)


root = tk.Tk()	#start of window
#{
root.geometry("300x400")
root.title("First Python GUI App")

mylabel = tk.Label(root,text="What will be the length of your password? ")
mylabel.pack()

entrybox = tk.Entry(root)
entrybox.pack()


special = '~`!@#$%^&*()-=_+{}[]|\:;"\',.<>/'

def password_generator():

	global password

	length = int(entrybox.get())
	#print(length)	-->successful

	if length < 1:
		exit()

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
			
			password+=random.choice(special)
			length-=1
			if not length:
				break	
	
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
#	messagebox.showinfo("Password",password)
	show_dialog()		
mybutton = tk.Button(root,text="Enter",command=password_generator)
mybutton.pack()


#}
root.mainloop()	#end of window
