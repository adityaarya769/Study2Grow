from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index1.html', views.home, name='home'),
    path('gov-jobs.html', views.gov_jobs, name='governmentJobs'),
    path('private-jobs.html', views.private_jobs, name='privateJobs'),
    path('blog.html', views.Blog, name='Blog'),
    path('private-jobs.html', views.private_jobs, name='ShowMoreJobs'),
    path('blog-single1.html', views.Blog_single1, name='TCS'),
    path('blog-single2.html', views.Blog_single2, name='Google'),
    path('blog-single3.html', views.Blog_single3, name='Isro'),
    path('Login.html', views.login, name='login'),

    
]
