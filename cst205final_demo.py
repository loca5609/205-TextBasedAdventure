from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import copy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

#previous_room = "castle_hall"

move_verbs = {
  "go": True,
  "enter": True,
  "move": True
}

#Couldn't quite figure out how to implement my own key system, but added a score system instead that increments
#if they have not visited the room before.

room_info = {
  "score": 0,
  "current_location": "castle_hall",
  "error": None,
  "castle_hall": {
    #Room 0 - Castle Hall
    "room_title": "Castle Hall",
    "room_connections": {
      "key_room": "Check out the key room.",
      "throne_room": "Proceed to the throne room."
    },
    "descriptions": ["You are in the castle hall. The west room goes to the ", " and the north room goes to the ", "."],
    "bolds": ["key room", "throne room"],
    "tags": {
      "hall": True,
      "castle hall": True
    },
    "visited": False,
    "locked": False
  },
  "key_room": {
    #Room 1 - Key Room
    "room_title": "Key Room",
    "room_connections": {
      "castle_hall": "Go back to the castle hall.",
      "throne_room": "Search for the throne room key."
    },
    "descriptions": ["The key room... what a fitting name. You're sure you can find a key for the throne room here. You can go back to the ", ", if you wish."],
    "bolds": ["castle hall"],
    "tags": {
      "key room": True
    },
    "visited": False,
    "locked": False
  },
  "throne_room": {
    "room_title": "Throne Room",
    #Room 2 - Throne Room
    "room_connections": {
      "castle_hall": "Go back to the castle hall."
    },
    "descriptions": ["You made it to the end of the game!!!!"],
    "bolds": None,
    "tags": {
      "throne": True,
      "throne room": True
    },
    "visited": False,
    "locked": True
  }
}

game_state = copy.deepcopy(room_info)

class Input(FlaskForm):
  user_input = StringField('What now?', validators=[DataRequired()])
  submit = SubmitField('Submit')


@app.route('/')
def index():
  return render_template('final_index.html', room_id = "castle_hall")

@app.route('/scene/<room>', methods = ['GET', 'POSt'])
def scene(room):
  form = Input()
  if game_state[room]["visited"] == False:
    game_state["score"] += 1
    game_state[room]["visited"] = True

  game_state["current_location"] = room
  #if (previous_room != game_state["current_location"]):
  #  game_state["error"] = None

  valid_verb = False

  if form.validate_on_submit():
    broken_statement = form.user_input.data.split(" ", 1)
    if broken_statement[0] in move_verbs:
      valid_verb = True
    else:
      game_state["error"] = "I don't understand that command. Please try again."
    if valid_verb:
      valid_location = False
      for room_option, room_desc in game_state[room]["room_connections"].items():
        if (broken_statement[1] in game_state[room_option]["tags"]):
          #previous_room = game_state["current_location"]
          if (game_state[room_option]["locked"] == False):
            game_state["current_location"] = room_option
            valid_location = True
            break
      
      if valid_location == False: 
        game_state["error"] = "I don't think that room is accessible."
    return redirect('/scene/' + game_state["current_location"])

  connection_size = len(game_state[room]["room_connections"])

  return render_template('room_connection.html', game_info = game_state, form = form)