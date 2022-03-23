from django.db import models

class Notification(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email