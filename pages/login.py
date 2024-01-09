from tkinter import messagebox
from tkinter import ttk, Widget
from importlib import util
from time import sleep

widgets: list[Widget] = []
name: str = "Login"

spec = util.spec_from_file_location("database.py", "src\\database.py")
database = util.module_from_spec(spec)
spec.loader.exec_module(database)
Database = database.Database

def func(root, page):

    db: Database = Database("test", "test.csv")

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if db.contains(Username = lambda x : x == username, Password = lambda x : x == password):
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    # Create a frame for better organization
    frame = ttk.Frame(root, padding=20)
    frame.grid(row=0, column=0, padx=20, pady=20)

    # Create themed labels, entry fields, and a login button with grid layout
    username_label = ttk.Label(frame, text="Username:")
    username_label.grid(row=0, column=0, sticky="w")

    username_entry = ttk.Entry(frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, ipady=5)

    password_label = ttk.Label(frame, text="Password:")
    password_label.grid(row=1, column=0, sticky="w")

    password_entry = ttk.Entry(frame, show="*")  # The password is hidden with asterisks
    password_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=10, ipady=5)

    login_button = ttk.Button(frame, text="Login", command=login)
    login_button.grid(row=2, columnspan=2, pady=10)

    #test = ttk.Button(frame, text="click lol", command=clear)
    #test.grid(row=3, column=3)

    # Add some padding between widgets
    frame.grid_rowconfigure(3, minsize=20)

    widgets.append(frame)
    widgets.append(username_label)
    widgets.append(username_entry)
    widgets.append(password_label)
    widgets.append(password_entry)
    widgets.append(login_button)
    #widgets.append(test)

    # Center the frame in the window
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)