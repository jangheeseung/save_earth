from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def board(request):
        return render(request,'board/board.html')
