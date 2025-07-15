from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from OtidiDo.accounts.models import AppUser


# Register your models here.
@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    pass