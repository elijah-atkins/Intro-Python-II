# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room, items = []):
        self.name = name
        self.current_room = starting_room
        self.items = []

    def move(self, direction):
        if hasattr(self.current_room, f'{direction}_to') is not False:
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('\nYou ran into a wall Silly!\n')
    def getitem(self, item):

        if item in self.current_room.roomitems:

            self.playeritems.append(item)
            self.current_room.roomitems.remove(item)

            print(f'\n\tYou got the {item}!\n')
        else:
            print(f'\n\t{self.current_room.name} does\'t have the {item}\n')

    def dropitem(self, item):

        if item in self.playeritems:

            self.playeritems.remove(item)
            self.current_room.roomitems.append(item)

            print(f'\n\tYou dropped the {item}!\n')
        else:
            print(f'\n\tYou don\'t have the {item} to drop!\n')

    def checkinv(self):

        inv = ', '.join(self.playeritems)

        if inv:
            print(f'\n\t{inv}\n')
        else:
            print('\n\tYou have nothing in your inventory!\n')

    def searchroom(self):

        if self.current_room.roomitems:

            print(
                f'\n\tItem(s) in {self.current_room.name}: {", ".join(self.current_room.roomitems)}\n')
        else:
            print(f'\n\tThere is nothing useful in this room\n')