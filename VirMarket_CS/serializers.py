from rest_framework import serializers
from .models import Stocks, Transactions, User_Finances



class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['Symbol', 'Name', 'Shares', 'User_id']

class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ['Symbol', 'Name', 'Shares', 'Price', 'TransactionType','User_id']

    def create(self, validated_data):
       Transaction = Transactions.objects.create(**validated_data)
       if validated_data['TransactionType'] == Transactions.TRANSACTION_TYPES.BUY.value:
           Users_CurrentBalance = User_Finances.objects.get(User = validated_data['User_id'])

           if validated_data['Price'] > Users_CurrentBalance.Current_Balance:
               return TypeError
            
           User_SharesForCompany = Stocks.objects.filter(Symbol=validated_data['Symbol'], User_id = validated_data['User_id'])
           print(User_SharesForCompany.exists())
           if User_SharesForCompany.exists():
               print(User_SharesForCompany.exist())

           else:
               Stocks.objects.create(Symbol=validated_data['Symbol'], Name=validated_data['Name'], 
                                        Shares=validated_data['Shares'], User_id=validated_data['User_id'])
               Transaction = Transactions.objects.create(**validated_data)
               NewBalance = Users_CurrentBalance.Current_Balance - validated_data['Price']
               User_Finances.objects.filter(User = validated_data['User_id']).update(Current_Balance=NewBalance)

               


       
       return Transaction
   

