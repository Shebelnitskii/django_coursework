from django import forms

from main.models import Message, Mailing


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['client', 'letter_subject', 'letter_body']

def validate_time(value):
    try:
        forms.TimeField().clean(value)
    except forms.ValidationError:
        raise forms.ValidationError('Некорректное время')

class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['mailing_time', 'periodicity']

