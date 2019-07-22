from django.contrib import admin
<<<<<<< HEAD
from .models import *


# Register your models here.
class PayAdmin(admin.ModelAdmin):
    list_display = ['id','buyer_name','amount']

admin.site.register(Pay,PayAdmin)
=======

# Register your models here.
>>>>>>> d0b4b02740d8cbb7c7ff0db556e1bfbf89ec8286
