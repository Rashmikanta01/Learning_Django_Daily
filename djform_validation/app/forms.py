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
    reemail=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False,validators=[validate_email])

def clean(self):
    print(str(self.cleaned_data))
    se=self.cleaned_data['semail']
    re=self.cleaned_data['reemail']
    if se!=re:
        raise forms.ValidationError('Email and Re-Email must be same')
    
def clean_botcatcher(self):
    bot=self.cleaned_data['botcatcher']
    if len(bot)>0:
        raise forms.ValidationError('Bot detected')

