from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField,validators


class ContactForm(FlaskForm):
  name=StringField('Name(Required)',[validators.Length(min=5, max=10)])
  email=StringField('Email Address(Required)',[validators.Length(min=6,max=20)])
  subject=StringField('Subject(Required)',[validators.Length(min=5, max=10)])
  message =TextAreaField('Message(Required)',[validators.Length(min=20, max=40)])

