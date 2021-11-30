from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Transactions, User_Finances, Stocks, User_Finance_History

# Register your models here

admin.site.register(Transactions)
admin.site.register(User_Finances)
admin.site.register(Stocks)
admin.site.register(User_Finance_History)
admin.site.register(Permission)