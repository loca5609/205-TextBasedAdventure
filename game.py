from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import copy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

#FORFUN:
#Add a favicon

class Player:
  def __init__(self, score, current_room, inventory, message=None):
    self.score = score
    self.current_room = current_room
    self.inventory = inventory
    self.message = message

  def setMessage(self, new_message):
    self.message = new_message

  def getScore(self):
    return self.score

  def addScore(self):
    self.score += 1

class GameState:
  def __init__(self, item_list, room_list, player):
    self.item_list = item_list
    self.room_list = room_list
    self.player = player

  def setRoom(self, destination):
    return self.room_list[destination]

move_verbs = ["go", "enter", "move"]

world = GameState(item_index, room_index, Player(0, room_index["laboratory antechamber"], None))

#Input form
class Input(FlaskForm):
  user_input = StringField('What now?', validators=[DataRequired()])
  submit = SubmitField('Submit')

#The game's home page
#Connects to the first room
@app.route('/')
def index():
  return render_template('start_page.html')


#Game logic
@app.route('/scene/<room>', methods = ['GET', 'POSt'])
def scene(room):
  form = Input()

  #Makes the room page URL-friendly
  url_id = world.player.current_room.setURL()

  if form.validate_on_submit():
    #Splits user input into "verb noun" format
    command = form.user_input.data.split(" ", 1)

    #Logic continues if valid move verb, error otherwise
    if command[0] in move_verbs:
      #moves player into requested room
      move_to(command[1], world)
    elif command[0] == "inspect":
      inspect(command[1], world)
    else:
      world.player.setMessage("I don't understand that command. Please try again.")

    #Makes the room page URL-friendly
    url_id = world.player.current_room.setURL()

    return redirect('/scene/' + url_id)

  #displays the HTML page
  return render_template('render_room.html', player = world.player, current_room = world.player.current_room, form = form)