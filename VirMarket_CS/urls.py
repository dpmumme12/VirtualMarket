from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.StockTransactionAPIView.as_view(), name='api'),
]