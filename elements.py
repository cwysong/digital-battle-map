from tkinter import PhotoImage

class entity():
    
    def __init__(self, name = "None", speed = 30, location = (0,0), sprite = None) -> None:
        self.status:str = None
        self.name:str = name
        self.speed:int = speed
        self.location:tuple= location
        self.sprite = sprite
        self.photo = PhotoImage(file=self.sprite)
        self.prev_id = None
        self.cur_id = None


class monster(entity):
    
    def __init__(self) -> None:
        super().__init__()


class player(entity):
    
    def __init__(self) -> None:
        super().__init__()


class status_effect:
    
    def __init__(self) -> None:
        self.effects:dict[str,str] = dict()
        self.effects["prone"] = "A prone creature's only movement option is to crawl, unless it stands up and thereby ends the condition. The creature has disadvantage on attack rolls. An attack roll against the creature has advantage if the attacker is within 5 feet of the creature. Otherwise, the attack roll has disadvantage."


    def define(self, effect:str) -> str:
        return self.effects[effect]


class spell_range:

    def __init__(self) -> None:
        pass