from django.shortcuts import get_object_or_404, render, redirect
from login.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .forms import UserCreationForm, UserChangeForm, UserLoginForm

def login(request):
        return render(request, 'login/login.html')

def signup(request):
        if request.method == 'POST':
                signupform = UserCreationForm(request.POST)
                if signupform.is_valid():
                        if signupform.clean_password2():
                                new_user = User.objects.create_user(
                                        signupform.cleaned_data['userId'],
                                        signupform.cleaned_data['userName'],
                                        signupform.cleaned_data['userPassword2']
                                )
                                new_user = signupform.save(commit=False)
                                new_user.address = signupform.cleaned_data['userAddress']
                                new_user.tel = signupform.cleaned_data['userTel']
                                new_user.save()
                                return render(request, 'main/main.html', {'form':signupform})
        else:
                signupform = UserCreationForm()
                return render(request, 'login/signup.html')
        return render(request, 'main/main.html', {'form':signupform})
        

def signin(request):
        if request.method == 'POST':
                signinform = UserLoginForm()
                id = request.POST['userId']
                password = request.POST['userPassword2']
                u = authenticate(userEmail=id, password=password)
                if u is not None:
                        if u.is_active:
                                login(request, user=u)
                                return redirect('main')
                else:
                        return render(request, 'login/login.html', {'error': '아이디 또는 비밀번호를 다시 확인바랍니다.'}) 
        else:
                return redirect('login')

def signout(request):
        logout(request)
        return redirect('login')
# def login(request):
#         if request.method == 'POST':
#                 userId = request.POST['userId']
#                 password = request.POST['userPassword']
#                 # user = auth.authenticate(request, username=username, password=password)
#                 new_user = authenticate(request, username=username, password=password)
#                 if new_user is not None:
#                         #로그인 성공 시
#                         # auth.login(request, user)
#                         login(request,user)
#                         return redirect('main')
#                 else:
#                         #로그인 실패 시
#                         return render(request, 'login/login.html', {'error': 'id or password is incorrect.'})
#         else:
#                 return render(request,'login/login.html')

# def signup(request):
#         if request.method == 'POST':
#                 if request.POST['userPassword1'] == request.POST['userPassword2']:
#                         #폼에서 회원정보 받아와
#                         # usertest = User.objects.create_user(
#                         #         username=request.POST['userName'],
#                         #         password=request.POST['userPassword1'])
#                         username=request.POST['userName']
#                         password=request.POST['userPassword1']
#                         email=request.POST['userId']
#                         tel=request.POST['userTel']
#                         address=request.POST['userAddress']

#                         # new_user = User(name=name, email=email, pw=password, address=address, tel=tel)
#                         new_user = User.objects.create_user(
#                                 username = username,
#                                 password = password
#                         )
#                         new_user.save()
#                         # profile = User(email=email, tel=tel, address=address)
#                         # profile = User(email=email, address=address)
#                         # profile.save()
#                         # auth.login(request, user)
#                         auth.login(new_user)
#                         return redirect('main') 
#                 else:
#                         #password와 확인용 password가 불일치 할 때
#                         return render(request, 'login/login.html', {'error': 'id or password is incorrect.'})
#                         # return HttpResponse('비밀번호가 불일치 합니다. 다시 입력해주세요')

#         else:
#                 #get방식일 경우
#                 return render(request,'login/signup.html')

# def logout(request):
#         if request.method == 'POST':
#                 logout(request)
#                 redirect('main')
#         return render(request, 'login/login.html')
#         # if user.is_athenticated() == True:
#         #         logout(request)
#         #         return render(request, 'login/login.html')
#         # else:
#         #         return redirect('main')


def googleLogin(request):
        return render(request, 'login/login.html')