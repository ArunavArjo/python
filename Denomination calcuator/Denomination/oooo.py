from tkinter import Tk, Label, Button, messagebox, CENTER
from PIL import Image, ImageTk


root = Tk()
root.title("Denomination Counter")  
root.configure(bg="light blue")
root.geometry("650x450")


try:
    upload = Image.open("app_img(1).jpg")
    upload = upload.resize((300, 300))
    image_tk = ImageTk.PhotoImage(upload)  
    label = Label(root, image=image_tk, bg="light blue")
    label.place(x=180, y=20)
except FileNotFoundError:
    messagebox.showerror("Error", "Image 'app_img(1).jpg' not found. Please ensure it's in the same directory.")
    image_tk = None 

label1 = Label(root, text="Hey User! Welcome to denomination counter application.", bg="light blue")
label1.place(relx=0.5, y=340, anchor=CENTER)


def msg():
    MsgBox = messagebox.askyesno("Alert:", "Do you want to count denominations?") # 
    if MsgBox:  
        topwin() 
button1 = Button(root, text="Let's get started", command=msg, bg="brown", fg="White")
button1.place(x=260, y=360)


root.mainloop()