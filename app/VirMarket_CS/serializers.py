from rest_framework import serializers
from .models import Stocks, Transactions, User_Finances
from django.contrib.auth.models import User


########################################
### Serializer for each API endpoint ###
########################################




class PostResponse(serializers.Serializer):
    success = serializers.BooleanField()
    msg = serializers.CharField(max_length=100)
    errors = serializers.DictField(child= serializers.ListField())

    def successful(self):
        response = self.data
        response['success'] = True
        return response

    def error(self, errors, msg=''):
        response = self.data
        response['success'] = False
        response['msg'] = msg
        response['errors'] = errors
        return response


class StocksSerializer(serializers.ModelSerializer):
    """Serializer for the StocksAPIView"""

    class Meta:
        model = Stocks
        fields = ['Symbol', 'Name', 'Shares', 'User_id']


class User_FinancesSerializer(serializers.ModelSerializer):
    """Serializer for the User_FinancesAPIView"""

    class Meta:
        model = User_Finances
        fields = ['Current_Balance']


class User_ProfileSerializer(serializers.ModelSerializer):
    """Serializer for the User_InfoAPIView"""

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']


class TransactionsSerializer(serializers.ModelSerializer):
    """Serializer for the StockTransactionAPIView"""

    class Meta:
        model = Transactions
        fields = ['Symbol', 'Name', 'Shares', 'Price', 'TransactionType','User_id']

    ### defining the logic for when a transaction is made. ex: Buying a stock ###
    def create(self, validated_data):
       Users_CurrentBalance = User_Finances.objects.get(User = validated_data['User_id'])

       ### Logic that ones if the user is buying a stock ###
       if validated_data['TransactionType'] == Transactions.TRANSACTION_TYPES.BUY.value:
           Users_CurrentBalance = User_Finances.objects.get(User = validated_data['User_id'])

           ### Checks if user has enough funds for the transaction ###
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
       
       ### Logic that runs if user is selling a stock ###
       elif validated_data['TransactionType'] == Transactions.TRANSACTION_TYPES.SELL.value:
           User_SharesForCompany = Stocks.objects.filter(Symbol=validated_data['Symbol'], User_id = validated_data['User_id'], 
                                                            Shares__gte=validated_data['Shares'])

           ### checks if user has the appropiate amount of shares to make transaction ###
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
   

