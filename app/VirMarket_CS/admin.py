from django.contrib import admin
from .models import Transactions, User_Finances, Stocks

# Register your models here

admin.site.register(Transactions)
admin.site.register(User_Finances)
admin.site.register(Stocks)