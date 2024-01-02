import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk

# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace this with your authentication logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create a themed Tkinter window
root = ThemedTk(theme="equilux")  # You can change the theme to your preference
root.title("Login Page")

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

# Add some padding between widgets
frame.grid_rowconfigure(3, minsize=20)

# Center the frame in the window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Start the Tkinter main loop
root.mainloop()
