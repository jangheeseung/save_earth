from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def main(request):
        return render(request,'main/main.html')

def load(request):
        return render(request,'main/loading.html')