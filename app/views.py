from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def demo(request):
    return render(request, 'index.html')

def submit_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        # You can perform additional actions and return an appropriate response
        return render(request, 'success.html', {'name': name})
    else:
        # Handle GET requests if needed
        return render(request, 'form.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already in use")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords not matching")
            return redirect('register')
    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def submit(request):
    return render(request,'submit.html')
