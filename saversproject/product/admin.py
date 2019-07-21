from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','name','price','donation_value','category','detail','image']

class ProductPropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'product','property','property_value']

class PropertyNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'property_name']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductProperty, ProductPropertyAdmin)
admin.site.register(PropertyName, PropertyNameAdmin)
admin.site.register(Category, CategoryAdmin)