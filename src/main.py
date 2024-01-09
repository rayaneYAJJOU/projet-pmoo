# Importation des modules

from ttkthemes import ThemedTk as TTk
from application import Application
from page_handler import PageHandler
from database import Database


# Constantes (valeurs par défaut)

TITLE: str = "Client"
WIDTH: int = 1080
HEIGHT: int = 720


# Initialisation

def main():

    root = TTk(theme = "equilux")

    PageHandler.load_page(root, "login.py")

    app: Application = Application(root, title = TITLE, width = WIDTH, height = HEIGHT)

    # Boucle principale d'évènements
    app.mainloop()


if __name__ == "__main__":
    main()