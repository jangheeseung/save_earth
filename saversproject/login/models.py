# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User



class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    monthly_amount = models.CharField(max_length=45, null=True) #월정액 금액
    donate_value = models.IntegerField(null=True) #기부금 총 합
    coin = models.IntegerField(null=True)
    post_code = models.CharField(max_length=45,null=True) #우편번호
    term = models.IntegerField(null=True) #월정액 기한
    use_period = models.IntegerField(null=True) #월정액 사용기한

    class Meta:
        managed = False
        db_table = 'user'
