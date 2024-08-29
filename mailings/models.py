from django.db import models
from django.contrib.auth.models import User

class MailingAttempt(models.Model):
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE)
    attempt_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Attempt at {self.attempt_datetime} for {self.mailing}"

class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Добавьте поле owner

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Mailing(models.Model):
    PERIODICITY_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    start_datetime = models.DateTimeField()
    periodicity = models.CharField(max_length=20, choices=PERIODICITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f"Рассылка на {self.start_datetime}"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
