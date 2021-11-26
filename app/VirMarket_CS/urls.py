from django.urls import path, re_path
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

api_info = openapi.Info(
   title="Snippets API",
   default_version='v1',
)

schema_view = get_schema_view(
   openapi.Info(
      title="Virtual Market API",
      default_version='1.0.0',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from rest_framework.schemas import get_schema_view
### Internal API routes ### 

urlpatterns = [
    path('Transactions', views.StockTransactionAPIView.as_view(), name = 'TransacionsAPI'),
    path('Stocks', views.StocksAPIView.as_view(), name = 'StocksAPI'),
    path('UserBalance', views.User_FinancesAPIView.as_view(), name = 'UserBalanceAPI'),
    path('UserInfo', views.User_InfoAPIView.as_view(), name = 'UserInfoAPI'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

