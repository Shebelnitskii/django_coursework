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
        return f'Имя: {self.first_name}\nФамилия: {self.last_name}\nПочта: {self.email}'

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

    mailing_time = models.TimeField()
    periodicity = models.IntegerField(choices=CHOICES_PERIODICITY)
    mailing_status = models.IntegerField(choices=STATUS_OPTIONS)

class Massage(models.Model):
    letter_subject = models.CharField(verbose_name='Тема письма')
    letter_body = models.CharField(verbose_name='Тело письма')

class MailingLogs(models.Model):
    date_time_attempt = models.DateTimeField()
    attempt_status = models.CharField(max_length=255)
    mailserver_response = models.TextField(**NULLABLE)