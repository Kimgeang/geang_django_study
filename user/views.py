from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터 베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        # password와 password2가 같이않다면
        if password != password2:
            return render(request, 'user/signup.html')
        else:

            exist_user = get_user_model().objects.filter(username=username)
            # exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)

        #         new_user = UserModel()
        #         new_user.username = username
        #         new_user.password = password
        #         new_user.bio = bio
        # # 위의형태는 변수에 데이터를 담아놓은것이고 실제로는 데이터베이스에 데이터 정보를 저장되지 않는 상태이다.
        # # 밑에 save를 통해서 데이터베이스에 데이터를 넣어주는 역활을 한다.
        #     new_user.save()
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)


        me = auth.authenticate(request, username = username, password = password)
        # 기존의 로그인정보가 있는지 확인하는 변수
        # me = UserModel.objects.get(username=username)
        # 데이터 베이스에 있는패스워드와 기존 입력한 패스워드를 검증하는 과정
        if me is not None:
            auth.login(request, me)
            # request.session['user'] = me.username
            return redirect('/')
        else:
            return redirect('/sign-in')


    elif request.method == 'GET':
            user = request.user.is_authenticated
            if user:
                return redirect('/')
            else:
                return render(request, 'user/signin.html')


@login_required     #로그인이 꼭 되어있어야만 접근이 가능한 함수
def logout(request):
    auth.logout(request)
    return redirect('/')