from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Length
import random

class Names():

    colors = ['Red', 'Green', 'Yellow', 'Blue', 'Purple', 'Static', 'Electric', 'Amazing', 'Ninja']
    animals = ['Vox', 'Bird', 'Snake', 'Bever', 'Turtle']

    names = []
    for color in colors:
        for animal in animals:
            names.append(color + " " + animal)

    def randomName(self):
        name = ""
        if self.names:
            name = self.names.pop(random.randint(0,len(Names.names)-1))
        else:
            name = "We have no names, man. No names. We are nameless!"
        return name



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
        moodMap = {
            'Fantastic': {'count': 0, 'percentage': 0 },
            'Great': {'count': 0, 'percentage': 0 },
            'Good': {'count': 0, 'percentage': 0 },
            'Bad': {'count': 0, 'percentage': 0 },
            'Terrible': {'count': 0, 'percentage': 0 },
            }
        
        for uuid, mood in self.teamMoods.items():
            moodMap[mood.mood]['count'] += 1
        
        for mood in moodMap:
            try:
                moodMap[mood]['percentage'] = (moodMap[mood]['count'] / len(self.teamMoods)) * 100
            except:
                moodMap[mood]['percentage'] = 0

        return moodMap


class Mood():
    def __init__(self, name, mood, comment):
        self.mood = mood
        self.name = name
        self.comment = comment
        self.color = Moods.moods[mood]['color']
        self.icon = Moods.moods[mood]['icon']
        self.description = Moods.moods[mood]['description']
        self.opacity = Moods.moods[mood]['opacity']


class mood_form(FlaskForm):
    name = StringField("Name", render_kw={'readonly': True})
    mood = RadioField('Mood', 
        choices=[
            (Moods.moods['Fantastic']['description'], Moods.moods['Fantastic']['icon'] + " ( " + Moods.moods['Fantastic']['description'] + " )"), 
            (Moods.moods['Great']['description'], Moods.moods['Great']['icon'] + " ( " + Moods.moods['Great']['description'] + " )"),
            (Moods.moods['Good']['description'], Moods.moods['Good']['icon'] + " ( " + Moods.moods['Good']['description'] + " )"),
            (Moods.moods['Bad']['description'], Moods.moods['Bad']['icon'] + " ( " + Moods.moods['Bad']['description'] + " )"),
            (Moods.moods['Terrible']['description'], Moods.moods['Terrible']['icon'] + " ( " + Moods.moods['Terrible']['description'] + " )")],
            validators=[InputRequired()])
    comment = TextAreaField("Comment", validators=[Length(max=750)])

    submit = SubmitField("Submit")
