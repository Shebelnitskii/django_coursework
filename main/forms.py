from django import forms
from main.models import Message, Client


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['client', 'letter_subject', 'letter_body', 'mailing_time', 'periodicity']
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.pk:  # Проверяем, новый ли это объект или существующий
            instance.owner = self.user
        if commit:
            instance.save()
        return instance


def validate_time(value):
    try:
        forms.TimeField().clean(value)
    except forms.ValidationError:
        raise forms.ValidationError('Некорректное время')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'first_name']
