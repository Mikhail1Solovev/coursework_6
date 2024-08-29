from django.contrib import admin
from .models import Message, Client, Mailing

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body')
    search_fields = ('subject',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment')
    search_fields = ('email', 'full_name')

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('start_datetime', 'periodicity', 'status')
    search_fields = ('status',)
