from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'userAccounts/login.html',{"error":"Code or password is invalid!"})
    return render(request, 'userAccounts/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'userAccounts/register.html', {"error": "An account already exists for this code."})
        elif cpassword != password:
            return render(request, 'userAccounts/register.html', {"error": "Password and Confirm password do not match."})
        else:
            user = User(username=username)
            user.set_password(password)
            
            try:
                user.save()
            except Exception as e:
                return render(request, 'userAccounts/register.html', {"error": "An error occurred while creating the account."})
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'userAccounts/register.html', {"error": "An error occurred during authentication."})

    else:
        return render(request,'userAccounts/register.html')