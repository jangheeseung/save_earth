from django.contrib import admin
from .models import *

class UserOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','ordered_product','amount', 'date','order_status']

class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'status']

class DonationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'donation_value']

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_status']

# Register your models here.
admin.site.register(UserOrder, UserOrderAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)