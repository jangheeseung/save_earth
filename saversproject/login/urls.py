from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.signout,name="logout"),
    path('accounts/', include('allauth.urls')),
    # path('', include('django.contrib.auth.urls')),
]

