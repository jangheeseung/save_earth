# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Pay(models.Model):
    pg = models.CharField(max_length=45)
    pay_method = models.CharField(max_length=45)
    name = models.CharField(max_length=45, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    buyer_email = models.CharField(max_length=45, blank=True, null=True)
    buyer_name = models.CharField(max_length=45, blank=True, null=True)
    buyer_tel = models.CharField(max_length=45, blank=True, null=True)
    buyer_addr = models.CharField(max_length=45, blank=True, null=True)
    buyer_postcode = models.CharField(max_length=45, blank=True, null=True)
    m_redirect_url = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay'
