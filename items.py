import game_data

class Item:
    def __init__(self, name, dialogue, effect=[None], visited=False):
        self.name = name
        self.dialogue = dialogue
        self.effect = effect
        self.visited = visited

    def inspect(self, item_name, room_items):
        try:
            if item_name in room_items:
            #Checks specific effect attached to item, otherwise inspects item dialogue
                if world_env.item_list[item_name].effect[0] is "inspect_death":
                    move_to("inspect game over", world_env, item_name)
                else:
                    world_env.player.message = world_env.item_list[item_name].dialogue
            elif item_name in world_env.player.inventory:
                world_env.player.message = world_env.item_list[item_name].dialogue
            else: 
                world_env.player.message = "ERROR - Can't seem to find that..."
        except ((AttributeError, TypeError)):
        world_env.player.message = "ERROR - Can't seem to find that..."

items_dict = {}

for obj in game_data.item_list:
   rooms_dict[obj["dict_key"]] = Item(obj)

# item_index = {
#     "metal office desk": Item("Office metal desk", 
#         "In the METAL OFFICE DESK, there are several drawers. In the topmost"
#         " drawer lies a piece of paper. A note, with only '0413' " 
#         "inscribed on it."),
#     "piles of paper": Item("Piles of paper", 
#         "The papers are shredded. The pages of fanfiction won’t here won’t help you here."),
#         "wooden chair": Item("Wooden chair", 
#         "You try sitting in the chair. You now have uncomfortable splinters in unforetold places."),
#     "wooden furniture": Item("Wooden furniture", 
#         "You once handcrafted all your tables and chairs with your grandchildren many summers ago. "
#         "It is now beyond repair. Amid the destruction, you find a single modified METAL BULLET. "
#         "Old treasures are hard to come by, you stow it in your HAMMERSPACE.",
#         False, ["add_item", "metal bullet"]),
#     "green vomit": Item("Green vomit",
#         "Inspecting the GREEN VOMIT, you find yourself becoming very woozy. HER radioactive levels "
#         "are too high for her own good. She’s sick. But it’s too late for you. GAME OVER.",
#         False, ["inspect_death"])
# }