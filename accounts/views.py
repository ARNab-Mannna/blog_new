from django.shortcuts import render,redirect
from django.contrib.auth .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib. auth  import logout as auth_logout
from django.contrib import messages

# Create your views here.

def login (request):
    if request.method == 'POST':
        ioguser_name=request.POST['logusername']
        ioguser_pass=request.POST['logpassword']

        user= authenticate(username=ioguser_name,password= ioguser_pass)

        if user is not None:
            auth_login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('/')
        else:
            messages.error(request,"  Invalid username or password please try again.. ! ")
            return redirect('/')

    return render(request, 'login.html')
def logout (request):
    auth_logout(request)
    messages.success(request,"Logging OUT")
    return redirect ('/')
    
def Register (request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request,'You Have alrady registerd.')
                return redirect('/register')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'This Email is alrady in use.')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email )
                user.save();
                messages.success(request,'You Have sucessfuly registard.')
                print('User susccesfully created')
                return redirect('/')
        else:          
            return redirect('/register')            
    else:
        return render(request, 'register.html')