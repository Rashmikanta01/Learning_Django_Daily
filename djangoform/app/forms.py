from django import forms

g=[('MALE','male'),('FEMALE','female')]
c=[('python','python'),('django','django'),('sql','sql')]
class StudentDjForm(forms.Form):
    stname=forms.CharField()
    stage=forms.IntegerField()
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':20}))

#