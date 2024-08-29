from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Mailing, Message, Client
from .forms import MailingForm

class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_list.html'

class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing_detail.html'

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing_create.html'
    success_url = reverse_lazy('mailing_list')

class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing_edit.html'
    success_url = reverse_lazy('mailing_list')

class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing_delete.html'
    success_url = reverse_lazy('mailing_list')

# Сообщения
class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'

class MessageCreateView(CreateView):
    model = Message
    fields = ['subject', 'body']
    template_name = 'message_create.html'
    success_url = reverse_lazy('message_list')

class MessageUpdateView(UpdateView):
    model = Message
    fields = ['subject', 'body']
    template_name = 'message_edit.html'
    success_url = reverse_lazy('message_list')

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('message_list')

# Клиенты
class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'

class ClientCreateView(CreateView):
    model = Client
    fields = ['email', 'full_name', 'comment']
    template_name = 'client_create.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['email', 'full_name', 'comment']
    template_name = 'client_edit.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')
