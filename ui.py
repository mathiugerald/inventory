import tkinter as tk
from tkinter import messagebox
import auth
import inventory
import reports

def login_window():
    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()

        if auth.authenticate_user(username, password):
            open_main_window()
            login_window.destroy()
        else:
            messagebox.showerror("Login failed", "Invalid credentials")

    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Password").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    tk.Button(login_window, text="Login", command=attempt_login).pack()

    login_window.mainloop()

def open_main_window():
    main_window = tk.Tk()
    main_window.title("Inventory Tracking System")

    def add_item_window():
        add_window = tk.Toplevel(main_window)
        add_window.title("Add Item")

        tk.Label(add_window, text="Item Name").pack()
        item_name_entry = tk.Entry(add_window)
        item_name_entry.pack()

        tk.Label(add_window, text="Category").pack()
        category_entry = tk.Entry(add_window)
        category_entry.pack()

        tk.Label(add_window, text="Quantity").pack()
        quantity_entry = tk.Entry(add_window)
        quantity_entry.pack()

        tk.Label(add_window, text="Price").pack()
        price_entry = tk.Entry(add_window)
        price_entry.pack()

        tk.Label(add_window, text="Supplier").pack()
        supplier_entry = tk.Entry(add_window)
        supplier_entry.pack()

        def submit_item():
            item_name = item_name_entry.get()
            category = category_entry.get()
            quantity = int(quantity_entry.get())
            price = float(price_entry.get())
            supplier = supplier_entry.get()

            inventory.add_item(item_name, category, quantity, price, supplier)
            messagebox.showinfo("Success", "Item added successfully")
            add_window.destroy()

        tk.Button(add_window, text="Add Item", command=submit_item).pack()

    def display_inventory_window():
        inventory_data = inventory.display_inventory()
        display_window = tk.Toplevel(main_window)
        display_window.title("Inventory Data")

        text_box = tk.Text(display_window)
        text_box.pack()

        for index, row in inventory_data.iterrows():
            text_box.insert(tk.END, f"{row['item_id']}: {row['item_name']} | Quantity: {row['quantity']}\n")

    tk.Button(main_window, text="Add Item", command=add_item_window).pack()
    tk.Button(main_window, text="Display Inventory", command=display_inventory_window).pack()

    main_window.mainloop()

login_window()


