from django.contrib import admin
<<<<<<< HEAD
# import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('saversproject/saversproject'))))
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# import sys
# sys.path.insert(0, 'saversproject/saversproject')
from .models import *


# Register your models here.

class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content']

class QABoardAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'title','content']

class QABoardCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'q_a']

admin.site.register(NoticeBoard, NoticeBoardAdmin)
admin.site.register(QABoard, QABoardAdmin)
admin.site.register(QABoardComment, QABoardCommentAdmin)


=======

# Register your models here.
>>>>>>> d0b4b02740d8cbb7c7ff0db556e1bfbf89ec8286
