from django.urls import path, include
from . import views

app_name = 'stock'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.sign_out, name='logout'),
]
