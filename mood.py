from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Length, DataRequired

class Mood():
    def __init__(self, name, mood, comment):
        self.mood = mood
        self.name = name
        self.comment = comment

    def moodColor(self):
        color = ""
        icon = ""
        if self.mood == "Fantastic":
            color = "success"
            icon = "🤩"
        elif self.mood == "Great":
            color = "info"
            icon = "😄"
        elif self.mood == "Good":
            color = "light"
            icon = "🙂"
        elif self.mood == "Bad":
            color = "warning"
            icon = "🙁"
        elif self.mood == "Terrible":
            color = "danger"
            icon = "😡"
        else:
            color = "dark"
        return color, icon

moods = { "Fantastic", "Great", "Good", "Bad", "Terrible" }    

class mood_form(FlaskForm):
    name = StringField("TextLabel")
    mood = RadioField('certification', choices=[('Fantastic','🤩 (Fantasic)'),('Great','😄 (Great)'), ('Good', '🙂 (Good/Neutral)'), ('Bad', '🙁 (Bad)'), ('Terrible', '😡 (Terrible)')])
    comment = TextAreaField("TextLabel")

    submit = SubmitField("Submit")

teamMoods = {}

