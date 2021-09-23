from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Stocks(models.Model):
    """ This Model is to keep track of all stocks a user currently has. """

    Symbol = models.CharField(max_length=10)
    Name = models.CharField(max_length=250)
    Shares = models.PositiveIntegerField()
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Symbol

class Transactions(models.Model):
    """ This model is to keep track of all of the transactions the user has made. """

    TRANSACTION_TYPES = [
        ('BUY', 'BUY'),
        ('SELL', 'SELL')
    ]

    Symbol = models.CharField(max_length=10)
    Name = models.CharField(max_length=250)
    Shares = models.PositiveIntegerField()
    Price = models.PositiveIntegerField()
    TransactionDateTime = models.DateTimeField(auto_now_add=True)
    TransactionType = models.CharField(max_length=4, choices=TRANSACTION_TYPES)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Symbol

class User_Finances(models.Model):
    """ This model is to keep track of the users finances. """

    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Current_Balance = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.User)
        


