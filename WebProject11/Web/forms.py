from django import forms
from .models import FormEnteriesModel


class EntryForm(forms.ModelForm):
    options = (
        ('General', 'General'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC')
    )

    choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    rollno = forms.IntegerField()
    category = forms.CharField(widget=forms.Select(choices=options, attrs={'class': 'form-control'}))
    gender = forms.CharField(widget=forms.Select(choices=choices, attrs={'class': 'form-control'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = FormEnteriesModel
        fields = ['name', 'rollno', 'category', 'gender','state']