# tweet/models.py
from django.db import models
from user.models import UserModel # user폴더속에 models파일의 UserModel 이라는 속성을 가지고와서 사용한다.


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"
    # 작성자
    # ForeignKey - 다른데이터 베이스에 데이터를 가지고 오겠다라는 명령어
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)