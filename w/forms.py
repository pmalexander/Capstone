from wtforms import Form, BooleanField, StringField, PasswordField, validators

class Search_Query(Form):
    search = StringField('search')
    submit = Submitfield('Find')
    
'''dummied out in favor of wtform, Flask
from django import forms

#come back to this, look setup class for search query
class Location(forms.form):
location_name = forms.