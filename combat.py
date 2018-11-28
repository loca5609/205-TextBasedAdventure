from classes import *
from rooms import layout
# test Battle
test_room = Room()

player = Player("Trash Roach", [], layout[0])
lizard = Enemy("Lizard", 2, "Tail", 10, 10)

print(
    f"The battle has started! {player.name} is facing off against {lizard.name}!"
)
while True:
    print(f"{player.name}: HP: {player.HP} MP: {player.MP}")
    print(f"{lizard.name}: HP: {lizard.HP} MP: {lizard.MP}")

    choice = input("What would you like to do? ")
    if (choice.lower() == "help"):
        print("You can attack, defend(NO), spell(NO), run")
    if (choice.lower() == "attack"):
        damage = player.attack()
        if (damage > 0):
            print(
                f"You swing at the {lizard.name}! You hit for {damage} damage!"
            )
            lizard.HP = lizard.HP - damage
        else:
            print(f"Darn! Missed the {lizard.name}")
        if (lizard.HP <= 0):
            print(f"The {lizard.name} has been defeated!")
            break

    if (choice.lower() == "defend"):
        print("nah")
    if (choice.lower() == "spell"):
        print("nah")
    if (choice.lower() == "run"):
        print(f"fight the {lizard.name}, bitch.")
