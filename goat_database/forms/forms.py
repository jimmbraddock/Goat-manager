from wtforms import (
    Form,
    StringField,
    TextAreaField,
    validators,
    HiddenField,
    FileField
)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
from wtforms.widgets import HTMLString


def strip_filter(x):
    return x.strip() if x else ''


class MyFileInput:
    def __init__(self, img=''):
        self.img = img

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        html = list()
        html.append('''<input type='file' id='{0}' name='photo' onchange="readURL(this);" />
        <img id="blah" src="{1}" />'''.format(field.id, self.img))
        html.append(
            '''<script type="text/javascript">
     function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#blah')
                        .attr('src', e.target.result)
                        .width(150)
                        .height(150);
                };

                reader.readAsDataURL(input.files[0]);
            }
        }
</script>''')
        return HTMLString('\n'.join(html))


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
    photo = FileField(u'Фотография', widget=MyFileInput())


class GoatUpdateForm(GoatCreateForm):
    id = HiddenField()
