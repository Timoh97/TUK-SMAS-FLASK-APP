from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField


class PostForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    title = TextAreaField('Title')
    content = TextAreaField('Post')
    submit = SubmitField('Submit')