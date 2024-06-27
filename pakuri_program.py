from pakudex import *

if __name__ == '__main__':
    menu = True
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    choose_capacity = True
    while choose_capacity == True:
        # Asks user for the capacity of the pakudex. Keeps asking until a valid input is given
        try:
            capacity = int(input('Enter max capacity of the Pakudex: '))
            if capacity < 1:
                raise ValueError
            choose_capacity = False
        except ValueError:
            print('Please enter a valid size.')
            print()
    print(f'The Pakudex can hold {capacity} species of Pakuri.')
    print()
    # creates pakudex instance
    pakudex_instance = Pakudex(capacity)

    while menu == True:
        menu_pick = True
        while menu_pick == True:
            try:
                # Prints menu and asks user for option. Keeps asking for option until a valid input is given
                print('Pakudex Main Menu')
                print('-----------------')
                print('1. List Pakuri')
                print('2. Show Pakuri')
                print('3. Add Pakuri')
                print('4. Evolve Pakuri')
                print('5. Sort Pakuri')
                print('6. Exit')
                print()
                user_choice = int(input('What would you like to do? '))
                if user_choice > 6 or user_choice < 1:
                    raise ValueError
                menu_pick = False
            except ValueError:
                print('Unrecognized menu selection!')
                print()

        # List pakuri
        if user_choice == 1:
            # Prints out the species of each pakuri instance, or gives an error is there are no pakuri
            if pakudex_instance.pakuris != []:
                print('Pakuri In Pakudex:')
                for index, pakuri in enumerate(pakudex_instance.get_species_array()):
                    print(f'{index + 1}. {pakuri}')
                print()
            else:
                print('No Pakuri in Pakudex yet!')
                print()

        # Show pakuri
        elif user_choice == 2:
            # Gets a species name from user input and checks the species array for it. If it doesn't exist, an error is
            # printed out. Otherwise, the class containing the species is searched for the stats, which is printed out
            # The stats are placed into a list, which is printed out.
            species_names = input('Enter the name of the species to display: ')
            if pakudex_instance.get_species_array() != None:
                if pakudex_instance.get_stats(species_names) == None:
                    print('Error: No such Pakuri!')
                    print()
                else:
                    paku_list = pakudex_instance.get_stats(species_names)
                    print(f'Species: {species_names}')
                    print(f'Attack: {paku_list[0]}')
                    print(f'Defense: {paku_list[1]}')
                    print(f'Speed: {paku_list[2]}')
                    print()
            else:
                print('Error: No such Pakuri!')
                print()

        # Add pakuri
        elif user_choice == 3:
            # Checks is the pakudex is full before adding a species
            if pakudex_instance.get_species_array() != None:
                if (pakudex_instance.size == pakudex_instance.capacity):
                    print('Error: Pakudex is full!')
                    print()
                else:
                    # User input is taken for a pakuri. If the species name is already in the pakudex, an error is
                    # printed. Otherwise, an instance is made for the pakuri and it is added to the pakudex.
                    added_pakuri = input('Enter the name of the species to add: ')
                    if (pakudex_instance.add_pakuri(added_pakuri) == False) and (added_pakuri in pakudex_instance.get_species_array()):
                        print('Error: Pakudex already contains this species!')
                        print()
                    else:
                        pakuri_added = Pakuri(added_pakuri)
                        pakudex_instance.add_pakuri(added_pakuri)
                        print(f'Pakuri species {added_pakuri} successfully added!')
                        print()
            elif pakudex_instance.get_species_array() == None:
                added_pakuri = input('Enter the name of the species to add: ')
                pakudex_instance.add_pakuri(added_pakuri)
                print(f'Pakuri species {added_pakuri} successfully added!')
                print()

        # Evolve pakuri
        elif user_choice == 4:
            # Asks user for input for a species to evolve. The pakudex is searched for the species and an error is
            # if the pakudex does not have the species. Otherwise, the pakuri is evolved after finding its instance
            evolve_choice = input('Enter the name of the species to evolve: ')
            if pakudex_instance.pakuris == [] or evolve_choice not in pakudex_instance.get_species_array():
                print('Error: No such Pakuri!')
                print()
            else:
                for pakuri in pakudex_instance.pakuris:
                    if pakuri.species == evolve_choice:
                        pakuri.evolve()
                print(f'{evolve_choice} has evolved!')
                print()

        # Sort pakuri
        elif user_choice == 5:
            # so
            pakudex_instance.sort_pakuri()
            print('Pakuri have been sorted!')
            print()

        # Exit menu
        elif user_choice == 6:
            print('Thanks for using Pakudex! Bye!')
            break







