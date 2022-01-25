# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('tweet/', views.tweet, name='tweet'), # 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
    # Tweet에 있는 고유 아이디값을 받아오기위해 <int:id>라는 값을 받아왔음

    path('tweet/delete/<int:id>',views.delete_tweet, name='delete-tweet'),

]