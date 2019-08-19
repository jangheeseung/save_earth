from django.shortcuts import get_object_or_404, render, redirect
from .models import NoticeBoard, QABoard, QABoardComment
from .forms import NoticeForm, QAForm, CommentForm
from django.utils import timezone

# Create your views here.
# def board(request):
#         notices = NoticeBoard.objects
#         posts = QABoard.objects
#         return render(request,'board/board.html', {'notices':notices})

def noticeboard(request):
        notices = NoticeBoard.objects
        return render(request, 'board/n_board.html', {'notices':notices})

def qaboard(request):
        questions = QABoard.objects
        return render(request, 'board/q_board.html', {'questions':questions})

def write(request):
        return render(request,'board/write.html')
def detail(request):
        return render(request,'board/detail.html')

#글 생성 함수
def n_create(request):
        notice = NoticeBoard()
        if request.method == 'POST':
                form = NoticeForm(request.POST, instance=notice)
                notice.title = request.POST['title']
                notice.content = request.POST['content']
                if form.is_valid():
                        notice = form.save(commit=False)
                        pub_date = timezone.datetime.now()
                        notice.save()
                        return redirect('noticeboard')
        else:
                form = NoticeForm(instance=notice)
                return render(request, 'board/write.html', {'form':form})    
        
def q_create(request):
        question = QABoard()
        if request.method == 'POST':
                form = QAForm(request.POST, instance=question)
                question.title = request.POST['title']
                question.content = request.POST['content']
                if form.is_valid():
                        question = form.save(commit=False)
                        pub_date = timezone.datetime.now()
                        notice.save()
                        return redirect('qaboard')
        else:
                form = QAForm(instance=question)
                return render(request, 'board/write.html', {'form':form})        

#notice 카테고리의 디테일을 보여줄 함수
def notice_detail(request, noticeboard_id):
        print("_____________________________들어옴_")
        n_detail = get_object_or_404(NoticeBoard, pk=noticeboard_id)
        return render(request, 'board/n_detail.html', {'n_detail':n_detail})

#q&a 카테고리의 디테일을 보여줄 함수
def QandA_detail(request):
        q_detail = get_object_or_404(QABoard, pk=qaboard_id)
        return render(request, 'board/q_detail.html', {'q_detail':q_detail})
