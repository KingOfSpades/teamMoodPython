from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from mood import Mood, mood_form, teamMoods

app = Flask(__name__)

app.config['SECRET_KEY'] = 'u/uGX8FzHMr9ijbuGz8B+Q'

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", currentMoods=teamMoods)


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    form = mood_form()
    if request.method == 'POST':
        new_mood = Mood(
            form.name.data,
            form.mood.data,
            form.comment.data
        )
        teamMoods.append(new_mood)
        return redirect('/')
    return render_template("mood.html", form=form, currentMoods=teamMoods )


@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")