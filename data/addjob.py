from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('Job name', validators=[DataRequired()])
    team_leader = IntegerField('Team leader ID', validators=[DataRequired()])
    work_size = StringField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField('Done')