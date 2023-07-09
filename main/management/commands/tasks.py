from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from main.models import Message
from config import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        email = 'Shebelnitskiy@gmail.com'
        subject = 'Тест Celery'
        body = 'Работает?'
        send_mail(subject=subject, message=body, from_email=settings.EMAIL_HOST_USER, recipient_list=[email],
                  fail_silently=False)
