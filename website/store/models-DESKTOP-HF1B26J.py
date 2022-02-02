from django.db import models


# Create your models here.


class Store (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.TextField(max_length=300, default="")
    quanity = models.TextField(max_length=300, default="")
    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}, {self.description}"

    def get_absolute_url(self):
        pass
