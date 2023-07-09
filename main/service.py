from django.conf import settings
from django.core.mail import send_mail
from main.models import Message

def send():
    # messages = Message.objects.all()
    # for message in messages:
    #     email = message.client.email
    #     subject = message.letter_subject
    #     body = message.letter_body
    email = 'Shebelnitskiy@gmail.com'
    subject = 'Тест Celery'
    body = 'Работает?'
    send_mail(subject=subject, message=body, from_email=settings.EMAIL_HOST_USER, recipient_list=[email],
                  fail_silently=False)