from django.db import models


class Account(models.Model):
    business = models.ForeignKey('profiles.Business')
    name = models.CharField(max_length=255)
