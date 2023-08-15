# Fichier principal pour exécuter le jeu.
import random 
from inventory import display_inventory
from characters import Player
from events import encounter_enemy, find_treasure
from quests import EliminateWolves

def main_menu():
    print("Le Destin d'Eldoria")
    print("1. Nouvelle partie")
    print("2. Charger une partie")
    print("3. Quitter")
    
    choix = input("Choisissez une option : ")

    if choix == "1":
        start_new_game()
    elif choix == "2":
        load_game()
    elif choix == "3":
        exit_game()
    else:
        print("Choix invalide. Veuillez essayer à nouveau.")
        main_menu()

def start_new_game():
    print("\nVotre aventure commence...")
    player_name = input("Entrez le nom de votre personnage : ")
    player = Player(player_name)
    
    print(f"\nBienvenue, {player.name}! Votre quête commence maintenant...")

    # Assigner une quête au joueur
    quest = EliminateWolves()

    while player.is_alive():
        action = input("\nQue voulez-vous faire? (Explorer / Inventaire / Quête / Quitter) ").lower()

        if action == "explorer":
            event = random.choice([encounter_enemy, find_treasure])
            event(player)
            if event == encounter_enemy:
                quest.update()
        elif action == "inventaire":
            display_inventory(player)
        elif action == "quête":
            print(quest.description)
        elif action == "quitter":
            print("Au revoir !")
            break

        if not player.is_alive():
            player.revive()


def load_game():
    # Cette fonction sera développée plus tard pour gérer le chargement des sauvegardes.
    print("Fonctionnalité à venir...")

def exit_game():
    print("Merci d'avoir joué ! À bientôt.")
    exit()

if __name__ == "__main__":
    main_menu()
