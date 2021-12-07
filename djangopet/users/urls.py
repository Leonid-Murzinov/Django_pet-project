from django.contrib import admin
from django.urls import path
from users.views import LoginView
from django.contrib.auth import views as authViews


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='/news/'), name='logout'),
] 