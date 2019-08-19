from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from .models import User

class UserAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    #admin 사이트에 보여질 필드 정의
    list_display = ('get_full_name', 'email', 'name', 'is_active', 'is_superuser', )
    #링크 기능(클릭)을 추가할 필드를 정의하는 옵션
    list_display_links = ('get_full_name',)
    #필터를 활성화할 필드를 설정하는 옵션
    list_filter = ('is_superuser', )
    #admin페이지 커스터마징하기. 
    # fieldsets = (
    # ('해당 줄의 제목', {'fields':('','', ...)}),
    # ('해당 줄의 제목', {'fields':('','', ...)}),
    #   )
    fieldsets = (
        (None, {'fields': ('email', 'name','password')}),
        (_('Personal info'), {'fields': ('address', 'tel', 'monthy_amount', 'donate_value', 'coin', 'post_code', 'term', 'use_period')}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    
    #create user페이지 커스터마이징하기.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'address', 'tel')}
         ),
    )
    search_fields = ('email','name')
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)