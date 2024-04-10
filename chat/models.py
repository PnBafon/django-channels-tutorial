from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)



class Conversation(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    messages = models.ManyToManyField(Chat)


