from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
  path('', views.LandingpageView, name='landpage' ),
  path('login/', views.LoginView, name='login'),
  path('logout/', views.LogoutView, name='logout'),
  path('register/', views.RegisterView, name='register'),
  path('dashboard/', views.DashboardView, name='dashboard'),
  path('create-skill/', views.CreateSkillView, name='create-skill'),
]