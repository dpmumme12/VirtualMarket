from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Stocks, Transactions, User_Finances
from .serializers import StocksSerializer, TransactionsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.



#    authentication_classes = [SessionAuthentication, BasicAuthentication]
#    authentication_classes = [TokenAuthentication]
#    permission_classes = [IsAuthenticated]





class StockTransactionAPIView(APIView):
    
    serializer_class = TransactionsSerializer
    

    def get(self, request):
        get_stocks = Stocks.objects.all()
        serializer = StocksSerializer(get_stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionsSerializer(data=request.data)

        if serializer.is_valid():
            
            serializer.save()
            

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
