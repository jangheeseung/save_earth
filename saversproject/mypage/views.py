from django.shortcuts import render

# Create your views here.
def mypage(request):
        return render(request,'mypage/mypage.html')

def mydetail(request):
        return render(request,'mypage/mydetail.html')

def basket(request):
        return render(request,'mypage/basket.html')

def order(request):
        return render(request,'mypage/order.html')