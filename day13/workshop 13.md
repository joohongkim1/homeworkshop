# workshop 13

1. 이름이 'classroom' 인 프로젝트를 생성하시오. (초기 setting을 수행 후 진행하는 것으로 가정했습니다.)

```bash
(venv)
$ django-admin startproject classroom .  # classroom 프로젝트 생성
```



2. ‘info/'' 의 주소로 접속했을 때 , 다음과 같이 반의 정보를 보여주는 페이지를 만드시오.

   1) pages application 생성

   ```bash
   $ python manage.py startapp pages
   ```

   2) settings.py 

```python
INSTALLED_APPS = [
	'pages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

​	  3) url.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('info/', views.info),
    path('admin/', admin.site.urls),
]  # views.py 에 있는 info 함수를 받아옴.
```

​	4) views.py

```python
from django.shortcuts import render

def info(request):
    return render(request, 'info.html')
```

​	5) templates 폴더 생성 후 info.html 생성

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Info page</title>
</head>
<body>
  <h1>우리반정보</h1>
  <h3>Teacher</h3>
  <ul>
  <li>Name</li>
  </ul>
  <h3>Student</h3>
  <ul>
    <li>홍길동</li>
    <li>김길동</li>
    <li>박길동</li>
  </ul>
</body>
</html>
```





3. ‘/ 학생이름 의 주소로 접속했을 때 , 다음과 같이 학생의 이름과 나이를
   보여주는 페이지를 만들어 주세요.

   1) url.py

   ```python
   from django.contrib import admin
   from django.urls import path
   from pages import views
   
   urlpatterns = [
       path('student/<str:name>/<int:age>', views.student),
       path('admin/', admin.site.urls),
   ]
   ```

   2) views.py

   ```python
   from django.shortcuts import render
   
   def student(request, name, age): # name과 age를 받아 context 에 저장 후 context 를 전달
       context = {
           'name': name,
           'age': age,
       }
       return render(request, 'student.html', context)
   ```

   3) templates 폴더 안에 student.html 생성

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>Student</title>
   </head>
   <body>
     <h1>이름: {{ name }}</h1>   <!-- name과 age를 변수로 받아줌 -->
     <h3>나이: {{ age }}</h3>
   </body>
   </html>
   ```

   