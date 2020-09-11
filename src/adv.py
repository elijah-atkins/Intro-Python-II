from room import Room
from player import Player
from item import Item

# Declare all the rooms

outside = Room("Outside Cave Entrance","North of you, the cave mount beckons",[Item('Lantern','Provides light')])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[Item('stick','provides meager defense'), 
Item('A dead rat',' find out if you must pick up everything')])

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [])

narrow =   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [])

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
	[Item('Penny',' buy something, I guess')])


# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playing = True
player = Player("Xenu the Adventurer", outside)
directions = ["n", "s", "e", "w"]


while playing:
        # Print out some room data
    print(f'\n~ {player.current_room.name} ~\n\t{player.current_room.description}\n')
    if len(player.current_room.items) != 0:
        items_list = player.current_room.items.copy()
        for item in items_list:
            approved_ans = False
            print(f"You Found:\n{item.name} to {item.description}")
            while approved_ans is False:
                ans = input('Pick up item?(y/n):')
                if ans == 'y':
                    player.items.append(item)
                    player.current_room.items.remove(item)
                    approved_ans = True
                elif ans == 'n':
                    approved_ans = True
                else:
                    print('Choose yes or no!') 


        #player's inventory
        items_list = []
        for item in player.items:
            items_list.append(item.name)
        print(f'Your Inventory:{str(items_list)[1:-1]}')


        #for player to be able to manage
        approved_ans = False
        while approved_ans is False:
            ans = input('Manage Inventory? (y/n):')
            if ans == 'y':
                approved_ans == True
                items_list = player.items.copy()
                for item in items_list:
                    rem = input(f'Remove {item.name}?(y/n):')
                    if rem == 'y':
                        player.items.remove(item)
                        player.current_room.items.append(item)
                        item_list = []
                        for item in player.items:
                            item_list.append(item.name)
                        print(f'Your Inventory:{str(item_list)[1:-1]}')
                    elif rem == 'n':
                        pass
                    else:
                        pass
            elif ans == 'n':
                approved_ans = True
            else:
                print('Choose yes or no!')
        try:
            player.current_room = player.current_room.s_to
        except:
            print('Ran into a wall silly')
    cmd = input('>>>')
    if cmd in directions:
        player.move(cmd)       
    if cmd == "inventory":
        item_list = []
        for item in player.items:
            item_list.append(item.name)
        print(f'Your Inventory:{str(item_list)[1:-1]}')
    if cmd == 'q':
        playing = False
        print("Thanks for playing!")
