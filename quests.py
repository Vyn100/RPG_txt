class Quest:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_completed = False

class EliminateWolves(Quest):
    def __init__(self):
        super().__init__("Éliminez les loups", "Éliminez 3 loups sauvages de la forêt.")
        self.wolf_count = 0

    def update(self):
        self.wolf_count += 1
        if self.wolf_count >= 3:
            self.is_completed = True
            print("\nQuête terminée ! Vous avez éliminé tous les loups.")
