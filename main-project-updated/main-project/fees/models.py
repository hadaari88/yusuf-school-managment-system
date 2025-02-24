
from django.db import models

class Fee(models.Model):
    date = models.DateField(auto_now_add=True)
    debit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return f"Fee on {self.date} - Amount: {self.amount}"
