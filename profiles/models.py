from django.db import models


class Business(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=120)
    
class ShardInfo(models.Model):
    shard = models.CharField(max_length=120)
    business = models.OneToOneField('Business')
