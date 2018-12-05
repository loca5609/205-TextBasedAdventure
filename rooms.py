import game_data, items

#items = importlib.import_module(game_data.py)

class Room:
   def __init__(self, obj):
      self.title = obj["title"]
      self.room_desc = obj["room_desc"]
      self.connections = obj["connections"]
      self.item_key = obj["item_key"]
      self.items = obj["items"]
      self.url = None

   def setURL(self):
      return self.title.lower().replace(" ", "_")

   # def move_to(self, new_room, item_ref=None):
   #    try:
   #       new_room = new_room.lower()
   #    except (AttributeError, TypeError):
   #       return "Directions can only be alphanumeric characters!"
   #    if new_room in self.connections:
   #       print (new_room)
   #       if new_room == "inspect game over":
   #          self. = world.setRoom(new_room)
   #          world_env.player.message = world_env.item_list[item_ref].dialogue
   #       else:
   #          world_env.player.current_room = world.setRoom(new_room)
   #          world_env.player.setMessage(None)
   #    else:
   #       return new_room + " is not accessible from here."


rooms_dict = {}

for obj in game_data.room_list:
   rooms_dict[obj["dict_key"]] = Room(obj)

print (rooms_dict["lab"].title)
print (rooms_dict["lab"].room_desc)
print (rooms_dict["lab"].connections)
print (rooms_dict["lab"].item_key)
print (rooms_dict["lab"].items)
print (rooms_dict["lab"].url)

# room_index = {
#    "laboratory antechamber": Room("Laboratory Antechamber", 
#       (["You enter your LABORATORY ANTECHAMBER. It is as clean and organized as you had left it, "
#       "perfect for patients to wait in. Judging from the blaring red lights, the whole building is in LOCKDOWN."
#       " This will not be as straightforward as you had hoped. There is a door leading to a long PASSAGE."]), ["passage"]),
#    "passage": Room("Passage",
#       (["The PASSAGE continues for another 30 feet. Sirens blare loudly."
#       " You have options of moving to different places. Some doors are inaccessible."
#       "Along the wall there are several doors. One door leads to the CALITIS OFFICE, "
#       "another to the CISTERN, and the last to the STUDY."]),
#       ["laboratory antechamber", "calitis office", "cistern", "study"]),
#    "calitis office": Room("Calitis Office",
#       (["You notice CLAW MARKS leading to the office door. Inside, the neatly stacked PILES OF PAPER"
#       " are all shredded and seemingly tossed wildly across the room. The WOODEN CHAIR is in pieces."
#       " The only thing left intact is the METAL OFFICE DESK. What do you do?"]),
#       ["passage"], None, ["metal office desk", "piles of paper", "wooden chair"]),
#    "study": Room("The Study", 
#       (["The door to THE STUDY is locked. The ALPHANUMERIC KEYPAD glows red angrily as you "
#       "press random codes to no avail.", 
#       "Inside is a mess. Your WOODEN FURNITURE is wrecked. Splotches of GREEN VOMIT lay strewn across "
#       "the walls and floor. There is a door leading to the EXPERIMENTATION LAB."]),
#       ["passage", "experimentation lab", "inspect game over"], item_index["metal office desk"], ["wooden furniture", "green vomit"]),
#    "cistern": Room("Cistern",
#       (["The once pristine POOLS OF WATER in this room are now tainted with radioactive chemicals. "
#       "Probably the same that caused HER to freak out. On the opposite wall, across the POOLS OF WATER, "
#       "hangs CHECKHOV’S GUN."]),
#       ["passage", "inspect game over"], None, ["pools of water", "chekhov's gun"]),
#    "inspect game over": Room("How unfortunate", "", []),
# }