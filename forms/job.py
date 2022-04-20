from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, BooleanField, SelectField
from wtforms.validators import DataRequired
from data import db_session


class JobForm(FlaskForm):
    db_sess = db_session.create_session()
    users = db_sess.query().all()
    team_leader = SelectField('Team Leader', choices=[(user.id, user.surname) for user in users],
                              validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = IntegerField('Время на работу', validators=[DataRequired()])
    collaborators = StringField('ID участников', validators=[DataRequired()])
    is_finished = BooleanField('Работа закончена')
    end_time = DateField('Дата завершения')


