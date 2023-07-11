from django import forms
from django.forms import TimeInput, DateInput
from main.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['client', 'letter_subject', 'letter_body', 'mailing_time', 'periodicity', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }
def validate_time(value):
    try:
        forms.TimeField().clean(value)
    except forms.ValidationError:
        raise forms.ValidationError('Некорректное время')

#
# class MailingForm(forms.ModelForm):
#     class Meta:
#         model = Mailing
#         fields = ['mailing_time', 'periodicity', 'start_date', 'end_date']

