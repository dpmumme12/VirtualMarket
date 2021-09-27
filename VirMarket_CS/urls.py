from django.urls import path, include
from . import views



urlpatterns = [
    path('Transactions', views.StockTransactionAPIView.as_view(), name = 'TransacionsAPI'),
    path('Stocks', views.StocksAPIView.as_view(), name = 'StocksAPI'),
    path('UserBalance', views.User_FinancesAPIView.as_view(), name = 'UserBalanceAPI'),
    path('UserInfo', views.User_InfoAPIView.as_view(), name = 'UserInfoAPI'),

]