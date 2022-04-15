from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, Email


class ParameterForm(FlaskForm):
    width = IntegerField('Ширина: ', default=20, name='width')
    height = IntegerField('Высота: ', default=20, name='height')
    submit = SubmitField('Задать размер мира')
