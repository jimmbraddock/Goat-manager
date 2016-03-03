from wtforms import (
    Form,
    StringField,
    TextAreaField,
    validators,
    HiddenField
)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField


def strip_filter(x):
    return x.strip() if x else ''


class GoatCreateForm(Form):
    name = StringField('Имя', [validators.Length(min=1, max=255)],
                       filters=[strip_filter])
    date_of_birth = DateField('Дата рождения', id='datepicker',
                              format='%d.%m.%Y')
    birth_place = TextAreaField('Место рождения',
                                [validators.Length(min=1)],
                                filters=[strip_filter])
    breed = QuerySelectField('Порода', get_label='breed_name')
    gender = QuerySelectField('Пол', get_label='gender_name')
    father = QuerySelectField('Отец', get_label='name', allow_blank=True,
                              blank_text=u'-- Выберите отца --')
    mother = QuerySelectField('Мать', get_label='name', allow_blank=True,
                              blank_text=u'-- Выберите мать --')


class GoatUpdateForm(GoatCreateForm):
    id = HiddenField()
