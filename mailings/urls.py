from django.urls import path, include
from .views import MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView, MailingDetailView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, BlogListView, BlogDetailView

urlpatterns = [
    # Маршруты для рассылок
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),

    # Маршруты для клиентов
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    # Маршруты для сообщений
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_edit'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    # Маршруты для блога
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
