from django import forms
from .models import Grade, Ascent


"""
A form in django simplifies massively HTML forms (clearly through black magic)

You set up here which Model you want to show as a form, as well as its different attributs.
Said attributs can be tuned just like you'd do in HTML/CSS
for example, here 'name' is supposed to be a non required input,
and 'date_uploaded' is changed from being a normal text input to being a true date input.
"""
class AscentForm(forms.ModelForm):
    
    name = forms.CharField(required=False)
    date_uploaded = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))

    class Meta:
        model = Ascent
        fields = ('name','grade','date_uploaded','video')