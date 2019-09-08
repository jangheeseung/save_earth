from django.shortcuts import redirect
from django.login.models import User

def login_required(function):
    def wrap(request, *args, *kwargs):
        user_id = request.session.get('user'):
        # user =     
        #     return redirect('/')
        # return fu
