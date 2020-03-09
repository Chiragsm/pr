from tkinter import Tk, StringVar,ttk
from tkinter import *
import time
import tkinter.messagebox

class Convert:
	def _init_(self, root):
		self.root = root
		self.root.title("Currancy Converter")
		self.root.geometry("1350x800+0+0")
		self.root.configure(background='Gray')


		TitleFrame = Frame(self.root, bd=10, width=1350, height=100, padx=10,pady=10, bg="Gray", relief=RIDGE)
		TitleFrame.grid(row=0,column=0)

		self.lblTitle=Label(TitleFrame, text= "Currency Converter", padx=17, pady=4, bd=1, font=('arial',30,'bold'), bg="sky blue",width =50)
		MainFrame = Frame(self.root, bd=10, width=1350, height=700, padx=11,pady=10, bg="Gray", relief=RIDGE)
		MainFrame.grid(row=1,column=0)


		if _name_=='_main':
			root = Tk()
			application = Convert(root)
			root.mainloop()