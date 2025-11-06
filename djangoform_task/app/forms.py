from django import forms

class TopicDjForm(forms.Form):
    topic_name=forms.CharField()
    
