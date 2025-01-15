import tkinter as tk
from kirana_store.controllers.product_controller import add_new_product, fetch_products

def open_product_management_window():
    root = tk.Tk()
    root.title("Kirana Store - Product Management")

    tk.Label(root, text="Product Name").grid(row=0)
    tk.Label(root, text="Stock").grid(row=1)
    tk.Label(root, text="Price").grid(row=2)
    
    product_name = tk.Entry(root)
    stock = tk.Entry(root)
    price = tk.Entry(root)
    
    product_name.grid(row=0, column=1)
    stock.grid(row=1, column=1)
    price.grid(row=2, column=1)
    
    def handle_add_product():
        add_new_product(product_name.get(), stock.get(), price.get())
        refresh_product_list()

    tk.Button(root, text="Add Product", command=handle_add_product).grid(row=3, columnspan=2)
    
    # Display the list of products
    product_list = tk.Listbox(root)
    product_list.grid(row=4, columnspan=2)
    
    def refresh_product_list():
        product_list.delete(0, tk.END)
        for product in fetch_products():
            product_list.insert(tk.END, f"{product[1]} (Stock: {product[2]}, Price: {product[3]})")

    refresh_product_list()
    root.mainloop()
