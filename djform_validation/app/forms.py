from django import forms

def validate_form(value):
    if  value[0].isupper() and len(value)<6:
        raise forms.ValidationError('Name should not be in lowercase')

def validate_email(value):
    if not value.endswith('@gmail.com'):
        raise forms.ValidationError('Email must be a gmail address')


class StudentForm(forms.Form):
    sname=forms.CharField(validators=[validate_form])
    sage=forms.IntegerField()
    semail=forms.EmailField()