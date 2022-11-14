from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Length, DataRequired

class Moods():
    def __init__(self):
        self.Fantastic = {"description": "Fantastic", "color": "succes", "icon": "🤩"}
        self.Great = {"description": "Great", "color": "info", "icon": "😄"}
        self.Good = {"description": "Good", "color": "light", "icon": "🙂"}
        self.Bad = {"description": "Bad", "color": "warning", "icon": "🙁"}
        self.Terrible = {"description": "Terrible", "color": "danger", "icon": "😡"}

    def moodColor(self, mood):
        return self.mood['color']

    def moodSmiley(self, mood):
        return self.mood['icon']
        
class Mood():
    def __init__(self, name, mood, comment):
        self.mood = mood
        self.name = name
        self.comment = comment


class mood_form(FlaskForm):
    name = StringField("TextLabel")
    mood = RadioField('certification', choices=[('Fantastic','🤩 (Fantasic)'),('Great','😄 (Great)'), ('Good', '🙂 (Good/Neutral)'), ('Bad', '🙁 (Bad)'), ('Terrible', '😡 (Terrible)')], validators=[InputRequired()])
    comment = TextAreaField("TextLabel")

    submit = SubmitField("Submit")

teamMoods = {}

