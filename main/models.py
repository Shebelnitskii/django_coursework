import email

from django.db import models
from django.utils.datetime_safe import date

NULLABLE = {'blank': True, 'null': True}
# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=100,  verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    surname = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)
    email = models.EmailField(max_length=100, unique=True, verbose_name='Почта')
    comment = models.TextField(max_length=100, verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return self.email

class Message(models.Model):
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

    letter_subject = models.CharField(verbose_name='Тема письма')
    letter_body = models.TextField(verbose_name='Тело письма')

    mailing_time = models.TimeField(verbose_name='Время отправки', default='12:00:00')
    periodicity = models.CharField(max_length=10, choices=CHOICES_PERIODICITY, verbose_name='Периодичность рассылки', default='daily')
    mailing_status = models.CharField(max_length=10, choices=STATUS_OPTIONS, verbose_name='Статус', default='created')
    start_date = models.DateField(default=date.today, verbose_name='Дата начала рассылки')
    end_date = models.DateField(default=date.today, verbose_name='Дата окончания рассылки')
    client = models.ManyToManyField('Client', verbose_name='Клиенты', related_name='messages')

    def __str__(self):
        return f'Тема: {self.letter_subject}'


class MailingLogs(models.Model):
    mailing = models.ForeignKey(Message, on_delete=models.CASCADE)
    date_time_attempt = models.DateTimeField()
    attempt_status = models.CharField(max_length=255)
    mailserver_response = models.TextField(**NULLABLE)