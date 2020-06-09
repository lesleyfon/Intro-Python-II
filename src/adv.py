from room import Room
from player import Player

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

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

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
# If the user enters "q", quit the game.å
'''
    step 1:
        - Create a loop to accepts inputs. It should be continouse unless the user break or quit
        - A while loop will be perfect
'''


while True:

    user_direction = input(
        "Input the direction you will like to move towards(Valid inputs [N, W, S, E])").lower()

    playerone = Player("First Player", room["outside"])
    print(playerone.current_room)
    print(playerone.current_room.description + "\n")
    try:
        if user_direction in ["s", "w", "n", "e"]:
            if user_direction == "w":

                room['outside'].w_to.append(room["outside"])
                print(room["outside"])

            elif user_direction == "s":
                room['outside'].s_to.append(room["outside"])
                print(room["outside"])

            elif user_direction == "n":

                room['outside'].n_to.append(room["outside"])
                print(room["outside"])

            elif user_direction == "e":
                room['outside'].e_to.append(room["outside"])
                print(room["outside"])

        elif user_direction == "q":
            print("\n Thanks For playing, See you ")
            break
        else:
            print("\n Movement isn't allowed, Please enter a valid input ")
    except ValueError:
        print("Please enter a valid number")
