from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('courses/', views.courses, name="courses"),
    path('contact/', views.contact, name="contact"),
    path('apply/', views.apply, name='apply'),  # Adjusted to use views.application_form
    path('success/', views.success, name='success'),

] 
