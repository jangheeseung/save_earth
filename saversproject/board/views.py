from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def n_board(request):
        return render(request,'board/n_board.html')
def q_board(request):
        return render(request,'board/q_board.html')
def write(request):
        return render(request,'board/write.html')
def n_detail(request):
        return render(request,'board/n_detail.html')
def q_detail(request):
        return render(request,'board/q_detail.html')