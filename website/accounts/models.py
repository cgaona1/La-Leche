from django.db import models

class Notification(models.Model):
    email = models.EmailField(max_length=50)
    remindTime = models.IntegerField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
