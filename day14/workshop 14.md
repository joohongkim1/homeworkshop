# Workshop 14

1) url.py 에서 path 설정

```python
urlpatterns = [
    path('push/', views.push),
    path('pull/', views.pull), 
    ]
```

2) view.py 에서 push, pull 함수 작성

```python
def push(request):
    return render(request, 'push.html')

def pull(request):
    number = request.GET.get('number')
    context = {
        'number': number,
    }
    return render(request, 'pull.html', context)
```

3) push.html 생성 및 form 을 보낼 곳을 pull 로 지정

```python
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Push</title>
</head>
<body>
  <h1>Push Number</h1>
  <form action="/pull/">
    <input type="number" name="number">
    <button type="submit">Push!</button>
  </form>
  
</body>
</html>
```

4) pull.html 생성 및 출력 내용 작성

```python
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Pull</title>
</head>
<body>
  <h1>Pull Number</h1>
  <h2>Pull 해보니 {{ number }} 입니다!</h2>  // pull 함수에서 받아온 context
</body>
</html>
```

