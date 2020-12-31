from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # user has an informations and wants an account nom !
        if request.POST ['password1'] == request.POST ['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render  (request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist :
                user = User.objects.create_user(request.POST['username'],request.POST ['password1'] )
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password does not match'})
    else:

        return render (request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request, username= request.POST['username'], password = request.POST ['password'])
        if user is not None:
            # if the form is filled
            auth.login(request, user)
            return redirect('home')
        else:
            return render (request, 'accounts/login.html', {'error':'username or password is incorrect.'})
    else:
        return render (request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    return render (request, 'accounts/logout.html')