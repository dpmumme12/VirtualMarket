from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm, LoginForm
from VirMarket_CS.models import User_Finances, Stocks
import requests
from urllib import parse
from decimal import Decimal


@login_required()
def index(request):
    queryset = Stocks.objects.filter(User_id = request.user.id).order_by('Symbol')
    user_stocks = []
    for stock in queryset:
        user_stocks.append(stock.Symbol)
    base_url = f"https://sandbox.iexapis.com/stable/stock/market/batch?symbols={(','.join(user_stocks))}&types=price&"
    url = base_url  + parse.urlencode({"token": 'Tsk_67f6bc30222b44d1b13725f19d0619db'})
    response = requests.get(url).json()
    print(response)
    TotalAccountBalance = 0
    for stock in queryset:
        try:
            TotalAccountBalance += (stock.Shares * response[stock.Symbol.upper()]['price'])
        except:
            pass

    print(TotalAccountBalance)
    

    

    return render(request, 'index.html', {
        'data': response
    })

### Authentication Views ###
def Register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            login(request, authenticate(username = username, password = password))
            User_Finances.objects.create(User=request.user, Current_Balance = 100000.00)
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)

    UserForm = SignUpForm()
    return render(request, 'register.html', {'UserForm': UserForm})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, 'Login.html', {
                'message': 'Invalid username and/or password.',
                'LoginForm': LoginForm()
            } )

    return render(request, 'Login.html', {'LoginForm': LoginForm()})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login'))