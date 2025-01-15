import tkinter as tk
from views.admin_view import show_admin_login
from views.stock_view import create_stock_frame


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.state('zoomed')
        self.root.title("Kirana Store Management")

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        menubar.add_command(label="STOCK", command=self.show_stock)
        menubar.add_command(label="ADMIN", command=self.show_admin_login)
        menubar.add_command(label="EXIT", command=self.root.quit)
        self.main_frame = tk.Frame(self.root, bg="#FFFFFF")
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_stock(self):
        # Clear the main frame before showing stock
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Add the stock frame
        stock_frame = create_stock_frame(self.main_frame)
        stock_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_admin_login(self):
        def on_admin_login_success():
            self.show_admin_options()

        show_admin_login(self.root, on_admin_login_success)

    def show_admin_options(self):
        # Clear the main frame before showing admin options
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        admin_menu_frame = tk.Frame(self.main_frame, bg="#FFD700")
        admin_menu_frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)

        admin_content_frame = tk.Frame(self.main_frame, bg="#FAFAD2")
        admin_content_frame.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

        options = ["Sales Report", "Stock Report", "User Management", "Stock Entry & Update", "Password Management"]

        for i, option in enumerate(options):
            tk.Button(admin_menu_frame, text=option, font=("Arial", 14), bg="#FFD700",
                      command=lambda opt=option: self.show_admin_option(opt, admin_content_frame)).place(relx=0.05,
                                                                                                         rely=0.1 + i * 0.15,
                                                                                                         relwidth=0.9)

    def show_admin_option(self, option, content_frame):
        """Display content based on selected admin option."""
        for widget in content_frame.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(content_frame, bg="#3CB371")
        header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        tk.Label(header_frame, text=f"{option}", font=("Arial", 24), bg="#3CB371", fg="white").place(relx=0.35,
                                                                                                     rely=0.2)

        # Depending on option, add specific content
        if option == "Sales Report":
            tk.Label(content_frame, text="Sales Report Content", bg="#FAFAD2", font=("Arial", 16)).place(relx=0.1,
                                                                                                         rely=0.2)
        elif option == "Stock Report":
            tk.Label(content_frame, text="Stock Report Content", bg="#FAFAD2", font=("Arial", 16)).place(relx=0.1,
                                                                                                         rely=0.2)
        # Other options can be added here


if __name__ == "main":
    print(__name__)
    root = tk.Tk()
    app = App(root)
    root.mainloop()
