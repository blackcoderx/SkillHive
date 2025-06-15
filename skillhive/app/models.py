from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUserModel(AbstractBaseUser, PermissionsMixin):
  full_name = models.CharField(max_length=225)
  email = models.EmailField(unique=True, verbose_name=_('Email Address'))
  bio = models.TextField(max_length=700, blank=True, null=True, verbose_name=_('Biography'))

  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  is_verified = models.BooleanField(default=False)
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now=True)

  objects = CustomUserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['full_name', 'bio']
  def __str__(self):
    return self.full_name


class Skill(models.Model):
  user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='skills')
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  category = models.CharField(max_length=50)
  level = models.CharField(max_length=30)
  type = models.CharField(max_length=30)
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self):
    return f"{self.user.full_name} - {self.title}"