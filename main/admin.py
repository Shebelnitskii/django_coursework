from django.contrib import admin
from .models import Client, Message, MailingLogs


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'surname', 'email', 'comment',)
    list_filter = ('email',)
    search_fields = ('first_name', 'email')


admin.site.register(Client, ClientAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('letter_subject', 'letter_body', 'mailing_time', 'periodicity', 'mailing_status')
    list_filter = ()


admin.site.register(Message, MessageAdmin)


class MailingLogsAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'date_time_attempt', 'attempt_status', 'mailserver_response')


admin.site.register(MailingLogs, MailingLogsAdmin)
