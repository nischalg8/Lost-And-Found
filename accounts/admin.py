from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
User = get_user_model()
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    
    model = User
    list_display = ('username', 'email', 'phone_number', 'roll_no', 'is_staff')