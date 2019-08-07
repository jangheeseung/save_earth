from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def board(request):
        return render(request,'board/board.html')
def write(request):
        return render(request,'board/write.html')
def detail(request):
        return render(request,'board/detail.html')
