from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class ContactForm(FlaskForm):
    name = StringField(label = 'Name')
    email = StringField(label = 'Email Address')
    subject = StringField(label = 'Subject')
    message = TextAreaField(label = 'Message')
    submit = SubmitField(label = 'Send')