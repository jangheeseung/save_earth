<<<<<<< HEAD
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class User(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    monthly_amount = models.CharField(max_length=45) #월정액 금액
    donate_value = models.IntegerField() #기부금 총 합
    coin = models.IntegerField()
    post_code = models.CharField(max_length=45) #우편번호
    term = models.IntegerField() #월정액 기한
    use_period = models.IntegerField() #월정액 사용기한

    class Meta:
        managed = False
        db_table = 'user'
=======
from django.db import models

# Create your models here.
>>>>>>> d0b4b02740d8cbb7c7ff0db556e1bfbf89ec8286
