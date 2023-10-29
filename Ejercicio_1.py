import random
class Dice:
    def __init__(self):
        self.number = None
    def throw(self):
        self.__number = random.randint(1,6)
        return self.__number
    