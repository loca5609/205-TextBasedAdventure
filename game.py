from flask import Flask, render_template, flash, redirect, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import copy, game_classes_v2, game_data, jsonpickle, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
bootstrap = Bootstrap(app)

move_verbs = ["go", "enter", "move"]


def help():
    return "'The game uses a 'verb noun' format. \n"
    "'inspect [item]' = inspects that particular item \n"
    "'move [room]' = move to that particular room \n"
    "'inventory' = show items stored in your Hammerspace \n"
    "'help' = shows this exact dialogue again, in case you get stuck"


#Input form
class Input(FlaskForm):
    user_input = StringField('What now?', validators=[DataRequired()])
    submit = SubmitField('Submit')


#The game's home page
#Connects to the first room
@app.route('/')
def index():
    # Sets the starting state of the game
    game_state = game_classes_v2.GameState(
        game_classes_v2.Player(), "laboratory antechamber",
        game_data.world_rooms, game_data.world_items, game_data.item_flags,
        game_data.hammerspace_flags)

    session['player'] = jsonpickle.encode(game_state.player)
    session['current_room'] = game_state.current_room
    session['items_state'] = game_state.item_flags
    session['hammerspace_state'] = game_state.hammerspace_flags
    return render_template('start_page.html')


#Game logic
@app.route('/scene/<room>', methods=['GET', 'POST'])
def scene(room):
    form = Input()

    player = jsonpickle.decode(session['player'])
    game_state = game_classes_v2.GameState(
        player, session['current_room'], game_data.world_rooms,
        game_data.world_items, session['items_state'],
        session['hammerspace_state'])

    #Makes the room page URL-friendly
    url_id = game_state.url_friendly()

    if form.validate_on_submit():
        #Splits user input into "verb noun" format
        command = form.user_input.data.split(" ", 1)

        try:
            #Logic continues if valid verb, error otherwise

            if command[0] in move_verbs:
                #moves player into requested room, if possible
                game_state.move(command[1])
            elif command[0] == "inspect":
                game_state.inspect(command[1])
            #elif command[0] == "help":
            #   game_state.player.setMsg.(help())
            else:
                game_state.player.setMsg(
                    "I don't understand that command. Please try again.")
        except (IndexError):
            game_state.player.setMsg("Please enter a complete, valid command.")

        #Makes the room page URL-friendly
        url_id = game_state.url_friendly()

        session['player'] = jsonpickle.encode(game_state.player)
        session['current_room'] = game_state.current_room
        session['items_state'] = game_state.item_flags
        session['hammerspace_state'] = game_state.hammerspace_flags

        return redirect('/scene/' + url_id)

    #displays the HTML page

    return render_template(
        'render_room.html',
        player=game_state.player,
        current_room=game_state.get_room_data(),
        item_flags=game_state.item_flags,
        hammerspace_flags=game_state.hammerspace_flags,
        form=form)


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
