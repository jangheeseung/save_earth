from django.shortcuts import get_object_or_404, render, redirect
from login.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
# from .backends import MyAuthBackend

# from .forms import UserCreationForm, UserChangeForm, UserLoginForm


def signin(request):
        if request.method == 'POST':
                # userid = request.POST['userId']
                email = request.POST['userId']
                password = request.POST['userPassword']
                
                print(email + ' ' + password)
                user = authenticate(email=email, password=password)
                # u = MyAuthBackend.authenticate(request, userid, password)
                print("____________________________________________________________________--------->", user)
                if user is not None:
                        #user객체가 있음
                        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                        return redirect('main')
                else:
                        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&없대 왜 없어&&&&&&&&&&&&&&&&&&&&&&")
                        #user객체가 None
                        return render(request, 'login/login.html', {'error': '해당 아이디가 존재하지 않습니다.'})
        else:
                return render(request,'login/login.html')
                

def signup(request):
        if request.method == 'POST':
                if request.POST['userPassword1'] == request.POST['userPassword2']:
                        #폼에서 회원정보 받아와
                        usermodel = get_user_model()
                        new_user = usermodel.objects.create_user(
                                email=request.POST['userId'],
                                password=request.POST['userPassword1'],
                                name=request.POST['userName'],
                                tel = request.POST['userTel'],
                                address = request.POST['userAddress'],
                        )
                        
                        # new_user.tel=request.POST['userTel']
                        # new_user.address=request.POST['userAddress']
                        # new_user.save()
                        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
                        # return redirect('login')
                        return redirect('main') 
                else:
                        #password와 확인용 password가 불일치 할 때
                        return render(request, 'login/signup.html', {'error': '비밀번호가 불일치합니다.'})
                        # return HttpResponse('비밀번호가 불일치 합니다. 다시 입력해주세요')

        else:
                #get방식일 경우
                return render(request,'login/signup.html')

def signout(request):
        logout(request)
        return redirect('main')
        # if user.is_athenticated() == True:
        #         logout(request)
        #         return render(request, 'login/login.html')
        # else:
        #         return redirect('main')


def googleLogin(request):
        return render(request, 'login/login.html')