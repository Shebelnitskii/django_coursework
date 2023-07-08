from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from main.models import Message
from config import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        messages = Message.objects.all()
        for message in messages:
            email = message.client.email
            subject = message.letter_subject
            body = message.letter_body

            send_mail(subject=subject, message=body, from_email=settings.EMAIL_HOST_USER, recipient_list=[email],
                      fail_silently=False)
