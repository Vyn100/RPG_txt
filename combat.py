# Gère le système de combat.
import random
from characters import Player, Enemy

def start_combat(player, enemy):
    print(f"Un {enemy.name} sauvage apparaît !")
    
    while player.is_alive() and enemy.is_alive():
        print(f"{player.name}: {player.health}HP | {enemy.name}: {enemy.health}HP")
        action = input("Que voulez-vous faire? (Attaquer / Fuir) ")

        if action.lower() == "attaquer":
            damage = player.strength - (0.5 * enemy.defense)
            enemy.take_damage(damage)
            print(f"Vous avez infligé {damage} dégâts à {enemy.name}!")
            
            if enemy.is_alive():
                damage = enemy.strength - (0.5 * player.defense)
                player.take_damage(damage)
                print(f"{enemy.name} vous a infligé {damage} dégâts!")
            else:
                exp_gain = random.randint(20, 50)  # Experience gagné entre 20 et 50 points
                player.gain_experience(exp_gain)
                gold_gain = random.randint(5, 20)  # Or gagner entre 5 et 20 or
                player.gold += gold_gain
                print(f"\nVous avez gagné {exp_gain} point d'expérience ainsi que {gold_gain} pièces d'or!")

        elif action.lower() == "fuir":
            print("Vous avez réussi à fuir le combat!")
            break

