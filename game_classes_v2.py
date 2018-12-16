# Player class keeps track of the player's score, whether they are alive or not
# and the specific message shown based on their actions.
class Player:
   def __init__(self, score=0, is_alive=True, msg=None):
      self.score = score
      self.is_alive = is_alive
      self.msg = msg

   def kill_player(self):
      self.is_alive = False

   def getScore(self):
      return self.score

   def addScore(self):
      self.score += 1

   def setMsg(self, msg=None):
      self.msg = msg

# GameState class holds the Player object, the player's current room,
# the data of the game's rooms, data of the world's items, flags for key items,
# and flags for important items that must exist in inventory.
class GameState:
   def __init__(self, player, current_room, world_rooms, world_items, item_flags, hammerspace_flags):
      self.player = player
      self.current_room = current_room
      self.world_rooms = world_rooms
      self.world_items = world_items
      self.item_flags = item_flags
      self.hammerspace_flags = hammerspace_flags

# Make it so the current scene is URL friendly, derived from the room's title
   def url_friendly(self):
      url = self.world_rooms[self.current_room]["title"]
      url = url.lower().replace(" ", "_")
      url = url.replace("'", "")
      url = url.replace(".", "")
      return url

   def get_room_data(self):
      return self.world_rooms[self.current_room]

# Check if the current room is unlocked, based on whether or not the room requires a key item,
# and if that key item has been interacted with, or if that key item must be interacted with on
# the room's locked state to view the unlocked state.
   def unlocked(self, item):
      if "key_item" in self.world_rooms[self.current_room]:
         activated_key = self.world_rooms[self.current_room]["key_item"]
         if activated_key in self.item_flags and self.item_flags[activated_key]:
            return True
         elif activated_key in self.hammerspace_flags and self.hammerspace_flags[activated_key]:
            return True
         elif "inspect_key" in self.world_rooms[self.current_room] and activated_key == item:
            return True
         else:
            return False
      else:
         return True

# Shows items that are "in inventory". There is no actual inventory system (picking up and dropping items, etc.),
# but the items added to the "inventory" are necessary for the endgame sequence. The inventory function is used
# so the player can remember what is on the protagonist's person.
   def inventory(self):
      inv_message = ["These are the items in your HAMMERSPACE: "]
      for item, value in self.hammerspace_flags.items():
         if value is True:
            inv_message.append(item)
      if len(inv_message) == 1:
         return "Your HAMMERSPACE is currently empty."
      else:
         return inv_message

# Check if the item is valid, as a regular item in the room, or as a key item.
   def valid_item(self, item_name, room_items):
      try:
         item_name = item_name.lower()
      except (AttributeError, TypeError):
         self.player.setMsg("Item can only be alphanumeric characters!")
         return False
      if item_name in room_items:
         return True
      elif "key_item" in self.world_rooms[self.current_room] and self.world_rooms[self.current_room]["key_item"] == item_name:
         return True
      else:
         self.player.setMsg("ERROR - Can't seem to find that...")
         return False  

   def inspect(self, item):
      # Check if room has any items to Inspect
      if "items" in self.world_rooms[self.current_room] or "specific_item" in self.world_rooms[self.current_room]:

         #If player is in a SpecificRoom, check if they entered requirement. Kill otherwise.
         if "specific_item" in self.world_rooms[self.current_room]:
            item = item.lower()
            if self.world_rooms[self.current_room]["specific_item"] == item:
               if item in self.item_flags:
                  if self.item_flags[item]:
                     self.current_room = self.world_rooms[self.current_room]["success_dest"]
                  else:
                     self.player.setMsg(self.world_rooms[self.current_room]["death_msg"]["11DEAFAULTDEATHMSG11"])
                     self.player.kill_player()
               elif item in self.hammerspace_flags:
                  if self.hammerspace_flags[item]:
                     self.current_room = self.world_rooms[self.current_room]["success_dest"]
                  else:
                     self.player.setMsg(self.world_rooms[self.current_room]["death_msg"]["11DEAFAULTDEATHMSG11"])
                     self.player.kill_player()
               else:
                  self.current_room = self.world_rooms[self.current_room]["success_dest"]
            else:
               if item in self.world_rooms[self.current_room]["death_msg"]:
                  self.player.setMsg(self.world_rooms[self.current_room]["death_msg"][item])
                  self.player.kill_player()
               else:
                  self.player.setMsg(self.world_rooms[self.current_room]["death_msg"]["11DEAFAULTDEATHMSG11"])
                  self.player.kill_player()

         # Check if Item is available in the player's room; Determine "type" of inspect associated with item
         # Cannot inspect on locked rooms.
         elif self.valid_item(item, self.world_rooms[self.current_room]["items"]) and self.unlocked(item):
            item = item.lower()
            print (item)
            self.determine_effect(item)
      else:
         self.player.setMsg("There is nothing noteworthy to inspect here.")

# Change the item flag to True and increments the player's score if the inspected item
# has not been inspected before.
   def change_item_state(self, item):
      if (item in self.item_flags) and (self.item_flags[item] is False):
         self.player.addScore()
         self.item_flags[item] = True
      elif (item in self.hammerspace_flags) and (self.hammerspace_flags[item] is False):
         self.player.addScore()
         self.hammerspace_flags[item] = True

   def determine_effect(self, item):
      if "effect" in self.world_items[item]:

         # inspect_kill: Kill player if player inspects item
         if self.world_items[item]["effect"] == "inspect_kill":
            self.player.setMsg(self.world_items[item]["item_desc"])
            self.player.kill_player()

         # inspect_prereq: Kill player if player does not inspect prereq item; regular inspect otheriwse
         elif self.world_items[item]["effect"] == "inspect_prereq":
            if (self.world_items[item]["prereq"] in self.item_flags) and (self.item_flags[self.world_items[item]["prereq"]]):
               self.player.setMsg(self.world_items[item]["item_desc"])
               self.change_item_state(item)
            elif (self.world_items[item]["prereq"] in self.hammerspace_flags) and self.hammerspace_flags[self.world_items[item]["prereq"]]:
               self.player.setMsg(self.world_items[item]["item_desc"])
               self.change_item_state(item)
            else:
               self.player.setMsg(self.world_items[item]["death_msg"])
               self.player.kill_player()

         # hammerspace_diff_item: Adds a different item to the inventory than the item Player inspects
         elif self.world_items[item]["effect"] == "hammerspace_diff_item":
            self.player.setMsg(self.world_items[item]["item_desc"])
            self.change_item_state(self.world_items[item]["new_item"])

      # If the inspected item does not have an "effect", add item to inventory, if required, and show item dialogue.
      else:
         self.change_item_state(item)
         self.player.setMsg(self.world_items[item])

# Change the player's current room, if the requested room is a valid connection of the current room and
# the requested room is not locked.
   def move(self, new_room):
      try:
         new_room = new_room.lower()
         if self.world_rooms[self.current_room]["connections"] is not None:
            if new_room in self.world_rooms[self.current_room]["connections"]:
               self.current_room = new_room
               self.player.setMsg()
            else:
               self.player.setMsg("'" + new_room + "'" + " is not accessible from here.")
         else:
            self.player.setMsg("The sound you make in moving around alerts HER to your presence. In her manic rampage, she shreds you to pieces. GAME OVER.")
            self.player.kill_player()
      except (AttributeError, TypeError):
         self.player.setMsg("Directions can only be alphanumeric characters!")