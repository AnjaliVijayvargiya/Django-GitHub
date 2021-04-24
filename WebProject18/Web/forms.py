from django import forms
from datetime import date
from datetime import datetime

from .models import EntryModel

class EntryForm(forms.ModelForm): 
    name = forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder': 'Write Your Name'}))
    rollno = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width:30ch','placeholder': 'Write Your Roll Number'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder': 'Write Your Category'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'style': 'width:29ch','placeholder': 'Write Your Email ID'}))
    gender_choices = [('Male','Male'),('Female','Female'),]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender_choices)
    date = forms.DateField(widget=forms.SelectDateWidget, initial=date.today)
    time = forms.TimeField(initial=datetime.now().strftime("%H:%M:%S"))
    
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':42,'placeholder': 'Write Comments'}))
    agree = forms.BooleanField()

    """ model_choice = forms.ModelChoiceField(
        queryset = EntryModel.objects.all(),
        initial = 0
        ) """

    class Meta: 
        model = EntryModel
        """ widgets = { 
            'description': forms.Textarea(attrs={'placeholder': 'Write Comments'}),
        } """
        fields = "__all__"