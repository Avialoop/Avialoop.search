from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    from_location = StringField('Откуда', validators=[DataRequired()])
    to_location = StringField('Куда', validators=[DataRequired()])
    departure_date = DateField('Дата вылета', format='%Y-%m-%d', validators=[DataRequired()])
    return_date = DateField('Дата возвращения', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Поиск')