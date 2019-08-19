from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('notice/',views.noticeboard,name="noticeboard"),
    path('notice/<int:noticeboard_id>/',views.notice_detail,name="notice_detail"),

    path('qaboard/',views.qaboard,name="qaboard"),
    path('qaboard/<int:qaboard_id>/',views.QandA_detail,name="QandA_detail"),

    path('write/',views.write,name="write"),
    path('detail/',views.detail,name="detail"),
    path('n_create/',views.n_create,name="n_create"),

]

