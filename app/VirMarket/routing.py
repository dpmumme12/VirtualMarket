from .consumers import StockGraphConsumer, UserTotalAccountBalanceConsumer
from django.urls import re_path

### Url patterns for websocket connections using ASGI server ###

ws_urlpatterns =[
    re_path('ws/stock/(?P<symbol>\w+)/$', StockGraphConsumer.as_asgi()),
    re_path('ws/UserTotalAccountBalance/(?P<pk>\d+)/$', UserTotalAccountBalanceConsumer.as_asgi()),
]