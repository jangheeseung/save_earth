<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def board(request):
        return render(request,'board/board.html')
>>>>>>> d0b4b02740d8cbb7c7ff0db556e1bfbf89ec8286
