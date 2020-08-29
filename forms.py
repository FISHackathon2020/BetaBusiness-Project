from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class MainForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=2, max=40)])