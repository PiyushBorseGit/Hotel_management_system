import tkinter as tk
from tkinter import *
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

# Global Menu Dictionary
menu = {
    "Pizza": 100,
    "Pasta": 100,
    "Burger": 50,
    "Coffee": 30
}

# Admin Panel Function
def admin():
    aw = tk.Toplevel()
    aw.title("Admin Panel")
    aw.configure(bg="white")

    tk.Label(aw, text="ADMIN PANEL", bg="royalblue", fg="white",
             font="Arial 16 bold", padx=10, pady=10).pack(padx=20, pady=20)

    def add_dish():
        dishname = dish_name.get()
        try:
            dishprice = int(dish_price.get())
            menu[dishname] = dishprice
            print("Updated Menu:", menu)
        except ValueError:
            print("Please enter a valid price.")

    tk.Label(aw, text="Dish Name").pack()
    dish_name = tk.Entry(aw)
    dish_name.pack()

    tk.Label(aw, text="Dish Price").pack()
    dish_price = tk.Entry(aw)
    dish_price.pack()

    tk.Button(aw, text="Add Dish", command=add_dish).pack(pady=10)

# Customer Order Function
def order():
    ow = tk.Toplevel()
    ow.title("Order Please!!!")
    ow.configure(bg="white")

    tk.Label(ow, text="Order Please", bg="royalblue", fg="white",
             font="Arial 16 bold", padx=10, pady=10).pack(padx=20, pady=20)

    selections = {}

    for dish, price in menu.items():
        var = tk.BooleanVar()
        selections[dish] = var
        tk.Checkbutton(ow, text=f"{dish} - Rs. {price}", variable=var).pack(anchor='w', padx=20)

    def place_order():
        total = sum(price for dish, var in selections.items() if var.get() for name, price in menu.items() if name == dish)
        Label(ow, text=f"Total Bill: Rs. {total}").pack()

    def receipt():
        doc = SimpleDocTemplate("receipt.pdf", pagesize=A4)
        elements = []

        data = [["Dish", "Price (Rs.)"]]
        total = 0
        for key, value in selections.items():
            if value.get():
                data.append([key, str(menu[key])])
                total += menu[key]

        if len(data) == 1:
            data.append(["No items selected", ""])

        data.append(["Total", str(total)])

        table = Table(data, colWidths=[200, 100])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
            ('BACKGROUND', (0, -1), (-1, -1), colors.yellow),
            ('TEXTCOLOR', (0, -1), (-1, -1), colors.black),
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold')
        ]))
        
        img = Image("thankyou.jpg", width=400, height=150)
        elements.append(img)

        elements.append(table)

        
        
        
            
            
     

        doc.build(elements)

    def multitask():
        place_order()
        receipt()

    tk.Button(ow, text="Place Order", command=multitask, bg="green", fg="white").pack(pady=20)

# Main Window Setup
frame = tk.Tk()
frame.title("Paras Hotel")
frame.configure(bg="white")
frame.geometry("300x400")

tk.Label(frame, text="PARAS HOTEL", bg="royalblue", fg="white",
         font="Arial 16 bold", padx=10, pady=10).pack(pady=(20, 10))

tk.Label(frame, text="MENU", bg="royalblue", fg="white",
         font="Arial 10 bold", padx=10, pady=5).pack(pady=(10, 5))

for item, price in menu.items():
    tk.Label(frame, text=f"{item:<10} Rs. {price}", bg="lightgray",
             fg="black", font="Arial 9", padx=10, pady=5, anchor="w").pack(fill='x', padx=50, pady=2)

tk.Button(frame, text="Admin", command=admin,
          bg="royalblue", fg="white", font="Arial 10 bold").pack(pady=10, padx=20, fill='x')

tk.Button(frame, text="Order", command=order,
          bg="royalblue", fg="white", font="Arial 10 bold").pack(pady=10, padx=20, fill='x')

tk.Button(frame, text="Close", command=frame.destroy,
          bg="royalblue", fg="white", font="Arial 10 bold").pack(pady=10, padx=20, fill='x')

frame.mainloop()
