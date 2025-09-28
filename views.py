from django.shortcuts import render
from .models import Course

def home(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'courses/home.html', {'courses': courses})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),  # Trang chủ
]
