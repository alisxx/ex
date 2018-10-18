from django.db import models
from django.utils.encoding import force_bytes
from django import forms

def __str__(self):
    return force_bytes(self.name)
# Create your models here.
def __unicode__(self):
    return self.name

class EmailForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    botcheck = forms.CharField(max_length=5)
    message = forms.CharField()