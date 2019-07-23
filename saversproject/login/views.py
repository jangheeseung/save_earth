from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def login(request):
        return render(request,'login/login.html')

def signup(request):
        return render(request,'login/signup.html')
