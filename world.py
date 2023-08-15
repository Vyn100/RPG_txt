# Gère les différentes zones, objets interactifs, énigmes.

class Zone:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.enemies = []

    def display(self):
        print(self.name)
        print(self.description)

class Village(Zone):
    def __init__(self):
        super().__init__("Village d'Eldoria", "Un paisible village entouré de forêts et de montagnes.")

    # Vous pouvez ajouter des méthodes spécifiques à cette zone ici.

class Forest(Zone):
    def __init__(self):
        super().__init__("Forêt Mystique", "Une forêt dense et mystérieuse, remplie de dangers cachés.")
