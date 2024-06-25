from tkinter import *

a = Tk()
a.title("I dont like homeworks")
a.geometry("500x500")
a.configure(background="black")

bt1 = Button(a, text="Button1")
bt1.pack(side="top")

bt2 = Button(a, text="Button2")
bt2.pack(side="right")

bt3 = Button(a, text="Button3")
bt3.pack(side="bottom")

bt4 = Button(a, text="Button4")
bt4.pack(side="left")

a.mainloop()
