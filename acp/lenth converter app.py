import tkinter as tk
from tkinter import messagebox

def convert_inches_to_cm():
    """Converts the input inches to centimeters and displays the result."""
    try:
        inches = float(entry_inches.get())
        if inches < 0:
            messagebox.showerror("Invalid Input", "Length cannot be negative.")
            return
        centimeters = inches * 2.54
        result_label.config(text=f"{inches} inches is equal to {centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for inches.")


root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x150") 


label_inches = tk.Label(root, text="Enter length in inches:")
label_inches.pack(pady=10)


entry_inches = tk.Entry(root, width=20)
entry_inches.pack(pady=5)


convert_button = tk.Button(root, text="Convert", command=convert_inches_to_cm)
convert_button.pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=5)


root.mainloop()