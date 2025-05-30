from django import forms
from .models import Feedback

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)

class Feedback(forms.ModelForm):
    class Meta:
        model=Feedback
        field=['name','email','message']