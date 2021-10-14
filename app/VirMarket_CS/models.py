from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

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

    class TRANSACTION_TYPES(models.TextChoices): 
        BUY = 'BUY', _('BUY')
        SELL = 'SELL', _('SELL') 
    

    Symbol = models.CharField(max_length=10)
    Name = models.CharField(max_length=250)
    Shares = models.PositiveIntegerField()
    Price = models.DecimalField(max_digits=20, decimal_places=2)
    TransactionDateTime = models.DateTimeField(auto_now_add=True)
    TransactionType = models.CharField(max_length=4, choices=TRANSACTION_TYPES.choices)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Symbol

class User_Finances(models.Model):
    """ This model is to keep track of the users finances. """

    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Current_Balance = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.User)
        


