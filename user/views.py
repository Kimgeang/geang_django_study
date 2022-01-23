from django.shortcuts import render, redirect
from .models import UserModel


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2= request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        # password와 password2가 같이않다면
        if password != password2:
            return render (request,'user/signup.html')
        else:
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.bio = bio
        # 위의형태는 변수에 데이터를 담아놓은것이고 실제로는 데이터베이스에 데이터 정보를 저장되지 않는 상태이다.
        # 밑에 save를 통해서 데이터베이스에 데이터를 넣어주는 역활을 한다.
            new_user.save()
        return redirect('/sign-in')


def sign_in_view(request):
    return render(request, 'user/signin.html')