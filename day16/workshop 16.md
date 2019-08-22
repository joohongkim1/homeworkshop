# workshop 16

1. 자신의 반에 있는 사람들의 데이터를 저장하는 Student Model 을 models.py 에
   작성하시오 . 

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()
```



2. 모델 마이그레이션 작업을 수행한 후 , Admin 페이지에서 주변 학생 3 명의 정보를
   삽입하시오

```bash
$ python manage.py makemigrations
```

![1566459945009](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566459945009.png)

3. 정보를 삽입한 후 , Admin 페이지에서 학생들의 목록을 보기 쉽게 만들기 위하여
   ‘__ 메소드를 작성하여 name 이 출력되도록 하시오

```python
def __str__(self):
        return f'{name}'
```



