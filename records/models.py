from django.db import models

record_choices = (
    ('invoice', 'invoice'),
    ('bill', 'bill'),
)

class Record(models.Model):
    business = models.ForeignKey('profiles.Business')
    record_type = models.CharField(max_length=10, choices=record_choices)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=5)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {
            'pk' : self.pk, 
            'type' : self.record_type, 
            'quantity' : self.quantity,
            'price_per' : self.amount.to_eng_string(),
            'total_amount' : (self.quantity * self.amount).to_eng_string(),
        }
