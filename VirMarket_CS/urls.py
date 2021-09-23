from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.StocksAPIView.as_view(), name='api'),
]