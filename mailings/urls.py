from django.urls import path
from .views import (
    MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView,
    MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView,
    ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView
)

urlpatterns = [
    # URLs for Mailing
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    # URLs for Message
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_edit'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    # URLs for Client
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]
