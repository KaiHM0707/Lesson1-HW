from tkinter import *
scr = Tk()
scr.title("Repl.it")
scr.geometry("600x600")


create = Button(scr, text="Create repl", bg="lightblue")
pick = Button(scr, text="Pick a template", bg="gray")
template = Button(scr, text="Template: Python",)
Project_name = Entry(scr, width=30).place(x=50,y=30)

create.pack(side="bottom")
pick.pack(side="left")
template.pack(side="top")


scr.mainloop()










