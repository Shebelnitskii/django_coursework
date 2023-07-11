from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from main.forms import MessageForm
from main.models import Message, Client


# Create your views here.

def index(request):
    total_mailings_count = Message.objects.count()
    active_mailings_count = Message.objects.filter(mailing_status='started').count()
    unique_clients_count = Client.objects.annotate(messages_count=Count('messages')).filter(
        messages_count__gt=0).count()

    context = {
        'total_mailings_count': total_mailings_count,
        'active_mailings_count': active_mailings_count,
        'unique_clients_count': unique_clients_count,
    }

    return render(request, 'main/main_menu.html', context)


class MessageListView(generic.ListView):
    model = Message
    template_name = 'main/massage_list'
    context_object_name = 'message_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список рассылок'
        return context


class MessageCreateView(generic.CreateView):
    model = Message
    form_class = MessageForm
    # fields = ('client', 'letter_subject', 'letter_body', 'mailing_time', 'periodicity', 'start_date', 'end_date')

    def get_success_url(self):
        return reverse('main:message_list')


class MessageUpdateView(generic.UpdateView):
    model = Message
    form_class = MessageForm
    # fields = ('client', 'letter_subject', 'letter_body', 'mailing_time', 'periodicity', 'start_date', 'end_date')
    extra_context = {'extra_context': 'Изменить рассылку'}


    def get_success_url(self):
        return reverse('main:message_list')


class MessageDetailView(generic.DetailView):
    model = Message
    template_name = 'main/message_detail.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"О рассылке {self.object.client}"

        return context


class MessageDeleteView(generic.DeleteView):
    model = Message
    template_name = 'main/message_confirm_delete.html'
    permission_required = 'main.delete_message'
    extra_context = {'title': 'Подтвердить удаление'}

    def get_success_url(self):
        return reverse('main:message_list')

