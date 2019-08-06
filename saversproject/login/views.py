from django.shortcuts import get_object_or_404, render, redirect
from login.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from .backends import MyAuthBackend

# from .forms import UserCreationForm, UserChangeForm, UserLoginForm

# def login(request):
#         return render(request, 'login/login.html')

# def signup(request):
#         usermodel = get_user_model()
#         if request.method == 'POST':
#                 signupform = UserCreationForm(request.POST)
#                 if signupform.is_valid():
#                         new_user = usermodel.objects.create_user(
#                         email=signupform.cleaned_data['email'],
#                         name=signupform.cleaned_data['name'],
#                         password=signupform.clean_password2()
#                         )
                        
#                         signupform.save(commit=False)
#                         new_user.address = signupform.cleaned_data['address']
#                         new_user.tel = signupform.cleaned_data['tel']
#                         new_user.save()
#                         return render(request, 'main/main.html', {'form':signupform})
#         else:
#                 signupform = UserCreationForm()
#         return render(request, 'login/signup.html')
#         # return render(request, 'main/main.html', {'form':signupform})
        

# def signin(request):
#         if request.method == 'POST':
#                 signinform = UserLoginForm()
#                 id = request.POST['userId']
#                 password = request.POST['userPassword']
#                 u = authenticate(userEmail=id, password=password)
#                 if u is not None:
#                         if u.is_active:
#                                 login(request, user=u)
#                                 return render(request, 'main/main.html')
#                 else:
#                         return render(request, 'login/login.html', {'error': '아이디 또는 비밀번호를 다시 확인바랍니다.'}) 
#         else:
#                 return redirect('login')

# def signout(request):
#         logout(request)
#         return redirect('login')




def login(request):
        if request.method == 'POST':
                userid = request.POST['userId']
                password = request.POST['userPassword']
                user = get_user_model().objects.get(email=userid)
                # print(user.name+"_____________________")
                # u = authenticate(request, username=user.name, password=password)
                # user = authenticate(userid, password)
                u = MyAuthBackend.authenticate(request,email=userid, password=password)
                if u is not None:
                        #user객체가 있음
                        login(request,u)
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
                                name=request.POST['userName'],
                                password=request.POST['userPassword1']
                        )
                        
                        new_user.tel=request.POST['userTel']
                        new_user.address=request.POST['userAddress']
                        new_user.save()
                        login(new_user)
                        return redirect('main') 
                else:
                        #password와 확인용 password가 불일치 할 때
                        return render(request, 'login/login.html', {'error': 'id or password is incorrect.'})
                        # return HttpResponse('비밀번호가 불일치 합니다. 다시 입력해주세요')

        else:
                #get방식일 경우
                return render(request,'login/signup.html')

def signout(request):
        if request.method == 'POST':
                logout(request)
                redirect('main')
        return render(request, 'login/login.html')
        # if user.is_athenticated() == True:
        #         logout(request)
        #         return render(request, 'login/login.html')
        # else:
        #         return redirect('main')


def googleLogin(request):
        return render(request, 'login/login.html')