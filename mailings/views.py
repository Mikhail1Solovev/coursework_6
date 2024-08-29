from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Mailing, Message, Client
from .forms import MailingForm, MessageForm, ClientForm
from .services import send_mailing

# Views for Mailing
class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_list.html'

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing_create.html'
    success_url = reverse_lazy('mailing_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing_update.html'
    success_url = reverse_lazy('mailing_list')

class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing_detail.html'

class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing_delete.html'
    success_url = reverse_lazy('mailing_list')

# Views for Message
class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_create.html'
    success_url = reverse_lazy('message_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_update.html'
    success_url = reverse_lazy('message_list')

class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('message_list')

# Views for Client
class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_create.html'
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_update.html'
    success_url = reverse_lazy('client_list')

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')
