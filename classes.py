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
    def __init__(self, name, inventory, current_room, HP=25, MP=15):
        self.name = name
        self.inventory = inventory
        self.current_room = current_room
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


# @func: Handles moving the player object between rooms
# Checking that there is a room to the indicated direction and updating
# the players current room if the direction is valid
# @params: direction: one of the cardinal directions north,south,east,and west
# or abreviations n,s,e,w
# @params: current_room, Room object player.current_room
def move(player, direction):
    try:
        direction = direction.lower()
    except (AttributeError, TypeError):
        raise AssertionError("Directions can only be strings!")
    allowed_dirs = player.current_room.connections.keys()
    if direction in allowed_dirs:
        new_room = player.current_room.connections.get(direction)
        print(f"Moving to {new_room}")
        player.current_room = findRoom(new_room, layout)
    else:
        print(f"Sorry there isnt a door to the {direction}")


# @funct: finds and returns the room object from the room name
# @param: name String: name of the room to find
# @param: layout List[Room]: list of Room objects, ideally every room in the game
def findRoom(name, layout):
    for room in layout:
        if (room.name.lower() == name.lower()):
            return room


#inventory = ["gun", "water bottle"]

#    Throne Room ----- Lab
#          |
#         |
#      Atrium ------ Rec Room

throne_room = Room("Throne Room", {
    "south": "Atrium",
    "east": "Lab"
}, ["Baseball Bat"], ["Kings Room", "Gilded Hall", "Big Chair Room"])

atrium = Room("Atrium", {
    "north": "Throne Room",
    "east": "Rec Room"
}, ["Potted Plant", "A Nicer Potted Plant"],
              ["Room with the Most Air Volume", "Real Tall Walls Here"])

lab = Room("Lab", {"west": "Throne Room"}, ["Microscope", "Macroscope"],
           ["Nerd Room", "Very Clean Room"])

rec_room = Room("Rec Room", {"west": "Atrium"},
                ["Baseball Bat", "Pool Cue", "Basketball"],
                ["Chillzone 9000", "Big Sofa here, very soft"])

layout = [throne_room, atrium, lab, rec_room]

start_room = rec_room
player = Player("Trash Roach", [], start_room)

while True:
    choice = input("What would you like to do? ")
    if (choice.lower() == "look"):
        player.current_room.look()
    if (choice.lower() == "help"):
        print(
            "The commands you can use are: look, inventory, search, go, status, and exit"
        )
    if (choice.lower() == "inventory" or choice.lower() == "inv"):
        player.getInventory()
    if (choice.lower() == "search"):
        player.current_room.search()
        # TODO: add interactions so you can place items into inventory
    if (choice.lower() == "go"):
        direction = input("Which direction? ")
        move(player, direction)
    if (choice.lower() == "status"):
        player.status()
    if (choice.lower() == "exit"):
        break

print("Thank you for playing!")
