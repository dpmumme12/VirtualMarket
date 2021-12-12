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

    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    Current_Balance = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.User)

class User_Finance_History(models.Model):
    CreatedOn = models.DateTimeField(auto_now_add=True)
    Balance = models.DecimalField(max_digits=20, decimal_places=2)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.User_id)


### Custom permisions models ###

class user_roles(models.Model):
    class Meta:
        managed = False
        permissions = [('User_Admin', 'Has access to the entire application'),
                        ('Basic_Customer_User', 'Has basic access to the application'),
                        ]

### middleware table ###

class newstats(models.Model):
    win = models.IntegerField()
    mac = models.IntegerField()
    iphone = models.IntegerField()
    android = models.IntegerField()
    other = models.IntegerField()






        


