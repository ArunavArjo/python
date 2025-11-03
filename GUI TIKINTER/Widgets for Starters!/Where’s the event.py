from tkinter import*
root = Tk()
root.title('Event Handler')
root.geometry('100x100')
def handle_keypress(event):
        print(event.char)


root.bind("<Key>",handle_keypress)

def handle_click(event):
        print("\n button was clicked")

button = Button(text="Click me!")
button.pack()
button.bind("<Button-1>",handle_click)

root.mainloop()