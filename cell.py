from elements import entity

class cell: 
    
    def __init__(self) -> None:
        self.creature = None

    def add_entity(self, creature:entity):
        self.creature = creature