item_list = [
    '''
    "dict_key": snake_case_string (the dictionary key of the Item object),
    "name": string (name of the item),
    "dialogue": string (dialogue shown when Inspecting the item),
    "effect": string/none (what effect this item does when Inspect, other than the default inspect function)
    '''
	{
	}
]

room_list = [
    '''
    "dict_key": snake_case_string (the dictionary key of the Room object),
    "title": string (Title of the room that player will see),
    "room_desc": string (description of the room),
    "connections": array of strings (keys of other Room objects that the Player object can enter),
    "item_key": string/None (key of item that must be visited in order to enter this Room, or None if no Item is required),
    "items": string/None (keys of items that player can interact with inside this Room, or None if no Items exist in room),
    "url": None (URL of the image associated with room; you do not need to enter a value here)
    '''
    {
    "dict_key": "lab",
    "title" : "Scientist's Laboratory",
    "room_desc" : "sdfsdfasdfdsa",
    "connections" : ["passage"],
    "item_key": "blah",
    "items": "Item blah???"
    }
]