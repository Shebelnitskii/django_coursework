from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from main.models import Message
from config import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in Message.objects.filter(periodicity='daily'):
            send_mailing(item)

def send_mailing(message_item: Message):
    # Получаем список email-адресов клиентов, которым нужно отправить рассылку
    clients_emails = message_item.client.values_list('email', flat=True)

    # Отправляем письмо каждому клиенту
    for email in clients_emails:
        try:
            send_mail(
                message_item.letter_subject,  # Тема письма
                message_item.letter_body,  # Тело письма
                settings.EMAIL_HOST_USER,  # От кого отправляем письмо
                [email],  # Кому отправляем письмо
                fail_silently=False,
            )
        except Exception as e:
            response = str(e)