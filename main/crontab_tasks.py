from django.core.mail import send_mail

from config import settings
from main.models import Message, MailingLogs
from django.core.cache import cache


def daily_send():
    for item in Message.objects.filter(periodicity='daily'):
        item.status = 'started'
        item.save()
        send_mailing(item)
        item.status = 'completed'
        item.save()


def weekly_send():
    for item in Message.objects.filter(periodicity='weekly'):
        item.status = 'started'
        item.save()
        send_mailing(item)
        item.status = 'completed'
        item.save()


def monthly_send():
    for item in Message.objects.filter(periodicity='monthly'):
        item.status = 'started'
        item.save()
        send_mailing(item)
        item.status = 'completed'
        item.save()


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
            status = 'success'
            response = 'Email sent successfully'
        except Exception as e:
            status = 'error'
            response = str(e)
        MailingLogs.objects.create(mailing=message_item, attempt_status=status, mailserver_response=response)