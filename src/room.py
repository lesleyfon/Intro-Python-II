# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.w_to = None
        self.s_to = None
        self.e_to = None
        self.items = []

    def __str__(self):
        # Get keys of a class
        # room_attr = [i for i in self.__dict__.keys() if i[:1] != "_"]
        return f' Room name: {self.name} \n Description: {self.description}'

    def print_items(self):
        if len(items) >= 1:
            for item in self.items:
                print(item)

    def get(self, item_name):
        return_item = ''
        if item_name in self.items:

            for item in self.items:
                return_item = self.items.remove(item)
        else:
            return_item = 'No item was found'
        return return_item
