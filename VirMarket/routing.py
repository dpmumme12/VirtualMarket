from django.conf.urls import url
from .consumers import StockGraphConsumer, UserTotalAccountBalanceConsumer
from django.urls import re_path



ws_urlpatterns =[
    url('ws/stockgraph/', StockGraphConsumer.as_asgi()),
    re_path('ws/UserTotalAccountBalance/(?P<pk>\d+)/$', UserTotalAccountBalanceConsumer.as_asgi()),
]