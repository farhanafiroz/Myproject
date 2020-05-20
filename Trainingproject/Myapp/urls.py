from django.urls import path
from Myapp import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('about_us',views.about),
    path('contact_us',views.contact),

]