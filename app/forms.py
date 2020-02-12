from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField,validators


class ContactForm(Form):
name=StringField('Name',[validators.Length(min=5, max=10)])
email=StringField('Email Address',[validators.Length(min=6,max=20)])
subject=StringField('Subject',[validators.Length(min=5, max=10)])
message =('Message',[validators.Length(min=20, max=40)])

