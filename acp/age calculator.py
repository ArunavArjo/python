import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def display_dob():
    """Retrieves the date of birth from input fields and displays it."""
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        # Validate date components
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= datetime.now().year):
            messagebox.showerror("Error", "Invalid date components. Please enter valid day, month, and year.")
            return

        # Attempt to create a datetime object to validate the full date
        try:
            birth_date = datetime(year, month, day)
            result_label.config(text=f"Your Date of Birth: {birth_date.strftime('%d/%m/%Y')}")
        except ValueError:
            messagebox.showerror("Error", "Invalid date of birth. Please ensure the day, month, and year form a valid date.")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for day, month, and year.")

# Create the main application window
root = tk.Tk()
root.title("Date of Birth Input")

# Create labels and entry fields for day, month, and year
day_label = tk.Label(root, text="Day:")
day_label.grid(row=0, column=0, padx=5, pady=5)
day_entry = tk.Entry(root)
day_entry.grid(row=0, column=1, padx=5, pady=5)

month_label = tk.Label(root, text="Month:")
month_label.grid(row=1, column=0, padx=5, pady=5)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1, padx=5, pady=5)

year_label = tk.Label(root, text="Year:")
year_label.grid(row=2, column=0, padx=5, pady=5)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a button to submit the date
submit_button = tk.Button(root, text="Display Date of Birth", command=display_dob)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the Tkinter event loop
root.mainloop()