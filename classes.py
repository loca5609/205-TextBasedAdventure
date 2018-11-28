import random


# @class Room, handles the Rooms the players interact with
# @member: connections is a dictionary with {direction: room name}
class Room:
    def __init__(self, name="", connections={}, items=[], tags=[]):
        self.name = name
        self.connections = connections
        self.items = items
        self.tags = tags

    def look(self):
        numRooms = len(self.connections)
        print(
            f"You are in the {self.name}, There are doors to {numRooms} rooms:"
        )
        for key, value in self.connections.items():
            print(f"The {value} which is to the {key}")

    def search(self):
        # add text randomization
        print(f"You decide to look around the {self.name}")
        if (len(self.items) == 1):
            print(f"You see a {self.items[0]}")

        if (len(self.items) == 2):
            print(
                f" You notice a few items, a {self.items[0]} and a {self.items[1]}"
            )

        if (len(self.items) == 3):
            print(
                f"Several things are visible, {self.items[0]}, {self.items[1]}, and a {self.items[2]} as well."
            )


class Player:
    def __init__(self, name, inventory, current_room, level=1, HP=25, MP=15):
        self.name = name
        self.inventory = inventory
        self.current_room = current_room
        self.level = level
        self.HP = HP
        self.MP = MP

    def getInventory(self):
        print("You look in your inventory...")
        print("Inside you see...")
        print(self.inventory)

    def status(self):
        print(f""" 
            Player: {self.name}
            Health: {self.HP}
            Magic Power: {self.MP}
            Current Inventory: {self.inventory}
        """)

    def attack(self):
        if (self.level in range(1, 4)):
            atkRoll = random.randint(2, 7)
            crit = random.randint(0, 100)
            if (crit >= 95):
                atkRoll = atkRoll * 2
            return atkRoll
        if (self.level in range(4, 7)):
            atkRoll = random.randint(4, 13)
            crit = random.randint(0, 100)
            if (crit >= 94):
                atkRoll = atkRoll * 2
            return atkRoll


# @class Enemy: generic object for all enemys
# @param: level, this is used to determine attack strength (range of random numbers to deal damage)
class Enemy:
    def __init__(self, name, level, weapon, HP, MP):
        self.name = name
        self.weapon = weapon
        self.HP = HP
        self.MP = MP
        self.level = level

    def attack(self):
        if (self.level in range(1, 3)):
            atkRoll = random.randint(0, 5)
            crit = random.randint(0, 100)
            if (crit >= 96):
                atkRoll = atkRoll * 2
            return atkRoll
        if (self.level in range(3, 5)):
            atkRoll = random.randint(2, 8)
            if (crit >= 97):
                atkRoll = atkRoll * 2
            return atkRoll
        if (self.level in range(5, 8)):
            atkRoll = random.randint(4, 14)
            if (crit >= 98):
                atkRoll = atkRoll * 2
            return atkRoll
