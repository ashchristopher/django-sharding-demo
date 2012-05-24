from django.db import models


class Business(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=120)
    shard = models.CharField(max_length=120)
