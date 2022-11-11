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
        if self.mood == "Fantastic":
            color = "success"
        elif self.mood == "Great":
            color = "info"
        elif self.mood == "Good":
            color = "light"
        elif self.mood == "Bad":
            color = "warning"
        elif self.mood == "Terrible":
            color = "danger"
        else:
            color = "dark"
        return color

moods = { "Fantastic", "Great", "Good", "Bad", "Terrible" }    

class mood_form(FlaskForm):
    name = StringField("TextLabel")
    mood = RadioField('certification', choices=[('Fantastic','Fantastic: I had a fantastic day'),('Great','Great: Today was great'), ('Good', 'Good/Neutral: It was a good day'), ('Bad', 'Bad: Today was a bad day'), ('Terrible', 'Terrible: A terrible day!')])
    comment = TextAreaField("TextLabel")

    submit = SubmitField("Submit")

teamMoods = {}

