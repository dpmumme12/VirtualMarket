from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm, LoginForm
from VirMarket_CS.models import User_Finances, Stocks, Transactions
import requests
from urllib import parse
from django.core.paginator import Paginator



@login_required()
def index(request):

    objects = Transactions.objects.filter(User_id = request.user.id).order_by('-TransactionDateTime')
    Users_Transactions = Paginator(objects, 20)

    page_number = request.GET.get('page')
    page_obj = Users_Transactions.get_page(page_number)

    queryset = Stocks.objects.filter(User_id = request.user.id).order_by('Symbol')
    UninvestedBalance = User_Finances.objects.get(User = request.user).Current_Balance
   
    
    user_stocks = []
    for stock in queryset:
        user_stocks.append(stock.Symbol)
    base_url = f"https://sandbox.iexapis.com/stable/stock/market/batch?symbols={(','.join(user_stocks))}&types=price&"
    url = base_url  + parse.urlencode({"token": 'Tsk_67f6bc30222b44d1b13725f19d0619db'})
    response = requests.get(url).json()
    TotalAccountBalance = 0
    for stock in queryset:
        try:
            TotalAccountBalance += (stock.Shares * response[stock.Symbol.upper()]['price'])
        except:
            pass

    TotalAccountBalance= TotalAccountBalance + float(UninvestedBalance)

    url = 'https://sandbox.iexapis.com/stable/stock/market/list/gainers?displayPercent=true&token=Tsk_67f6bc30222b44d1b13725f19d0619db'
    gainers = requests.get(url).json()

    url = 'https://sandbox.iexapis.com/stable/stock/market/list/losers?displayPercent=true&token=Tsk_67f6bc30222b44d1b13725f19d0619db'
    losers = requests.get(url).json()

    url = 'https://finnhub.io/api/v1/news?category=general&minId=10&token=c5bmkjqad3ifmvj0nc10'
    resp = requests.get(url).json()
    NewsArticles = resp[:5]
    print(NewsArticles)
    
    return render(request, 'index.html', {
        'data': TotalAccountBalance, 
        'pk': request.user.id,
        'gainers': gainers,
        'losers': losers,
        'page_obj': page_obj,
        'NewsArticles': NewsArticles,
        'BuyingPower': UninvestedBalance})


@login_required()
def CompanyPage(request, Symbol):
 
    url = f'https://sandbox.iexapis.com/stable/stock/{Symbol}/chart/3m?token=Tsk_67f6bc30222b44d1b13725f19d0619db'
    ChartData = requests.get(url).json()

    url = f'https://sandbox.iexapis.com/stable/stock/{Symbol}/quote?token=Tsk_67f6bc30222b44d1b13725f19d0619db'
    quote = requests.get(url).json()

    url = f'https://cloud.iexapis.com/stable/stock/{Symbol}/company?token=pk_2bf7385198b8400582fd6b7f335e879f'
    CompanyData = requests.get(url).json()
    

    

    return render(request, 'CompanyPage.html', {
        'data': ChartData,
        'quote': quote,
        'UserId': request.user.id,
        'CompanyData': CompanyData
    })

def UserProfile(request):
    
    return render(request, 'Profile.html')


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
            return render(request, 'register.html', {'UserForm': form})

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


################ total balance script ############
     # queryset = Stocks.objects.filter(User_id = request.user.id).order_by('Symbol')
    # user_stocks = []
    # for stock in queryset:
    #     user_stocks.append(stock.Symbol)
    # base_url = f"https://sandbox.iexapis.com/stable/stock/market/batch?symbols={(','.join(user_stocks))}&types=price&"
    # url = base_url  + parse.urlencode({"token": 'Tsk_67f6bc30222b44d1b13725f19d0619db'})
    # response = requests.get(url).json()
    # print(response)
    # TotalAccountBalance = 0
    # for stock in queryset:
    #     try:
    #         TotalAccountBalance += (stock.Shares * response[stock.Symbol.upper()]['price'])
    #     except:
    #         pass

    # print(TotalAccountBalance)