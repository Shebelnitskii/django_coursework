from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from main.forms import MessageForm, ClientForm
from main.models import Message, Client, MailingLogs
from blog.models import BlogPost
from random import sample


# Create your views here.

def index(request):
    total_mailings_count = Message.objects.count()
    active_mailings_count = Message.objects.filter(mailing_status='started').count()
    unique_clients_count = Client.objects.annotate(messages_count=Count('messages')).filter(
        messages_count__gt=0).count()
    active_posts = BlogPost.objects.filter(is_active=True)
    ### Проверка на количество случайных постов, при значении ниже 3 выводятся все посты на главную страницу
    if active_posts.count() >= 3:
        random_posts = sample(list(active_posts), 3)
    else:
        random_posts = active_posts

    context = {
        'total_mailings_count': total_mailings_count,
        'active_mailings_count': active_mailings_count,
        'unique_clients_count': unique_clients_count,
        'random_posts': random_posts,
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


class MessageCreateView(LoginRequiredMixin, generic.CreateView):
    model = Message
    form_class = MessageForm
    extra_context = {'title': 'Добавить рассылку'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        # Сохраняем объект Message
        message = form.save()
        # Привязываем клиентов, выбранных в форме, к сообщению
        clients = form.cleaned_data['client']
        message.client.set(clients)
        return redirect('main:message_list')

    def get_success_url(self):
        return reverse('main:message_list')


class MessageUpdateView(generic.UpdateView):
    model = Message
    form_class = MessageForm
    # fields = ('client', 'letter_subject', 'letter_body', 'mailing_time', 'periodicity', 'start_date', 'end_date')
    extra_context = {'extra_context': 'Изменить рассылку'}

    def form_valid(self, form):
        message = self.get_object()
        form.instance.owner = message.owner
        updated_message = form.save()
        clients = form.cleaned_data['client']
        updated_message.client.set(clients)
        return redirect('main:message_list')

    def get_success_url(self):
        return reverse('main:message_list')


def complete_mailing(request, pk):
    message = get_object_or_404(Message, id=pk)

    # Изменяем статус рассылки на 'completed'
    message.mailing_status = 'completed'
    message.save()

    return redirect('main:message_list')


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


class ClientCreateView(generic.CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'main/client_form.html'

    def get_success_url(self):
        return reverse('main:client_list')


class ClientListView(generic.ListView):
    model = Client
    template_name = 'main/client_list'
    context_object_name = 'client_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список клиентов'
        return context


class ClientDeleteView(generic.DeleteView):
    model = Client
    template_name = 'main/client_confirm_delete.html'
    permission_required = 'main.client_message'
    extra_context = {'title': 'Подтвердить удаление'}

    def get_success_url(self):
        return reverse('main:client_list')


class LogsListView(generic.ListView):
    model = MailingLogs
    template_name = 'main/mailinglogs_list'
    context_object_name = 'mailinglogs_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Логи рассылки'
        return context


class LogsDetailView(generic.DetailView):
    model = MailingLogs
    template_name = 'main/mailinglogs_detail.html'
    context_object_name = 'mailing_log'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Отчёты по рассылке"
        return context
