import logging
from wtforms import (
    Form,
    StringField,
    TextAreaField,
    validators,
    HiddenField
)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
from wtforms.widgets.core import HTMLString, html_params


log = logging.getLogger(__name__)
strip_filter = lambda x: x.strip() if x else ''


class SelectDateWidget(object):
    def __call__(self, field, **kwargs):
        html = '<input type="text" id="datepicker" value="{}" {}>'.format(field.data, html_params(**kwargs))
        return HTMLString(''.join(html))


class GoatCreateForm(Form):
    name = StringField('Имя', [validators.Length(min=1, max=255)],
                       filters=[strip_filter])
    date_of_birth = DateField('Дата рождения', id='datepicker', format='%d.%m.%Y')
    birth_place = TextAreaField('Место рождения', [validators.Length(min=1)],
                                filters=[strip_filter])
    breed = QuerySelectField('Порода', get_label='breed_name')
    gender = QuerySelectField('Пол', get_label='gender_name')


class GoatUpdateForm(GoatCreateForm):
    id = HiddenField()
