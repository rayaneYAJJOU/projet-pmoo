from tkinter import ttk, Widget
from importlib import util

widgets: dict[str, Widget] = dict()
name: str = "Test"
root = None

"""spec = util.spec_from_file_location("database.py", "src\\database.py")
database = util.module_from_spec(spec)
spec.loader.exec_module(database)
Database = database.Database
database: Database = Database("test", "test.csv")"""


def func(preload: bool = False) -> dict[str, Widget]:

    # Create a frame for better organization
    frame = ttk.Frame(root, padding=20)
    #frame.grid(row=0, column=0, padx=20, pady=20)

    test_label = ttk.Label(root, text = "this is a teeeest")
    #test_label.grid(row=0, column=0, sticky="w")

    if not preload:
        frame.grid(row=0, column=0, padx=20, pady=20)
        test_label.grid(row=0, column=0, sticky="w")

    # Add some padding between widgets
    frame.grid_rowconfigure(3, minsize=20)

    widgets.update({"frame": frame})
    widgets.update({"test_label": test_label})

    return widgets

    # Center the frame in the window
    #root.columnconfigure(0, weight=1)
    #root.rowconfigure(0, weight=1)