from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name =request.POST['last_name']
        username = request.POST['username']
        password =request.POST['password']
        email=request.POST['email']
        confirmpassword =request.POST['confirmpassword']
        if password == confirmpassword:
            print("hryy")
            if User.objects.filter(username=username).exists():
                print("username taken")
                messages.info(request, "Username taken! Please try with a different username.")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken! Please use some other mail")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                password=password, email=email)
                user.save()
                print('user created')
                return redirect('http://127.0.0.1:8000/login')
        else:
            messages.info(request, "Passwords don't match!")
        return redirect('register')
    else:
        return render(request, 'shop/register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("entered")
            return redirect('http://127.0.0.1:8000/shop')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('http://127.0.0.1:8000/login')
    else:
        return render(request, 'shop/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def flex(request):
    return render(request, 'shop/flex.html')


# Create your views here.
