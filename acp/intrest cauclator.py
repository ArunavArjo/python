import tkinter as tk
from tkinter import messagebox

def calculate_simple_interest():
    """Calculates simple interest based on user inputs."""
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        if principal < 0 or time < 0 or rate < 0:
            messagebox.showerror("Input Error", "Please enter positive values for all fields.")
            return

        simple_interest = (principal * time * rate) / 100
        result_label.config(text=f"Simple Interest: {simple_interest:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

def clear_fields():
    """Clears all input fields and the result."""
    principal_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    result_label.config(text="Simple Interest: ")

# Create the main application window
app = tk.Tk()
app.title("Simple Interest Calculator")

# Create labels and entry fields for inputs
tk.Label(app, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
principal_entry = tk.Entry(app)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Time Period (Years):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
time_entry = tk.Entry(app)
time_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
rate_entry = tk.Entry(app)
rate_entry.grid(row=2, column=1, padx=10, pady=5)

# Create buttons
calculate_button = tk.Button(app, text="Calculate", command=calculate_simple_interest)
calculate_button.grid(row=3, column=0, columnspan=1, padx=10, pady=10)

clear_button = tk.Button(app, text="Clear", command=clear_fields)
clear_button.grid(row=3, column=1, columnspan=1, padx=10, pady=10)

# Create label to display the result
result_label = tk.Label(app, text="Simple Interest: ", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
app.mainloop()