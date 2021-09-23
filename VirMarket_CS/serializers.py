from rest_framework import serializers
from .models import Stocks, Transactions, User_Finances


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['Symbol', 'Name', 'Shares', 'User_id']
   

