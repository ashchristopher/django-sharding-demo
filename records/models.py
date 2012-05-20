from django.db import models

class Record(models.Model):
    business = models.ForeignKey('profiles.Business')
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=5)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bill(Record):
    pass


class Invoice(Record):
    pass
