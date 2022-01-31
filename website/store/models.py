from email.policy import default
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    cost = models.CharField(max_length=300, default="")
    # description = models.TextField(max_length=300, default="")
    quantity = models.CharField(max_length=300, default="")
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        pass
