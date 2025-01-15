from tkinter import *
from tkinter import ttk


def main():
    master = Tk()
    app = LoginPage(master)
    master.mainloop()


class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1300x700+0+0")
        self.master.title("Restaurant  Management System")

        # TITLE LABEL:
        self.title_label = Label(self.master, text="Restaurant  Management System", font=("Arial", 32, "bold"),
                                 bg="LightGrey", bd=8, relief=GROOVE)
        self.title_label.pack(side=TOP, fill=X)

        # Login Frame
        self.login_Frame = Frame(self.master, bg="lightGreen", bd=6, relief=GROOVE)
        self.login_Frame.place(x=180, y=150, width=900, height=400)

        # Login Label:
        self.login_label = Label(self.login_Frame, text="Login", bd=6, relief=GROOVE, font=("Arial", 25, "bold"))
        self.login_label.pack(side=TOP, fill=X)

        # Entry Frame:
        self.entry_frame = LabelFrame(self.login_Frame, text='Detail Entry', bd=6, relief=GROOVE, font=("Arial", 10))
        self.entry_frame.pack(fill=BOTH, expand=True)

        # Entry Label
        self.user_label = Label(self.entry_frame, text="user name", font=('Arial', 12, 'bold'))
        self.user_label.grid(row=0, column=0, padx=2, pady=5)
        self.password_label = Label(self.entry_frame, text="password", font=('Arial', 12, 'bold'))
        self.password_label.grid(row=1, column=0, padx=2, pady=5)

        #==================== Variables ==================================
        username = StringVar() 
        password = StringVar()

        #-----------------------------------------------------------------

        # Entry Text
        self.user_entry = Entry(self.entry_frame, font=('Arial', 10), bd=2, textvariable=username)
        self.user_entry.grid(row=0, column=1, padx=2, pady=5)
        self.password_entry = Entry(self.entry_frame, font=('Arial', 10), show='*', bd=2, textvariable=password)
        self.password_entry.grid(row=1, column=1, padx=2, pady=5)

        # Button Frame:
        self.btn_frame = Frame(self.entry_frame, bd=2, bg='Light Blue', relief=GROOVE)
        self.btn_frame.place(x=5, y=90, height=40, width=300)

        # Button:
        self.login_btn = Button(self.btn_frame, text='login', bd=2, relief=GROOVE)
        self.login_btn.grid(column=0, row=0, padx=2, pady=2)
        self.billing_btn = Button(self.btn_frame, text='Billing', bd=2, relief=GROOVE)
        self.billing_btn.grid(column=1, row=0, padx=2, pady=2)
        self.billing_btn.config(state='disabled')
        self.cancel_btn = Button(self.btn_frame, text='login', bd=2, relief=GROOVE)
        self.cancel_btn.grid(column=3, row=0, padx=2, pady=2)


if __name__ == "__main__":
    main()
