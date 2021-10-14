from rest_framework import fields, serializers
from .models import Stocks, Transactions, User_Finances
from django.contrib.auth.models import User



class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['Symbol', 'Name', 'Shares', 'User_id']


class User_FinancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Finances
        fields = ['Current_Balance']


class User_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['Symbol', 'Name', 'Shares', 'Price', 'TransactionType','User_id']

    def create(self, validated_data):
       Users_CurrentBalance = User_Finances.objects.get(User = validated_data['User_id'])

       if validated_data['TransactionType'] == Transactions.TRANSACTION_TYPES.BUY.value:
           Users_CurrentBalance = User_Finances.objects.get(User = validated_data['User_id'])

           if (validated_data['Price'] * validated_data['Shares']) > Users_CurrentBalance.Current_Balance:
               raise Exception('Insuffcient funds for this transaction.')
               
        
           User_SharesForCompany = Stocks.objects.filter(Symbol=validated_data['Symbol'], User_id = validated_data['User_id'])
        
           if User_SharesForCompany.exists():
               Users_TotalShares = User_SharesForCompany.get().Shares + validated_data['Shares']
               User_SharesForCompany.update(Shares=Users_TotalShares) 

           else:
               Stocks.objects.create(Symbol=validated_data['Symbol'], Name=validated_data['Name'], 
                                        Shares=validated_data['Shares'], User_id=validated_data['User_id'])

           Transaction = Transactions.objects.create(**validated_data)
           NewBalance = Users_CurrentBalance.Current_Balance - (validated_data['Price'] * validated_data['Shares'])
           User_Finances.objects.filter(User = validated_data['User_id']).update(Current_Balance=NewBalance)

       elif validated_data['TransactionType'] == Transactions.TRANSACTION_TYPES.SELL.value:
           User_SharesForCompany = Stocks.objects.filter(Symbol=validated_data['Symbol'], User_id = validated_data['User_id'], 
                                                            Shares__gte=validated_data['Shares'])
        
           if User_SharesForCompany.exists():
               Users_TotalShares = User_SharesForCompany.get().Shares - validated_data['Shares']

               if Users_TotalShares == 0:
                   User_SharesForCompany.delete()

               User_SharesForCompany.update(Shares=Users_TotalShares) 

           else:
               raise Exception('Insuffcient shares to make this transaction.')

           Transaction = Transactions.objects.create(**validated_data)
           NewBalance = Users_CurrentBalance.Current_Balance + (validated_data['Price'] * validated_data['Shares'])
           User_Finances.objects.filter(User = validated_data['User_id']).update(Current_Balance=NewBalance)
       
       return Transaction
   

