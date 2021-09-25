from rest_framework.parsers import JSONParser
from .models import Stocks, Transactions, User_Finances
from .serializers import StocksSerializer, TransactionsSerializer, User_FinancesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.

class StockTransactionAPIView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = TransactionsSerializer

    def get(self, request):
        get_transactions = Transactions.objects.filter(User_id = request.user.id)
        serializer = TransactionsSerializer(get_transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionsSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({'error_message': str(error)}, status=status.HTTP_402_PAYMENT_REQUIRED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StocksAPIView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = StocksSerializer

    def get(self, request):
        get_stocks = Stocks.objects.filter(User_id = request.user.id)
        serializer = StocksSerializer(get_stocks, many=True)
        return Response(serializer.data)


class User_FinancesAPIView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = User_Finances

    def get(self, request):
        get_userinfo = User_Finances.objects.filter(User = User.objects.get(id=request.user.id))
        serializer = User_FinancesSerializer(get_userinfo)
        return Response(serializer.data)
