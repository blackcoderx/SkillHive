from django.shortcuts import render,redirect
from .form import CustomUserRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import *
# from django.contrib.auth.decorators import login_required

def LandingpageView(request):
  return render(request,'index.html')

def LoginView(request):
  if request.user.is_authenticated:
    return redirect('dashboard')

  if request.method == "POST":
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('dashboard')  # Redirect to your dashboard or home page
    else:
      error_message = "Invalid email or password"
      return render(request, 'auth/login.html', {'error': error_message})
  else:
    return render(request, 'auth/login.html')


def LogoutView(request):
  logout(request)
  return redirect('login')
  

def RegisterView(request):
  if request.user.is_authenticated:
    return redirect('dashboard')
  
  if request.method == 'POST':
    form = CustomUserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')  # Redirect to your login page
    else:
      # If the form is invalid, render the form with errors
      return render(request, 'auth/register.html', {'form': form})
  else:
    form = CustomUserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


def DashboardView(request):
  if not request.user.is_authenticated:
    return redirect('login')
  
  t_skills = Skill.objects.filter(user=request.user, type='teach').order_by('-created_at')
  l_skills = Skill.objects.filter(user=request.user, type='learn').order_by('-created_at')

  # Get all requests sent by the user
  requests_sent = Requests.objects.filter(from_user=request.user).order_by('-created_at')
  # Get all requests received by the user
  requests_received = Requests.objects.filter(to_user=request.user, status='pending').order_by('-created_at')

  # If you want to include accepted requests as well, you can modify the filter:
  content = {
    'user': request.user,
    't_skills': t_skills,
    'l_skills': l_skills,
    'requests_sent': requests_sent,
    'requests_received': requests_received,
  }

  return render(request, 'dashboard.html', content)

def SkillsView(request):
  if not request.user.is_authenticated:
    return redirect('login')

  skills = Skill.objects.all().order_by('-created_at')
  content = {
    'user': request.user,
    'skills': skills,
  }
  return render(request, 'skills.html', content)


def CreateSkillView(request):
  if not request.user.is_authenticated:
    return redirect('login')

  if request.method == 'POST':
    if request.POST.get('teach') is not None:
      type = 'teach'

    if request.POST.get('learn') is not None:
      type = 'learn'
      
    skill = Skill.objects.create(
      user=request.user,
      title=request.POST.get('title'),
      description=request.POST.get('description'),
      category=request.POST.get('category'),
      level=request.POST.get('level'),
      type=type
    )
    
    if not skill.pk:
      return JsonResponse({'message': 'Skill creation failed'}, status=500)
    return redirect('dashboard')

  return JsonResponse({'message': 'Invalid request'}, status=400)

def SendRequestView(request, pk):
  if not request.user.is_authenticated:
    return redirect('login')

  skill = Skill.objects.get(id=pk)

  if skill:
    Requests.objects.create(
      from_user=request.user,
      to_user=skill.user,
      skill=skill
    )

    return redirect('dashboard')

  return render(request, 'skills.html')

def AcceptRequestView(request, pk):
  if not request.user.is_authenticated:
    return redirect('login')

  request_obj = Requests.objects.get(id=pk)

  if request_obj and request_obj.to_user == request.user:
    request_obj.status = 'accepted'
    request_obj.save()
    return redirect('dashboard')

  return render(request, 'skills.html')