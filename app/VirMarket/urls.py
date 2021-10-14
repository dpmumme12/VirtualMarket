from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Stock/<str:Symbol>', views.CompanyPage, name='CompanyPage'),
    path('Profile', views.UserProfile, name='UserProfile'),



    ### Authentication Paths ###
    path('Register', views.Register, name='Register'),
    path('Login', views.Login, name='Login'),
    path('Logout', views.Logout, name='Logout'),
]