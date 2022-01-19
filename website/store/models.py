from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.description}"

    def get_absolute_url(self):
        pass

    @classmethod
    def create(cls,user):
        User = cls(user = user, name = user.username, email = user.email)
        return User

class Product(models.Model):
    description = models.TextField()
    cost = models.TextField(max_length=300, default="")
    quanity = models.TextField(max_length=300, default="")
    image = models.ImageField(null=True, blank=True)
    body = models.TextField(default='Item Description',null=True, blank=True)
    size = models.IntegerField(default=8, null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def get_absolute_url(self): 
        return reverse('view', args=[str(self.id)])

