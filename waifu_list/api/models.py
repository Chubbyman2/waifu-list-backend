from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Waifu(models.Model):
    name = models.CharField(max_length=50)
    anime = models.CharField(max_length=100)
    rank = models.IntegerField(default=0)
    description = models.TextField()
    image = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name