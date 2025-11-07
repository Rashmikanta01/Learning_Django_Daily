from django import forms

from app.models import *
class TopicMF(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
        
class WebpageMF(forms.ModelForm):
    class Meta:
        model=WebPage
        fields='__all__'

class AccessMF(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'

class CountriesMF(forms.ModelForm):
    class Meta:
        model=Countries
        fields='__all__'   