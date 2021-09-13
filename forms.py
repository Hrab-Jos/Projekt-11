from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class NotifikaceForm(FlaskForm):
    header = StringField('Nadpis', validators=[DataRequired()])
    message = StringField('Zpráva')
    submit = SubmitField('Odeslat')