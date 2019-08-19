# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=45, unique=True)
    address = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique=True)
    tel = models.CharField(max_length=45)
    monthly_amount = models.CharField(max_length=45, blank=True, default='NULL') #월정액 금액
    donate_value = models.IntegerField(blank=True, default=0) #기부금 총 합
    coin = models.IntegerField(blank=True, default=0)
    post_code = models.CharField(max_length=45,blank=True, default='NULL') #우편번호
    term = models.IntegerField( blank=True, default=1) #월정액 기한 1개월/3개월/6개월/12개월
    use_period = models.IntegerField(blank=True, default=0) #월정액 사용기한 

    #AbstractBaseUser사용할때 꼭 정의해줘야 
    last_login=models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email' #여기서 지정한 모든 필드는 unique=True 여야 한다는데
    
    REQUIRED_FIELDS = ['name'] #user를 생성하는데 필수적인 필드

    # USER_TYPE_CHOICES = (
    # ('django', 'Django'),
    # ('facebook', 'Facebook'),
    # ('gmail', 'Gmail')
    # )

    class Meta:
        app_label='login'
        verbose_name = ('user') #admin 페이지에서 조회할 떄 읽기 쉬운 이름으로 정의하는 옵션
        verbose_name_plural = ('users') #영어 기준으로 복수형 이름으로 정의하는 옵션
        ordering = ('email',) #모델의 정렬 순서 지정, 여러 개일 경우 필드 이름을 리스트로 나열.기본값은 오름차순. -를 붙이면 내림차순
        managed = True #False일 때 : 모델이 자동으로 테이블을 생성하지 않게 함.
        # db_table = 'user'

    def __str__(self):
        return self.email

    def get_full_name(self):       
        # The user is identified by their email address 
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All superusers are staff
    #     return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
    # @property
    # def is_active(self):
    #     return bool(self.is_active)
