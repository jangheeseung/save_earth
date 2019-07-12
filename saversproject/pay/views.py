from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def pay(request):
        return render(request,'pay/pay.html')