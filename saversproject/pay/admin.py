from django.contrib import admin
from .models import *


# Register your models here.
class PayAdmin(admin.ModelAdmin):
    list_display = ['id','buyer_name','amount']

admin.site.register(Pay,PayAdmin)
