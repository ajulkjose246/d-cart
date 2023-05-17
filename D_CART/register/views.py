from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cnfpassword = request.POST.get('cnfpassword')

        if password == cnfpassword:
            if User.objects.filter(username=username).exists():
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                return redirect('/register/')
            else:
                user_reg = User.objects.create_user(
                    username=username, email=email, password=password, first_name=fname, last_name=lname)
                return redirect('/register/')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')