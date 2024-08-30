from django.contrib import admin
from .models import Mailing, Message, Client, MailingAttempt

class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_datetime', 'periodicity', 'status', 'owner')
    list_filter = ('status', 'periodicity')
    search_fields = ('status', 'owner__username')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'owner')
    search_fields = ('subject', 'owner__username')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'owner')
    search_fields = ('full_name', 'email', 'owner__username')

admin.site.register(Mailing, MailingAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(MailingAttempt)
