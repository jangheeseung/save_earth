<<<<<<< HEAD
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'category'

class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    detail = models.CharField(max_length=45)
    image = models.CharField(max_length=45)
    donation_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'


class ProductProperty(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    property = models.ForeignKey('PropertyName', on_delete=models.CASCADE) #속성 종류
    property_value = models.CharField(max_length=45) #속성 값

    class Meta:
        managed = False
        db_table = 'product_property'


class PropertyName(models.Model):
    property_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'property_name'


=======
from django.db import models

# Create your models here.
>>>>>>> d0b4b02740d8cbb7c7ff0db556e1bfbf89ec8286
