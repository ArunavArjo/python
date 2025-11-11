import tkinter as tk
from tkinter import ttk,messagebox

class ResturantOrderManegment:
    def __init__(self,root):
        self.root = root
        self.root.title(
            "Resturant manegment app"
        )

        self.menu_items={
            "French fries" : 2,
            "Lunch Meal": 2,
            "Burger Meal": 3,
            "Pizza Meal": 4,
            "ChesseBurger Meal":5,
            "Drinks":1
        }

        self.exchange_rate=82
        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,
                    anchor=tk.CENTER)
        
        ttk.Label(frame,
                  text="Resturant Order Manegment"      
                   font = ("Arial",20,"bold")).grid(
                                                    row = 0,
                                                    columnspan = 3,
                                                    padx = 10,
                                                    pady = 10
                   )
        self.menu_labels = {}
        self.quantites = {}

        for i,(item,price) in enumerate(self.menu_items.items(), start = 1):
            label = ttk.Label(frame,
                              text=f"{item } (${price}):",
                              font = ("Arial",12))


            label.grid(row = 1,column=0,padx=10,pady=5)
            self.menu_labels[item] = label


            quantity_entry = ttk.Entry(frame,width=5)
            quantity_entry.grid (row = 1,column=0,padx=10,pady=5)
            self.menu_quantities[item ] = quantity_entry


            self.currency_var = tk.StringVar()
            ttk.Label(frame,text="Currency:",
                font = ("Arial",12)).grid (row=len(self.menu_items)+1,
                                            column=0,
                                            padx=10, 
                                            pady=5) 
            currency_dropdown = ttk.Combobox(frame,
                                             textvariable=self.currency_var,
                                             state="readonly",
                                             width=18
                                             values=("USD","INR")

            )  

            currency_dropdown.grid(row=len(self.menu_items))+1,
                                   column = 1,
                                   padx = 10,
                                   pady = 5
            currency_dropdown.current(0)
            self.currency_var.trace('w',self.update_menu_prices)


            order_button = ttk.Button(
                                    frame,
                                    text="Place order",
                                    command=self.place_order)
            order_button.grid(row = len(self.menu_items)+2,
            columnspan = 3,
            padx = 10,
            pady = 5)


    def setup_background(self,root):
        bg_width,bg_height = 800,400
        canvas = tk.Canvas(root,width=bg_width,height=bg_height)
        canvas.pack()
        orignal_image = tk.PhotoImage(file = "food.jpg")
        food_image = orignal_image.subsample(
            orignal_image.width()// bg_width,
            orignal_image.height()// bg_height)
        canvas.create_image(0,0, anchor = tk.NW, image = food_image)
        canvas.image = food_image
    
    def update_menu_prices(self,*args):
            currency = self.currency_var.get()
            symbol = "$" if currency == "INR" else "$"
            rate = self.exchange_rate if currency == "INR" else 1

            for item, entry in self.menu_quantites.items():
                    quantity = entry.get()
                    if quantity.isdigit():
                            quantity = int(quantity)
                            price = self.menu_items[item]*rate
                            total_cost += cost
                            if quantity > 0:
                                    order_summary += f"{item}:{quantity} x {symbol}{price} = {symbol}{cost}"
                                    messagebox.showinfo(
                                            "order placed",
                                            order_summary
                                    )
                            else:
                                    messagebox.showerror("Erron","Please order atleast one item.")
