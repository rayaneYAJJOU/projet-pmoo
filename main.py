# Importation des modules

from tkinter import *
from tkinter import ttk
from application import Application


# Constantes (valeurs par défaut)

TITLE = "Client"
WIDTH = 1080
HEIGHT = 720


# Initialisation

root = Tk()

app = Application(root, title = TITLE, width = WIDTH, height = HEIGHT)


# Boucle principale d'évènements

app.mainloop()