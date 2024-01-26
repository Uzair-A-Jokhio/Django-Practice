from django import forms

from myapp.models import Person

class logForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
