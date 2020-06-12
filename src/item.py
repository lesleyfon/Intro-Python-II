class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}, {self.description}'

    def on_take(self):

        return f'You picked up {self.name}'

    def on_drop(self):
        return f'You drop up {self.name}'
