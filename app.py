from flask import Flask, render_template, request, redirect, url_for, session
import uuid

from mood import Names, Moods, Mood, mood_form, teamMoods

app = Flask(__name__)

app.config['SECRET_KEY'] = 'u/uGX8FzHMr9ijbuGz8B+Q'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Moods = Moods()
names = Names()

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", currentMoods=Moods.teamMoods, moodMap=Moods.moodMap())


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    form = mood_form()

    if "uuid" not in session:
        session['uuid'] = uuid.uuid4()

    if "name" not in session:
        session['name'] = names.names.pop()

    if request.method == 'POST':
        new_mood = Mood(
            form.name.data,
            form.mood.data,
            form.comment.data
        )
        Moods.teamMoods[session["uuid"]] = new_mood
        return redirect('/')
    
    if request.method == 'GET' and session['uuid'] in teamMoods:
        form.name.data = teamMoods[session['uuid']].name
        form.mood.data = teamMoods[session['uuid']].mood
        form.comment.data = teamMoods[session['uuid']].comment
    return render_template("mood.html", form=form, currentMoods=Moods.teamMoods, name=session['name'])


@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")