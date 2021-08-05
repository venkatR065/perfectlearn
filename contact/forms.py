from django import forms
from django.forms import ModelForm
from .models import Contact
from .models import Email
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('Name','email','phonenumber','massage','hunter')
