from pakuri import *

class Pakudex():
    # Pakudex has a list of pakuri
    def __init__(self, capacity=20):
        # initializes the list of pakuri species and stats, the capacity of the pakudex and size of current pakuri list
        self.pakuris = []
        self.capacity = capacity
        self.size = 0


    def get_size(self):
        self.size = len(self.pakuris)
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if self.pakuris == []:
            return None
        else:
            # appends the species of each pakuri instance to an empty list which is returned
            paku_list = []
            for pakuri in self.pakuris:
                paku_list.append(pakuri.species)
            return paku_list

    def get_stats(self,species):
        # creates a list of the specified pakuri species' stats
        if self.pakuris == [] or (species not in self.get_species_array()):
            return None
        elif species in self.get_species_array():
            for pakuri in self.pakuris:
                if pakuri.species == species:
                    paku_stats = [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return paku_stats

    def sort_pakuri(self):
        self.pakuris.sort()
        return self.pakuris

    def add_pakuri(self, species):
        # checks if there are any pakuri in the pakudex already, if so the inputted species is checked for
        # repetitions or if it would not fit into the specified capacity
        if self.get_species_array() != None:
        # if list full - unsuccessful
            if self.size == self.capacity:
                return False
        # check for duplicates -unsuccessful
            elif species in self.get_species_array():
                return False
            else:
                # creates an instance for the pakuri species and appends it to the species list
                # increases the self.size which counts how many pakuri there are to compare to the capacity
                pakuri = Pakuri(species)
                self.pakuris.append(pakuri)
                self.size += 1
                return True
        else:
            pakuri = Pakuri(species)
            self.pakuris.append(pakuri)
            self.size += 1
            return True

    def evolve_species(self, species):
        # is the inputted species is in the pakudex, it is evolved by increasing its stats
        if self.pakuris == [] or (species not in self.get_species_array()):
            return False
        elif species in self.get_species_array():
            Pakuri(species).evolve()
            return True

