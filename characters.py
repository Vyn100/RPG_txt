# Gère les personnages, ennemis, compétences, etc.

class Character:
    def __init__(self, name, health=100, strength=10, magic=10, defense=5):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10, 5, 5)
        self.experience = 0
        self.level = 1
        self.next_level_exp = 100
        self.gold = 0 # L'argent du joueur
        self.inventory = []
        self.max_health = 100
    
    def revive(self):
        self.health = self.max_health / 2  # Par exemple, vous pourriez ressusciter le joueur avec la moitié de sa santé maximale
        print(f"\n{self.name} a été ressuscité avec {self.health}HP! \n Vous devriez prendre une potion de soin !")

    def gain_experience(self, amount):
        self.experience += amount
        
        while self.experience >= self.next_level_exp:
            self.level_up()

    def level_up(self):
        self.experience -= self.next_level_exp
        self.level += 1
        self.next_level_exp += 100
        
        # Augmentez les stats du joueur
        self.health += 12
        self.strength += 5
        self.magic += 5
        self.defense += 2
        
        print(f"\nFélicitations ! {self.name} est maintenant niveau {self.level}!")

class Enemy(Character):
    def __init__(self, name, health, strength, magic, defense):
        super().__init__(name, health, strength, magic, defense)
