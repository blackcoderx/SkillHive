from django.contrib import admin
from .models import CustomUserModel, Requests, Skill
# Register your models here.

admin.site.register(CustomUserModel)
admin.site.register(Skill)
admin.site.register(Requests)
