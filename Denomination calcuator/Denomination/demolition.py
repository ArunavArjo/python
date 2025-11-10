from tkinter import*
from tkinter import messagebox
from PIL import image,imageTk

root = Tk()
root.title('Denomination')
root.configure(bg = "light blue")
root.geometry('650x450')
upload = image.open("app_img(1).jpg")
upload = upload.resize((300,300))
Image = ImageTk.photoImage(upload)
label = Label(root , image=image,bg="light blue")
label.place(x = 180,y=20)

label1 = Label(root,
               "Hey User! Welcome to demolition counter application.",
               bg = "light blue"
               )
label1.place(relx = 0.5, y =340, anchor = Center)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert:","Do you want to count demolition?"

    if MsgBox =="ok":
          topwin()

Button1 = Button(root,
                 text = "Let get started",
                 command = msg,
                 bg = 'brown',
                 fg = 'White'
                 )
button1.Place(x = 260,y=360)

    )

