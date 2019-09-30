from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('n_board/',views.n_board,name="n_board"),
    path('q_board/',views.q_board,name="q_board"),
    path('write/',views.write,name="write"),
    path('n_detail/',views.n_detail,name="n_detail"),
    path('q_detail/',views.q_detail,name="q_detail"),
]