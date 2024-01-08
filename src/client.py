class Client:
    """Classe pour un client/utilisateur de l'application"""

    ROLES: list[str] = ["Administrateur", "Enseignant", "Étudiant"]
    """Les rôles possibles"""
    
    def __init__(self, id: int = 0, perm: int = -1) -> None:

        # Initialisation
        self.__id = id
        self.__perm = perm


    # Getters/Setters

    def get_id(self) -> int:
        return self.__id

    def get_perm_level(self) -> int:
        return self.__perm
    
    def get_perm_name(self) -> str:
        return Client.ROLES[self.__perm] if 0 <= self.__perm <= 2 else "Néant"