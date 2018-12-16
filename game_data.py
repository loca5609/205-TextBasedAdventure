world_items = {
    # "dict_key": string with spaces (the dictionary key of the Item object),
    # "name": string (name of the item),
    # "item_desc": string (dialogue shown when Inspecting the item),
    # "effect": string/none (what effect this item does when Inspect, other than the default inspect function)

    ### BIG LEVER (key)
    "big lever": "You pull the BIG LEVER.",
    
    ### METAL DESK (key item)
    "metal desk": "In the METAL DESK, there are several drawers. "
        "In the top most drawer lies a piece of paper. A note, with only '0413' inscribed on it.",

    ### PILES OF PAPER (no effect)
    "piles of paper": "The papers are shredded. The pages of fanfiction won’t help you here.",

    ### WOODEN CHAIR (no effect)
    "wooden chair": "You try sitting in the chair. " 
        "You now have uncomfortable splinters in unforetold places.",

    ### POOLS OF WATER (no effect)
    "pools of water": "Upon further inspection, certain chemicals from your previous experiments have leaked through the VENTS and drains. " 
        "How? You don’t know. But this is a problem.",

    ### CHEKHOV'S GUN (danger, key item)
    "chekhov's gun": {
        "item_desc": "You hold the gun in your hands. The most powerful weapon in the entire laboratory. Nostalgically, you remember that it "
            "only shoots modified METAL BULLETs of your own design. Of course, nothing in the entire world would ever require its "
            "immense power. You carefully drop it in your HAMMERSPACE anyway.",
        "effect": "inspect_prereq",
        "prereq": "hazard suit",
        "death_msg": "Wading through the pools of water, you begin to realize that the radiation is too much for your feeble body to handle. GAME OVER."
    },

    ### WOODEN FURNITURE ## HAS METAL BULLET
    # "new_item": This particular item has its flags changed, rather than the item inspected
    "wooden furniture": {
        "item_desc": "You once handcrafted all your tables and chairs with your grandchildren many summers ago. It is now beyond repair. " 
        "Amid the destruction, you find a single modified METAL BULLET. "
        "Old treasures are hard to come by, you stow it in your HAMMERSPACE.",
        "effect": "hammerspace_diff_item",
        "new_item": "metal bullet"
    },

    ### METAL BULLET (goes in inventory, key item)
    "metal bullet": "Old treasures are hard to come by, you stow it in your HAMMERSPACE.",

    ### GREEN VOMIT (danger)
    "green vomit": {
        "item_desc": "Inspecting the GREEN VOMIT, you find yourself becoming very woozy. " 
        "HER radioactive levels are too high for her own good. She’s sick. But it’s too late for you. " 
        "GAME OVER.",
        "effect": "inspect_kill"
    },

    ### VISCOUS LIQUID
    "viscous_liquid": "Trails of the liquid lead from tubes to the VENTS. You need to find her fast.",

    ### VENTS
    "vents": "You open the grate to the VENTS, but you are too large to fit inside. "  
        "SHE could be anywhere in the lab now.",

    ### HAZARD SUIT (key item)
    "hazard suit": "You always felt safe in one of these. Better put it on.",

    ### WET THUD (danger)
    # "wet thud": {
    #     "item_desc": "The sound you make in turning around alerts HER to your presence. In her manic rampage, she shreds you to pieces. GAME OVER.",
    #     "effect": "inspect_kill"
    # },

    # ### WET FOOTSTEPS (danger)
    # "wet footsteps": {
    #     "item_desc": "The sound you make in turning around alerts HER to your presence. In her manic rampage, she shreds you to pieces. GAME OVER.",
    #     "effect": "inspect_kill"
    # }
}

# Flags of important items the player must visit in order to progress.
item_flags = {
    # "name of item": boolean (Player has or hasn't visited this key item)
    
    ### BIG LEVER (key)
    "big lever": False,
    
    ### METAL DESK (key item)
    "metal desk": False
}

# Flags of important items the player must visit in order to progress.
# Distinguished from item_flags, as items in the hammerspace can be reviewed
# with the "inventory" command.
hammerspace_flags = {
    # "name of item": boolean (Player has or hasn't visited this key item)

    ### CHEKHOV'S GUN (danger, key item)
    "chekhov's gun": False,

    ### METAL BULLET (goes in inventory)
    "metal bullet": False,

    ### HAZARD SUITS (key item, on person)
    "hazard suit": False
}

