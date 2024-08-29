from django import forms
from .models import Mailing, Message

class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['start_datetime', 'periodicity', 'status', 'message', 'clients']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'periodicity': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Select(attrs={'class': 'form-control'}),
            'clients': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
