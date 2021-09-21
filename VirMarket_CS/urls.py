from django.urls import path
from . import views

urlpatterns = [
    path('api', views.article_list, name='api'),
    path('api/<int:pk>', views.article_detail)
]