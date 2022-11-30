from flask_wtf import FlaskForm
import wtforms as ws

class StudentForm(FlaskForm):
    name = ws.StringField('ФИО студента', validators=[ws.validators.DataRequired(), ])
    birth_date = ws.DateField('Дата рождения', validators=[ws.validators.DataRequired(), ])

class UserForm(FlaskForm):
    username = ws.StringField('Имя полбзователя', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=4, max=20)
    ])
    password = ws.PasswordField('Пароль', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=8, max=24)
    ])

