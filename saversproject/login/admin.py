from django.contrib import admin
<<<<<<< HEAD
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'email', 'pw', 'tel', 'monthly_amount', 'donate_value','coin', 'post_code','term','use_period']

admin.site.register(User, UserAdmin)
=======

# Register your models here.
>>>>>>> d0b4b02740d8cbb7c7ff0db556e1bfbf89ec8286
