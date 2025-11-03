import tkinter as tk
from tkinter import messagebox

def calculate_product():
    """Reads numbers from the entry fields, calculates the product, and displays it."""
    try:
        # Get input from the entry fields and convert to floats
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Calculate the product
        product = num1 * num2

        # Display the result in the result label
        label_result.config(text=f"Product: {product}")
    except ValueError:
        # Handle cases where the input is not a valid number
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")
        label_result.config(text="Product: Error")

# --- Set up the main application window ---
root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x200") # Set the initial window size

# --- Create and place widgets ---
# Label and Entry for the first number
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

# Label and Entry for the second number
label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Button to trigger the calculation
button_multiply = tk.Button(root, text="Calculate Product", command=calculate_product)
button_multiply.pack(pady=10)

# Label to display the result
label_result = tk.Label(root, text="Product: ", font=("Helvetica", 12, "bold"))
label_result.pack(pady=10)

# --- Run the Tkinter event loop ---
root.mainloop()