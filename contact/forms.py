from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField

from django import forms
from django.forms import ModelForm
from .models import Contact
from .models import Email
from courses.models import New
from courses.models import Course
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('Name','email','phonenumber','massage','hunter')
class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ('email',)
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets={
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class' :'form control'}),




        } 
class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'
       
