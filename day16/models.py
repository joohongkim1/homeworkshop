from django.db import models


# 1. python manage.py makemigrations => django 한테 model 작성했음을 알림
# 2. python manage.py migrate => django 한테 실제 DB 에 작성하라고 명령

class Article(models.Model): # 장고 모델 상속
    # id(pk)는 기본적으로 처음 테이블 생성될 때 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)

    # 모든 필드는 기본적으로 NOT NULL => 비어있으면 안 된다.

    #CharField 에서는 max_length 가 필수 인자다.
    title = models.CharField(max_length=20) # 클래스 변수 (DB의 필드)
    content = models.TextField() # 클래스 변수 (DB의 필드)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'


class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()

    def __str__(self):
        return f'{name}'