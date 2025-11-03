from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry('400x300')

def msg():
    messagebox.showwarning("Alert","Stop virus Found!")

button = Button(root, text="Scan for virus",command=msg)
button.place(x=40,y=80)

root.mainloop()