from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Length, DataRequired


moods = { 
            "Fantastic": {"description": "Fantastic", "color": "succes", "icon": "🤩"},
            "Great": {"description": "Great", "color": "info", "icon": "😄"},
            "Good": {"description": "Good", "color": "light", "icon": "🙂"},
            "Bad": {"description": "Bad", "color": "warning", "icon": "🙁"},
            "Terrible": {"description": "Terrible", "color": "danger", "icon": "😡"}
        }  

class Mood():
    def __init__(self, name, mood, comment):
        self.mood = mood
        self.name = name
        self.comment = comment

    def moodColor(self):
        return moods[self.mood]['color']

    def moodSmiley(self):
        return moods[self.mood]['icon']
 

class mood_form(FlaskForm):
    name = StringField("TextLabel")
    mood = RadioField('certification', choices=[('Fantastic','🤩 (Fantasic)'),('Great','😄 (Great)'), ('Good', '🙂 (Good/Neutral)'), ('Bad', '🙁 (Bad)'), ('Terrible', '😡 (Terrible)')], validators=[InputRequired()])
    comment = TextAreaField("TextLabel")

    submit = SubmitField("Submit")

teamMoods = {}

