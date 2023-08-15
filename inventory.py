# Gère l'inventaire et les objets du joueur.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Potion(Item):
    def __init__(self, name, description, healing_amount):
        super().__init__(name, description)
        self.healing_amount = healing_amount

    def use(self, character):
        character.health += self.healing_amount
        if character.health > character.max_health:
            character.health = character.max_health
        print(f"\n{character.name} utilise {self.name} et restaure {self.healing_amount}HP!")

def display_inventory(player):
    while True:  # Nous lançons une boucle pour que l'utilisateur puisse continuer à interagir avec l'inventaire jusqu'à ce qu'il décide d'en sortir.
        print("\nInventaire :")
        if not player.inventory:
            print("Votre inventaire est vide.")
            break

        for index, item in enumerate(player.inventory, 1):  # Nous utilisons enumerate pour obtenir un index pour chaque objet, en commençant à 1.
            print(f"{index}. {item.name}: {item.description}")

        print("0. Retour")  # Option pour quitter l'inventaire

        choice = input("Sélectionnez un objet à utiliser ou '0' pour quitter: ")
        
        if choice == "0":
            break  # Sortir de la boucle et donc de l'inventaire

        if choice.isdigit() and 0 < int(choice) <= len(player.inventory):  # Vérifie que le choix est valide
            item_to_use = player.inventory[int(choice) - 1]  # -1 car les listes sont indexées à partir de 0

            # Vérification du type d'objet pour déterminer l'action appropriée
            if isinstance(item_to_use, Potion):
                item_to_use.use(player)
                player.inventory.remove(item_to_use)  # Supprime la potion après utilisation
        else:
            print("Choix invalide. Veuillez réessayer.")
