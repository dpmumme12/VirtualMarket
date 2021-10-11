from .models import Stocks, Transactions, User_Finances
from .serializers import StocksSerializer, TransactionsSerializer, User_FinancesSerializer, User_ProfileSerializer
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


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
        user = User.objects.get(id=request.user.id)
        get_user = User_Finances.objects.get(User=user)
        serializer = User_FinancesSerializer(get_user)
        return Response(serializer.data)


class User_InfoAPIView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        user_info = User.objects.get(id = request.user.id)
        serializer = User_ProfileSerializer(user_info)
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    def put(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        serializer = User_ProfileSerializer(user,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


