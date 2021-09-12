from django import forms
from .models import *


class EventForm(forms.ModelForm):
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
     'class': 'border border-secondary p-4',  'placeholder': 'Upload Image'
    }) ,label=(u'Upload Image'))

    event_name = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Enter Event Name'
    }))

    date = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Enter Date'
    }))

    time = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Enter Time'
    }))

    location = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Enter Location'
    }))


    class Meta:
        model = Event
        fields = ('image','event_name','date', 'time','location', )