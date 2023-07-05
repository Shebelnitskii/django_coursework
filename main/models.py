import email

from django.db import models

NULLABLE = {'blank': True, 'null': True}
# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=100,  verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    surname = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)
    email = models.EmailField(max_length=100, verbose_name='Почта')
    comment = models.TextField(max_length=100, verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'Почта: {self.email}'

class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    letter_subject = models.CharField(verbose_name='Тема письма')
    letter_body = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.client.email} тема: {self.letter_subject}'

class Mailing(models.Model):
    CHOICES_PERIODICITY = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )

    STATUS_OPTIONS = (
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    )

    message = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name='Принадлежность', related_name='mailing')
    mailing_time = models.TimeField(verbose_name='Время отправки', default='12:00:00')
    periodicity = models.CharField(max_length=10, choices=CHOICES_PERIODICITY, verbose_name='Переодичность', default='daily')
    mailing_status = models.CharField(max_length=10, choices=STATUS_OPTIONS, verbose_name='Статус', default='created')



class MailingLogs(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    date_time_attempt = models.DateTimeField()
    attempt_status = models.CharField(max_length=255)
    mailserver_response = models.TextField(**NULLABLE)