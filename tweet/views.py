from django.shortcuts import render, redirect
from .models import TweetModel
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    #유저가 로그인이 되어있는지 확인 하는 변수
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')


def tweet(request):
    if request.method == 'GET':
        #유저가 로그인이 되어있는지 확인 하는 변수
        user = request.user.is_authenticated
        # user의 값이 true(있다) 라면
        if user:
            # 여기서 데이터 베이스에서 저장된 순서(최신순)으로 저장이 되지만
            # order_by를 사용함으로서 created_at 순서를 역순으로 나열해주는
            # 함수를 사용하고 음수-를 사용하여 역순으로 정렬해주는 역활을 하게된다.

            all_tweet = TweetModel.objects.all().order_by('-created_at')
            # home 화면으로 가준다
            return render(request, 'tweet/home.html',{'tweet':all_tweet})

        #만약 유저가 로그인정보가 없다면
        else:
            # 로그인 화면으로 가준다다
            return redirect('/sign-in')
    elif request.method == 'POST':
        user = request.user
        content = request.POST.get('my-content','')

        if content == '':
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request,'tweet/home.html', {'error':'글은 공백일수 없습니다','tweet':all_tweet})
        else:
            my_tweet = TweetModel.objects.create(author=user, content=content)
            my_tweet.save()
            # my_tweet = TweetModel()
            # my_tweet.author = user
            # my_tweet.content = request.POST.get('my-content','')
            # my_tweet.save()
            return redirect('/tweet')

# 로그인이 되어있어야만 실행되는 함수
@login_required
def delete_tweet(request,id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')

