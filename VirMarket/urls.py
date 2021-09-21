from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),



    ### Authentication Paths ###
    path('Register', views.Register, name='Register'),
    path('Login', views.Login, name='Login'),
    path('Logout', views.Logout, name='Logout'),
]