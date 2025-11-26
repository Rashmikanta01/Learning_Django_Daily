from django import forms
from app.models import school

class schoolMF(forms.ModelForm):
    class Meta:
        model = school
        fields = '__all__'