world_rooms = {
    # '''
    # "dict_key": snake_case_string (the dictionary key of the Room object),
    #   "title": string (Title of the room that player will see),
    #   "room_desc": string (description of the room) or array of strings (locked, then unlocked descriptions)
    #   "connections": array of strings (keys of other Room dicts that the Player can enter)
    #   
    #   OTHER ROOM PARAMETERS
    #   "items": array of strings (Items the player can interact with)
    #   "key_item": string (Key for item that exists in one of the flag dictionaries, necessary for progress)
    #   "inspect_key": boolean (Needed to distinguish if a locked room has something that can be inspected to unlock it)
    # '''
    ### LABORATORY ANTECHAMBER
    "laboratory antechamber": {
        "title" : "Laboratory Antechamber",
        "room_desc" : "You enter your LABORATORY ANTECHAMBER. " 
            "It is as clean and organized as you had left it, perfect for patients to wait in. " 
            "Judging from the blaring red lights, the whole building is in lockdown. " 
            "This will not be as straightforward as you had hoped. "
            "There is a door leading to a long PASSAGE towards the rest of the building.",
        "connections" : ["passage"]
    },

    ### PASSAGE TO THE STUDY  
    "passage": {
        "title" : "30 ft Passage",
        "room_desc" : "The PASSAGE continues for another 30 feet. Sirens blare loudly. "
            "Along the wall there are several doors. "
            "One door leads to the CALITIS OFFICE, another to the CISTERN, and the last to the STUDY.",
        "connections" : ["laboratory antechamber", "calitis office", "cistern", "study"]
    },

    ### MR. CALITIS OFFICE
    "calitis office": {
        "title" : "The Calitis' Office",
        "room_desc" : "You notice claw marks leading to the office door. " 
            "Inside, the neatly stacked PILES OF PAPER are all shredded and seemingly tossed wildly across the room. " 
            "The WOODEN CHAIR is in pieces. The only thing left intact is the METAL DESK.",
        "connections" : ["passage"],
        "items": ["metal desk", "piles of paper", "wooden chair"]
    },

    ### CISTERN
    "cistern": {
        "title" : "The Cistern",
        "room_desc" : "The once pristine POOLS OF WATER in this room are now tainted with radioactive chemicals. " 
            "Probably the same that caused HER to freak out. On the opposite wall, across the POOLS OF WATER, hangs CHEKHOV’S GUN.",
        "connections" : ["passage"],
        "items": ["pools of water", "chekhov's gun"]
    },

    ### THE STUDY
    "study": {
        "title" : "The Study",
        "room_desc" : 
            #Locked Description
            ["The door to the STUDY is locked. The alphanumeric keypad glows red angrily as you press random codes.", 
            #Unlocked description
            "Inside is a mess. The WOODEN FURNITURE is wrecked. " 
            "Splotches of GREEN VOMIT lay strewn across the walls and floor. There is a door leading to the EXPERIMENTATION LAB."],
        "connections" : ["passage", "experimentation lab"],
        "key_item": "metal desk",
        "items": ["wooden furniture", "green vomit",]
    },

    ### EXPERIEMENTATION LAB ## Only has locked description
    "experimentation lab": {
        "title" : "The Experimentation Lab",
        "room_desc" : 
            #Locked Description
            ["The door to the labs is a heavy metal one. It’s locked. " 
            "There are no knobs to turn, only one BIG LEVER on the side of the wall.", 
            #Unlocked Description
            "There is glass everywhere. Lines of VISCOUS LIQUID streak from tubes along the floor. " 
            "You see a HAZARD SUIT hang untouched in one of the closets. There is also the door to the MACGUFFIN ROOM."],
        "connections" : ["study", "macguffin room"],
        "key_item": "big lever",
        "inspect_key": True,
        "items": ["viscous liquid", "vents", "hazard suit"]
    },

    # '''
    #   "specific_item": string (The specific sequence that must be inspected in order to continue, or else GAME OVER)
    #   "success_dest": string (Dictionary key for room upon successfully inspecting particular item)
    #   "death_msg": dictionary of strings (Death messages for inspecting a particular thing, as well as a default death message)
    # '''

    ### MACGUFFIN ROOM / MACGUFFIN 00
    "macguffin room": {
        "title" : "The Macguffin",
        "room_desc" : "You open the door to the MACGUFFIN. As you do so, you hear a WET THUD behind you. "
            "You feel a primal fear deep inside your heart. "
            "What do you inspect first?",
        "specific_item": "macguffin",
        "success_dest": "macguffin_01",
        "death_msg": {
            "wet thud": "The sound you make in turning around alerts HER to your presence. In her manic rampage, she shreds you to pieces. GAME OVER.",
            "11DEAFAULTDEATHMSG11": "Trying to interact with anything else causes HER to leap at you, ripping you to pieces. GAME OVER."
        }
    },

    ## MACGUFFIN 01
    "macguffin_01": {
        "title" : "5",
        "room_desc" : "You don’t remember designing the security measures like this, but the MACGUFFIN is encased in an incredibly large box. " 
            "Protecting the box, there is an ALPHANUMERIC KEYPAD and a LARGE LEVER. "

            "Since SHE is blind, SHE hasn’t noticed you yet. " 
            
            "Judging from the WET FOOTSTEPS and the sniffing behind you, you only have 5 seconds to administer the MACGUFFIN.",

        "specific_item": "alphanumeric keypad",
        "success_dest": "macguffin_02",
        "death_msg": {
            "wet footsteps": "The sound you make in turning around alerts HER to your presence. In her manic rampage, she shreds you to pieces. GAME OVER.",
            "chekhov's gun": "You swing CHEKHOV'S GUN toward HER. Point. Click. The gun isn’t loaded. She leaps at you, ripping you to pieces. GAME OVER",
            "large lever": "The lever doesnt budge. The alphanumeric keypad beeps angrily. Alerted by the sound, SHE leaps at you. GAME OVER.",
            "11DEAFAULTDEATHMSG11": "Trying to interact with anything else causes HER to leap at you, ripping you to pieces. GAME OVER."
        }
    },

    ## MACGUFFIN 02
    "macguffin_02": {
        "title" : "4",
        "room_desc" : "The keypad glows green. The first step is unlocked. " 
            "Hearing the pushing of buttons, SHE turns HER head toward you. "
            "The MACGUFFIN is still encased in an incredibly large box. " 
            "The ALPHANUMERIC KEYPAD glows green and a LARGE LEVER sits next to it. \n"

            "4 seconds left.",

        "specific_item": "large lever",
        "success_dest": "macguffin_03",
        "death_msg": {
            "chekhov's gun": "You swing CHEKHOV'S GUN toward HER. Point. Click. The gun isn’t loaded. She leaps at you, ripping you to pieces. GAME OVER",
            "11DEAFAULTDEATHMSG11": "Trying to interact with anything else causes HER to leap at you, ripping you to pieces. GAME OVER."
        }
    },

    ### MACGUFFIN 03
    "macguffin_03": {
        "title" : "3",
        "room_desc" : "You pull the lever, something inside clicks and the MACGUFFIN is revealed. You take the MACGUFFIN in your hand. "

            "Alerted by the clicking of the box’s mechanism, SHE cautiously stalks toward you. "
            "3 seconds left.",

        "specific_item": "metal bullet",
        "success_dest": "macguffin_04",
        "death_msg": {
            "chekhov's gun": "You swing CHEKHOV'S GUN toward HER. Point. Click. The gun isn’t loaded. She leaps at you, ripping you to pieces. GAME OVER",
            "11DEAFAULTDEATHMSG11": "Trying to interact with anything else causes HER to leap at you, ripping you to pieces. GAME OVER."
        }
    },

    ### MACGUFFIN 04
    "macguffin_04": {
        "title" : "2",
        "room_desc" : "You hastily load the METAL BULLET into CHEKHOV'S GUN. " 

            "You can feel HER breath on the back of your neck. " 
            "2 seconds left.",

        "specific_item": "chekhov's gun",
        "success_dest": "macguffin_05",
        "death_msg": {
            "macguffin": "You turn and rush to use the MACGUFFIN on HER, but her SCALES are too tough for the MACGUFFIN to pierce. "
                "SHE swipes at you with her claws. GAME OVER.",
            "chekhov's gun": "You swing CHEKHOV'S GUN toward HER. Point. Click. The gun isn’t loaded. She leaps at you, ripping you to pieces. GAME OVER",
            "11DEAFAULTDEATHMSG11": "Trying to interact with anything else causes HER to leap at you, ripping you to pieces. GAME OVER."
        }
    },

    ### MACGUFFIN 05
    "macguffin_05": {
        "title" : "1",
        "room_desc" : "You swing CHEKHOV'S GUN toward HER. Point. BANG! " 
            "The METAL BULLET flies through the air. You feel the recoil in your shoulder. " 
            "If you hadn’t been the original designer, your arm might have been ripped off. "

            "Your shot nearly misses but it strikes HER in her ACHILLES HEEL, denting HER scales and stunning HER temporarily. " 
            "The most powerful gun in existence should have done much more, but now is not the time to think about that. "  

            "The place where you struck HER left the smallest opening in HER defenses. "
            "1 second left. What do you do?",

        "specific_item": "macguffin",
        "success_dest": "macguffin_endgame",
        "death_msg": {
            "chekhov's gun": "You swing CHEKHOV'S GUN toward HER. Point. Click. The gun isn’t loaded. She leaps at you, ripping you to pieces. GAME OVER",
            "11DEAFAULTDEATHMSG11": "Trying to interact with anything else causes HER to leap at you, ripping you to pieces. GAME OVER."
        }
    },

    ### MACGUFFIN ENDGAME
    "macguffin_endgame": {
        "title" : "...silence...",
        "room_desc" : "Utilizing the opening in her ACHILLES HEEL, you use the MACGUFFIN. \n"
            "She calms down instantly. \n"
            "YOU WIN."
    }
}