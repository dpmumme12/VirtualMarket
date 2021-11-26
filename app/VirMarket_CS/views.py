from .models import Stocks, Transactions, User_Finances
from .serializers import StocksSerializer, TransactionsSerializer, User_FinancesSerializer, User_ProfileSerializer,PostResponse
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

##############################
### Internal API endpoints ###
##############################


class StockTransactionAPIView(APIView):
    """API endpoint to handle all transactions the user makes such as Buying or Selling stocks"""

    ### Setting the authentication for the endpoint ###
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200:  TransactionsSerializer() })
    def get(self, request):
        """Gets all transactions the user has made"""

        get_transactions = Transactions.objects.filter(User_id = request.user.id)
        serializer = TransactionsSerializer(get_transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200:  PostResponse, 400: PostResponse }, request_body= TransactionsSerializer)
    def post(self, request):
        """Handles the Buying and Selling of stocks"""

        serializer = TransactionsSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(PostResponse().successful(), status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response(PostResponse().error(errors=serializer.errors, msg=str(error)), status=status.HTTP_400_BAD_REQUEST)

        return Response(PostResponse().error(serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class StocksAPIView(generics.GenericAPIView):
    """API endpoint to get all of the stocks the user is currently invested in"""
  
    ### Setting the authentication for the endpoint ###
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    @swagger_auto_schema(responses={200:  StocksSerializer })
    def get(self, request):
        get_stocks = Stocks.objects.filter(User_id = request.user.id)
        serializer = StocksSerializer(get_stocks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class User_FinancesAPIView(APIView):
    """API endpoint to get the user's current account balance"""

    ### Setting the authentication for the endpoint ###
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(responses={200:  User_FinancesSerializer })
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        get_user = User_Finances.objects.get(User=user)
        serializer = User_FinancesSerializer(get_user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class User_InfoAPIView(APIView):
    """API endpoint to get user's profile info as well as update it"""

    ### Setting the authentication for the endpoint ###
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(responses={200:  User_ProfileSerializer })
    def get(self, request):
        user_info = User.objects.get(id = request.user.id)
        serializer = User_ProfileSerializer(user_info)
        return Response(serializer.data, status = status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: PostResponse, 400: PostResponse }, request_body=User_ProfileSerializer)
    def put(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        serializer = User_ProfileSerializer(user,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(PostResponse().successful(), status = status.HTTP_200_OK)

        return Response(PostResponse().error(serializer.errors), status.HTTP_400_BAD_REQUEST)



