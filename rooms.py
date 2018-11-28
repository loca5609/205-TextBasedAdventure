from classes import Room


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
