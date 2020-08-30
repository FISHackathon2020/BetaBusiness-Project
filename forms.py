from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class MainForm(FlaskForm):
    fname = StringField('First Name', validators=[
        DataRequired(), Length(min=1, max=20)])
    lname = StringField('Last Name', validators=[
        DataRequired(), Length(min=1, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    resume = FileField('Submit Resume (pdf only)', validators=[
        FileAllowed(['pdf'])])
    submit = SubmitField('Submit')
