from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    participants = models.ManyToManyField(User,
                                          related_name='threads',
                                          limit_choices_to={'participants__count': 2})
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
