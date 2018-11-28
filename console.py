from classes import *
from rooms import *
from combat import *
from rooms import layout

player = Player("Trash Roach", [], layout[0])

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
