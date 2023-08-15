from characters import Enemy
from combat import start_combat
from inventory import Item, Potion

def encounter_enemy(player):
    enemy = Enemy(name="Loup", health=50, strength=8, magic=5, defense=3)
    print(f"\nUn {enemy.name} sauvage apparaît !")
    start_combat(player, enemy)
    if not enemy.is_alive():
        # Récompensez le joueur avec un objet
        potion = Potion("Potion de Vie", "Restaure 20HP", 20)
        player.inventory.append(potion)
        print(f"\nVous avez trouvé une {potion.name} après avoir vaincu {enemy.name}!")
    
def find_treasure(player):
    print("\nVous avez trouvé un trésor caché !")
    # Vous pouvez ajouter ici des objets à l'inventaire du joueur ou lui donner de l'XP, par exemple.
