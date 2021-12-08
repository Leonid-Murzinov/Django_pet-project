from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from .forms import RegisterForm


class LoginView(LoginView):
    template_name = 'users/login.html'


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/news")
    else:
        form = RegisterForm()

    return render(response, "users/register.html", {"form":form})