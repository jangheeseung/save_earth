from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def product(request):
        return render(request,'product/product.html')
