from django.urls import path
from Myapp import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('register',views.create, name='register'),
    path('success', views.success, name='success'),
    path('json/', views.python_training, name='json'),
    # path('api/', views.LoginList.as_view()),
    # path('practice/', views.PracticeView.as_view()),

]
