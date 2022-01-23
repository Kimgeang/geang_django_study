from django.contrib import admin # 장고에서 어드민 툴을 사용하겠다는 뜻
from .models import UserModel #내가 생성한 models.py에서 UserModel의 속성을 가지고 오겠다는 뜻

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다