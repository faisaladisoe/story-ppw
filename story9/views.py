from .forms import CreateUserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def userRegister(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Congratulations %s!! 🥳' % username)
            return redirect('login')

    content = {
        'form': form
    }
    return render(request, 'story9/register.html', content)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        userAuth = authenticate(request, username = username, password = password)
        if userAuth is not None:
            login(request, userAuth)
            return redirect('index')
        else:
            messages.error(request, 'Oops seems like combination of your username and password doesn\'t match')

    return render(request, 'story9/login.html')

def userLogout(request):
    logout(request)
    return redirect('login')
