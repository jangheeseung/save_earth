from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.conf import settings

def login_required(function):
    def wrap(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/')
        return function(request, *args, *kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def superuser_required(function):
    @login_required
    def wrap(request, *args, **kwargs):
        user_id = request.session.get('user')
        um = get_user_model()
        user = um.objects.get(pk=user_id)
        if user.is_superuser < 1:
            return redirect('/')

        return function(request, *args, *kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
    