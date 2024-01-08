from tkinter import ttk
from ttkthemes import ThemedTk as TTk

root = TTk()
root.title("Hi")

username_label = ttk.Label(None, text="Username:")
username_label.grid(row=0, column=0, sticky="w")

username_entry = ttk.Entry(None)
username_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, ipady=5)

root.mainloop()