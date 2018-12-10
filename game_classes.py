#give items another variable called hammerspace
#makea ntoher function that prints out the inventory
#funciton will parse through all the items in the world
#check if hammerspace equals true
#print those

# class SpecificRoom(Room):
#    def __init__(self, obj):
#       super().__init__(obj)
#       self.specific_item = obj["specific_item"]
#       self.success_dest = obj["success_dest"]
#       self.death_msg = obj["death_msg"]

#    def get_dest(self):
#       return self.success_dest

#    def get_death_msg(self, item):
#       if item in self.death_msg:
#          return death_msg[item]
#       else:
#          return death_msg["default"]

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

class GameState:
   def __init__(self, player, current_room, world_rooms, world_items, item_flags, hammerspace_flags, room_urls=None):
      self.player = player
      self.current_room = current_room
      self.world_rooms = world_rooms
      self.world_items = world_items
      self.item_flags = item_flags
      self.hammerspace_flags = hammerspace_flags
      self.room_urls = room_urls

   def url_friendly(self):
      url = self.world_rooms[self.current_room]["title"]
      url = url.lower().replace(" ", "_")
      url = url.replace("'", "")
      url = url.replace(".", "")
      return url

   def get_room_data(self):
      return self.world_rooms[self.current_room]

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

   #def hammerspace(self):
   #   for item in self.hammerspace_flags:
   #      if item is True:

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

         # Check if Item is available in the Player's room; Determine "type" of inspect associated with item
         elif self.valid_item(item, self.world_rooms[self.current_room]["items"]) and self.unlocked(item):
            item = item.lower()
            print (item)
            self.determine_effect(item)
      else:
         self.player.setMsg("There is nothing noteworthy to inspect here.")

   def change_item_state(self, item):
      if (item in self.item_flags) and (self.item_flags[item] is False):
         self.player.addScore()
         self.item_flags[item] = True
      elif (item in self.hammerspace_flags) and (self.hammerspace_flags[item] is False):
         self.player.addScore()
         self.hammerspace_flags[item] = True

   def determine_effect(self, item):
      if "effect" in self.world_items[item]:

         # Kill player if player inspects item
         if self.world_items[item]["effect"] == "inspect_kill":
            self.player.setMsg(self.world_items[item]["item_desc"])
            self.player.kill_player()

         # Kill player if player does not inspect prereq item; reg inspect otheriwse
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

         # Adds a different item to the inventory than the item Player inspects
         elif self.world_items[item]["effect"] == "hammerspace_diff_item":
            self.player.setMsg(self.world_items[item]["item_desc"])
            self.change_item_state(self.world_items[item]["new_item"])

      # Adds inspected item to inventory, if required, and show item dialogue
      else:
         self.change_item_state(item)
         self.player.setMsg(self.world_items[item])

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