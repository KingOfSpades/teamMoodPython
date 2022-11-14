from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Length, DataRequired

class Moods():
    def __init__(self):
        self.teamMoods = {}
    
    moods = {
        "Fantastic": {"description": "Fantastic", "color": "success", "icon": "🤩", "opacity": "bg-opacity-100"},
        "Great": {"description": "Great", "color": "success", "icon": "😄", "opacity": "bg-opacity-75"},
        "Good": {"description": "Good", "color": "success", "icon": "🙂", "opacity": "bg-opacity-50"},
        "Bad": {"description": "Bad", "color": "warning", "icon": "🙁", "opacity": "bg-opacity-100"},
        "Terrible": {"description": "Terrible", "color": "danger", "icon": "😡", "opacity": "bg-opacity-100"}
    }

    def moodMap(self):
        moodMap = {'count': 0, 'percentage': 0}
        for uuid, moods in self.moodMap:
            for mood in moods:
                pass
               # moodMap['count'] =  operator.countOf(moods, mood)
        return moodMap


class Mood(Moods):
    def __init__(self, name, mood, comment):
        self.mood = mood
        self.name = name
        self.comment = comment
        self.color = Moods.moods[mood]['color']
        self.icon = Moods.moods[mood]['icon']
        self.description = Moods.moods[mood]['description']
        self.opacity = Moods.moods[mood]['opacity']


class mood_form(FlaskForm):
    name = StringField("TextLabel")
    mood = RadioField('certification', 
        choices=[
            (Moods.moods['Fantastic']['description'], Moods.moods['Fantastic']['icon'] + " ( " + Moods.moods['Fantastic']['description'] + " )"), 
            (Moods.moods['Great']['description'], Moods.moods['Great']['icon'] + " ( " + Moods.moods['Great']['description'] + " )"),
            (Moods.moods['Good']['description'], Moods.moods['Good']['icon'] + " ( " + Moods.moods['Good']['description'] + " )"),
            (Moods.moods['Bad']['description'], Moods.moods['Bad']['icon'] + " ( " + Moods.moods['Bad']['description'] + " )"),
            (Moods.moods['Terrible']['description'], Moods.moods['Terrible']['icon'] + " ( " + Moods.moods['Terrible']['description'] + " )")],
            validators=[InputRequired()])
    comment = TextAreaField("TextLabel")

    submit = SubmitField("Submit")

teamMoods = {}

