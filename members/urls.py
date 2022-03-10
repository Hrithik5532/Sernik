from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import UserRegistrationView
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('register/',UserRegistrationView,name="register"),
  path('reset_password/',auth_views.PasswordResetView.as_view(template_name='registration/change_pass.html'), name='reset_password'),
  path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='registration/pass_done.html'),name='password_reset_done'),
  path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
  path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]