<<<<<<< HEAD
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Basket(models.Model):
    user = models.ForeignKey('login.User', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    status = models.IntegerField() #0이면 장바구니, 1이면 주문

    class Meta:
        managed = False
        db_table = 'basket'



class Donation(models.Model):
    user = models.ForeignKey('login.User', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    donation_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donation'


class OrderStatus(models.Model):
    order_status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'order_status'


class UserOrder(models.Model):
    user = models.ForeignKey('login.User', on_delete=models.CASCADE)
    ordered_product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    amount = models.IntegerField() #수량
    date = models.DateTimeField()
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE) #주문상태

    class Meta:
        managed = False
        db_table = 'user_order'
=======
from django.db import models

# Create your models here.
>>>>>>> d0b4b02740d8cbb7c7ff0db556e1bfbf89ec8286
