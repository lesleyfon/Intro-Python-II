# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def print_current_room_details(self):
        print(
            f' Player Name: {self.name} \n Current Room Name: {self.current_room.name} \n Current Room Description: {self.current_room.description} \n')
