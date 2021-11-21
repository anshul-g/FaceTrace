from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'Institution']

    fieldsets = UserAdmin.fieldsets + (
            ('Extra Fields', {'fields': ('Institution',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)