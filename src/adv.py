from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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
# If the user enters "q", quit the game.å

'''
    step 1:
        - Create a loop to accepts inputs. It should be continouse unless the user break or quit
        - A while loop will be perfect
'''
# Create a player and assign the outside to the current room
playerone = Player("Lesley", room["outside"])

print(playerone.current_room)
print(playerone.current_room.description + "\n")
while True:

    user_input = input(
        "Input the direction you will like to move towards(Valid inputs [N, W, S, E])")

    user_direction = ''

    # Parse user input of they type in multiple words
    if len(user_input.split(" ")) > 1:
        user_input = user_input.split(" ")
        user_direction = user_input[0]
        show_inventory = user_input[2]
        weapon = user_input[1]
        if show_inventory:
            print(playerone.items)
    else:
        user_direction = user_input

    try:
        if user_direction in ["s", "w", "n", "e"]:

            if user_direction == "n" and "outside" in playerone.current_room.name.lower():
                playerone.current_room = room["foyer"]
                playerone.print_current_room_details()
            elif user_direction == "s" and "foyer" in playerone.current_room.name.lower():
                playerone.current_room = room["outside"]
                playerone.print_current_room_details()

            elif user_direction == "n" and "foyer" in playerone.current_room.name.lower():
                playerone.current_room = room["overlook"]
                playerone.print_current_room_details()

            elif user_direction == "e" and "foyer" in playerone.current_room.name.lower():
                playerone.current_room = room["narrow"]
                playerone.print_current_room_details()

            elif user_direction == "s" and "overlook" in playerone.current_room.name.lower():
                playerone.current_room = room["foyer"]
                playerone.print_current_room_details()

            elif user_direction == "w" and "narrow" in playerone.current_room.name.lower():
                playerone.current_room = room["foyer"]
                playerone.print_current_room_details()

            elif user_direction == "n" and "narrow" in playerone.current_room.name.lower():
                playerone.current_room = room["treasure"]
                playerone.print_current_room_details()

            elif user_direction == "n" and "treasure" in playerone.current_room.name.lower():
                playerone.current_room = room["narrow"]
                playerone.print_current_room_details()

            else:
                print("Player can't move in that direction")
            pass
        elif user_direction == "q":
            print("\n Thanks For playing, See you ")
            break
        else:
            print("\n Movement isn't allowed, Please enter a valid input ")
    except ValueError:
        print("Please enter a valid number")

'''

'''
