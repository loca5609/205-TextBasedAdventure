import game_data

rooms_dict = {}

class MoveReturn:
   def __init__(self, room, message=None):
      self.room = room
      self.message = message

class Room:
   def __init__(self, obj):
      self.title = obj["title"]
      self.room_desc = obj["room_desc"]
      self.connections = obj["connections"]
      self.item_key = obj["item_key"]
      self.items = obj["items"]
      self.danger = obj["danger"]
      self.url = None

   def url_friendly(self):
      return self.title.lower().replace(" ", "_")

   def unlocked(self):
      if (self.item_key is None) or (items.items_dict[self.item_key].visited):
         return True
      else:
         return False

   def move_to(self, new_room, item_ref=None):
      try:
         new_room = new_room.lower()
      except (AttributeError, TypeError):
         return MoveReturn(self, "Directions can only be alphanumeric characters!")
      if new_room in self.connections and self.unlocked():
         return MoveReturn(rooms_dict[new_room], None)
      else:
         return MoveReturn(self, new_room + " is not accessible from here.")

class Player:
   def __init__(self, score, current_room, inventory, is_alive=True, message=None):
      self.score = score
      self.current_room = current_room
      self.inventory = inventory
      self.is_alive = is_alive
      self.message = message

   def setMessage(self, new_message):
      self.message = new_message

   def in_danger(self):
      if self.current_room.danger

   def getScore(self):
      return self.score

   def addScore(self):
      self.score += 1

   def inspect(item_name, room_items, inventory):
      try:
         if item_name in room_items:
         #Checks specific effect attached to item, otherwise inspects item dialogue
            #if world_env.item_list[item_name].effect[0] is "inspect_death":
            #    move_to("inspect game over", world_env, item_name)
            #else:
            items_dict[item_name].visited = True
            return items_dict[item_name].dialogue
         elif item_name in inventory:
            return items_dict[item_name].dialogue
         else: 
            return "ERROR - Can't seem to find that..."
        except ((AttributeError, TypeError)):
            return "ERROR - Can't seem to find that..."

for obj in game_data.room_list:
   rooms_dict[obj["dict_key"]] = Room(obj)

print (rooms_dict["lab"].title)
print (rooms_dict["lab"].room_desc)
print (rooms_dict["lab"].connections)
print (rooms_dict["lab"].item_key)
print (rooms_dict["lab"].items)
print (rooms_dict["lab"].url)

test = rooms_dict["lab"].move_to("passage")
print (test.room.title)

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