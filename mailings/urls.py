from django.urls import path
from . import views

urlpatterns = [
    path('', views.MailingListView.as_view(), name='mailing_list'),
    path('create/', views.MailingCreateView.as_view(), name='mailing_create'),
    path('<int:pk>/', views.MailingDetailView.as_view(), name='mailing_detail'),
    path('<int:pk>/edit/', views.MailingUpdateView.as_view(), name='mailing_edit'),
    path('<int:pk>/delete/', views.MailingDeleteView.as_view(), name='mailing_delete'),
    path('messages/create/', views.MessageCreateView.as_view(), name='message_create'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
]
