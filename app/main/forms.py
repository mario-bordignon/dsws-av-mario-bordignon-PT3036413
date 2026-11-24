from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class ProfessorForm(FlaskForm):
    nome = StringField('Cadastre o novo Professor:',
                       validators=[DataRequired(), Length(max=64)])
    disciplina = SelectField('Disciplina associada:', coerce=int)
    submit = SubmitField('Cadastrar')
