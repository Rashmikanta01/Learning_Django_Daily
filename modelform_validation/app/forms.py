
from django import forms
from .models import *  # Replace with your actual model

class StudentMF(forms.ModelForm):
    class Meta:
        model = Student  # Replace with your actual model
        fields = '__all__'  # Or specify the fields you want to include
    reemail = forms.EmailField()
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    def clean(self):
        se=self.cleaned_data['email']
        sre=self.cleaned_data['reemail']
        if se!=sre:
            raise forms.ValidationError("Email and Re-enter Email must match.")
        
    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("Bot detected")
        