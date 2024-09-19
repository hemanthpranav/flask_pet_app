 
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class PetForm(FlaskForm):
    name = StringField('Pet Name', validators=[DataRequired()])
    type = StringField('type', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Add Pet')