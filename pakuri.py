class Pakuri:
    def __init__(self, species):
        # Initializes the variables for species, attack, defense, and speed
        self.species = species
        self.attack = (len(self.species) * 7) + 9
        self.defense = (len(self.species)*5) + 17
        self.speed = (len(self.species)*6) + 13

    def __lt__(self,other):
        # < operation overloading to sort the pakuri list
        if isinstance(other, Pakuri):
            if self.species < other.species:
                return True
        else:
            return False

    def get_species(self):
        return self.species

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def set_attack(self, new_attack):
        self.attack = new_attack

    def evolve(self):
        # increases the pakuri species stats upon evolution
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3