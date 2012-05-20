from django.db import models


class Account(models.Model):
    user_id = models.IntegerField()
    data = models.CharField(max_length=255)
