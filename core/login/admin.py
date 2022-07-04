from django.contrib import admin

# Register your models here.

from .models import RegisterUser, LoginUser
admin.site.register(RegisterUser)
admin.site.register(LoginUser)