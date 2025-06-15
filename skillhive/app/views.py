from django.shortcuts import render,redirect
from .form import CustomUserRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Skill
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
  
  return render(request, 'dashboard.html', {'user': request.user})

def SkillsView(request):
  if not request.user.is_authenticated:
    return redirect('login')

  return render(request, 'skills.html', {'user': request.user})


def CreateSkillView(request):
  if not request.user.is_authenticated:
    return redirect('login')

  if request.method == 'POST':
    type = 'teach' if request.POST.get('type') == 'teach' else 'learn'

    skill = Skill.objects.create(
      user=request.user,
      title=request.POST.get('title'),
      description=request.POST.get('description'),
      category=request.POST.get('category'),
      level=request.POST.get('level'),
      type=type
    )
    return render(request, 'dashboard.html', {
      'user': request.user,
      'skill_created': True,
    })

  return JsonResponse({'message': 'Invalid request'}, status=400)