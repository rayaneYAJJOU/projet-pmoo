from tkinter import messagebox
from tkinter import ttk, Widget
from importlib import util

widgets: dict[str, Widget] = dict()
name: str = "Login"
root = None

spec = util.spec_from_file_location("database.py", "src\\database.py")
database = util.module_from_spec(spec)
spec.loader.exec_module(database)
Database = database.Database

db: Database = Database("test", "test.csv")

spec = util.spec_from_file_location("page_handler.py", "src\\page_handler.py")
page_handler = util.module_from_spec(spec)
spec.loader.exec_module(page_handler)
PageHandler = page_handler.PageHandler


def login() -> None:
    username: str = widgets["username_entry"].get()
    password: str = widgets["password_entry"].get()

    if db.contains(Username = lambda x : x == username, Password = lambda x : x == password):
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        PageHandler.load_page("testpage.py")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def func(preload: bool = False) -> None:

    # Create a frame for better organization
    frame = ttk.Frame(root, padding=20)
    #frame.grid(row=0, column=0, padx=20, pady=20)

    # Create themed labels, entry fields, and a login button with grid layout
    username_label = ttk.Label(frame, text="Username:")
    #username_label.grid(row=0, column=0, sticky="w")

    username_entry = ttk.Entry(frame)
    #username_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, ipady=5)

    password_label = ttk.Label(frame, text="Password:")
    #password_label.grid(row=1, column=0, sticky="w")

    password_entry = ttk.Entry(frame, show="*")  # The password is hidden with asterisks
    #password_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=10, ipady=5)

    login_button = ttk.Button(frame, text="Login", command=login)
    #login_button.grid(row=2, columnspan=2, pady=10)

    if not preload:
        frame.grid(row=0, column=0, padx=20, pady=20)
        username_label.grid(row=0, column=0, sticky="w")
        username_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, ipady=5)
        password_label.grid(row=1, column=0, sticky="w")
        password_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=10, ipady=5)
        login_button.grid(row=2, columnspan=2, pady=10)

    #test = ttk.Button(frame, text="click lol", command=clear)
    #test.grid(row=3, column=3)

    # Add some padding between widgets
    frame.grid_rowconfigure(3, minsize=20)

    widgets.update({"frame": frame})
    widgets.update({"username_label": username_label})
    widgets.update({"username_entry": username_entry})
    widgets.update({"password_label": password_label})
    widgets.update({"password_entry": password_entry})
    widgets.update({"login_button": login_button})
    #widgets.update({"test": test})

    # Center the frame in the window
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)