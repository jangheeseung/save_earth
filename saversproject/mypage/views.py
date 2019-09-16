from django.shortcuts import render, redirect
from .models import Basket
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def mypage(request):
        usermodel = get_user_model().objects.get(id=request.user.id)#현재 로그인된 유저의 id값과 일치하는 user객체 가져오기
        return render(request,'mypage/mypage.html', {'user':usermodel})

def mydetail(request):
        return render(request,'mypage/mydetail.html')

def basket(request):
        return render(request,'mypage/basket.html')

        