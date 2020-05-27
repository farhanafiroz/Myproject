from django.urls import path
from Myapp import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('register',views.form_view, name='register'),
]