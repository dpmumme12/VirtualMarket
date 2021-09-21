from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm, LoginForm


@login_required()
def index(request):
    return render(request, 'index.html')

### Authentication Views ###
def Register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            login(request, authenticate(username = username, password = password))
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