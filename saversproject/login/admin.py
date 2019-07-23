from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'email', 'pw', 'tel', 'monthly_amount', 'donate_value','coin', 'post_code','term','use_period']

admin.site.register(User, UserAdmin)
