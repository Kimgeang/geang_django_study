#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        #데이터베이스 테이블 이름설정
        db_table = "my_user"
    # 데이터 베이스에 들어갈 내용
    # 유저네임
    # username = models.CharField(max_length=20, null=False)
    # # 유저 패스워드
    # password = models.CharField(max_length=256, null=False)
    # # 새로 생성한 날짜 (유저정보를 입력하면 자동으로 생성됨)
    # created_at = models.DateTimeField(auto_now_add=True)
    # # 수정한 날짜 (유저정보를 입력하면 자동으로 생성됨)
    # updated_at = models.DateTimeField(auto_now=True)
    # 유저 상태 메세지
    bio = models.CharField(max_length=256, default='')



    #django 모델 필드의 종류

        # 문자열 : CharField, TextField
        # 날짜/시간: DateTimeField, DateField, TimeField
        # 숫자 : IntegerField, FloatField
        # 다른 테이블과 연관을 지어 줄 때 : ForeignKey

    # 새로생성한 데이터 베이스를 인식시켜주는 터미널 명령어
        # python manage.py makemigrations

    # 인식한 데이터들을 데이터 베이스에 적용 시켜주는 터미널 명령어
        # python manage.py migrate

