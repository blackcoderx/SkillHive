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
  path('skills/', views.SkillsView, name='skills'),
  path('send-request/<int:pk>/', views.SendRequestView, name='send_request'),
  path('accept-request/<int:pk>/', views.AcceptRequestView, name='accept_request'),
]