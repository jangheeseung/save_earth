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

    path('write/<word>/',views.write,name="write"),
    path('detail/',views.detail,name="detail"),
    path('n_create/',views.n_create,name="n_create"),
    path('q_create/',views.q_create,name="q_create"),

    # path('n_board/',views.n_board,name="n_board"),
    # path('q_board/',views.q_board,name="q_board"),
    # path('n_detail/',views.n_detail,name="n_detail"),
    # path('q_detail/',views.q_detail,name="q_detail"),
]
