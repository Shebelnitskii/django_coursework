from celery import shared_task
from django.conf import settings
from main.models import Message
from django.core.mail import send_mail


@shared_task
def send_email_task():
    messages = Message.objects.all()
    for message in messages:
        email = message.client.email
        subject = message.letter_subject
        body = message.letter_body

        send_mail(subject=subject, message=body, from_email=settings.EMAIL_HOST_USER, recipient_list=[email],
                  fail_silently=False)
