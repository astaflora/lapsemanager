from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth import views as auth_view
from django.contrib.auth import decorators, logout

from . import forms

# Create your views here.


#on exige que toute les pages soit acessible si on se connecte dab.
class LoginView(auth_view.LoginView):
    template_name = 'stock/pages/login.html'
    form = forms.LoginForm


@decorators.login_required
def index(request):
    return render(request, 'stock/pages/index.html')


@decorators.login_required
def sign_out(request):
    logout(request)
    return redirect(reverse('stock:index'))
