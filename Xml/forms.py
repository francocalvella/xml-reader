from django import forms
from django import forms

class AlbumForm(forms.Form):
    title = forms.CharField(max_length=40)
    release_year = forms.DateField()
    author = forms.CharField(max_length=40)
    best_song = forms.CharField(max_length=40)
    
class XmlForm(forms.Form):
    xml = forms.FileField()