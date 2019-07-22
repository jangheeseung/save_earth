<<<<<<< HEAD
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class NoticeBoard(models.Model):
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'notice_board'



class QABoard(models.Model):
    user = models.ForeignKey('login.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'q&a_board'


class QABoardComment(models.Model):
    content = models.CharField(max_length=45)
    q_a = models.ForeignKey(QABoard, on_delete=models.CASCADE, db_column='q&a_id')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'q&a_board_comment'


=======
from django.db import models

# Create your models here.
>>>>>>> d0b4b02740d8cbb7c7ff0db556e1bfbf89ec8286
