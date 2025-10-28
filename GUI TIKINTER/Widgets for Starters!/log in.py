from tkinter import*
root = Tk()
root.title('Log in app')
root.geometry('400x300')
frame = Frame(master = root, height = 200,width = 360,bg = '#de0efff')

lbl1 = Label(frame,text = "Full Name",bg = '#3895D3',fg = 'white',width=12)
lbl1 = Label(frame,text = "Email Id",bg = '#3895D3',fg = 'white',width=12)
lbl1 = Label(frame,text = "Entwr Password",bg = '#3895D3',fg = 'white',width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame,show="*")

def display():
    name = name_entry.get()
    greet = "Hey"+name
    message = "\n Congratulations for your new account"
    textbox.insert(End,greet)
    textbox.insert(End,message)

textbox = Text(bg = "#BEBEBE",fg='black')


btn = Button( Text = "Create account",command = display,bg = 'red')

frame.place(x = 40,y = 20)
lbl1.place(x=40,y=40)
name_entry.place(x = 76,y = 20)
lbl2.place(x=60,y=90)
email_entry.place(x = 39,y = 63)
lbl3.place(x=90,y=80)
pass_entry.place(x = 78,y=59)
btn.place(x = 130,y = 210)
textbox.place(y = 250)

root.mainloop()