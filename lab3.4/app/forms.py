from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms import SubmitField

class FileForm(FlaskForm):
    file = FileField('file', validators=[
        FileRequired(),
        FileAllowed(['txt'])
    ])    
    submit = SubmitField('Найти слово!')