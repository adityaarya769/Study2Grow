from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import privateJobs, privateJobs1, govJobs1
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def home(request):
    private_work = privateJobs.objects.all()
    return render(request, 'index1.html', {'private_work': private_work})

def Blog(request):
    return render(request, 'blog.html')



def gov_jobs(request):
    gov_work = govJobs1.objects.all()
    return render(request, 'gov-jobs.html', {'gov_work': gov_work})

def private_jobs(request):
    private_work = privateJobs1.objects.all()
    return render(request, 'private-jobs.html', {'private_work': private_work})

def Blog_single1(request):
    return render(request, 'blog-single1.html')

def Blog_single2(request):
    return render(request, 'blog-single2.html')

def Blog_single3(request):
    return render(request, 'blog-single3.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('login')
            else: 
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'user created')
                return redirect('/')

    else: 
        messages.info(request, 'password not matching')
        return render(request, 'Login.html')
    return redirect('/')