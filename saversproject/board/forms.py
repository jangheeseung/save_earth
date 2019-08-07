from django import forms
from .models import NoticeBoard, QABoard, QABoardComment
class NoticeForm(forms.ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ['title', 'content']

class QAForm(forms.ModelForm):
    class Meta:
        model = QABoard
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = QABoardComment
        fields = ['content']
