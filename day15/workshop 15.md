# workshop 15

1. base.html 파일 작성

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>
    {% block title%}{% endblock %}
  </title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
  <h1>Base is everywhere!</h1>
  {% block content %}
  {% endblock %}

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```



2. pages/url.py 경로 지정

```python
urlpatterns = [
    path('one/', views.one),
    path('two/', views.two),
    ]
```



3. view.py 함수 작성

```python
from django.shortcuts import render

def one(request):
    return render(request, 'pages/one.html')

def two(request):
    return render(request, 'pages/two.html')
```



4. one.html, two.html 작성

```python
{% extends 'base.html' %}

{% block title %}one{% endblock  %}

{% block content %}
  <h2>I am one!</h2>
{% endblock  %}

{% extends 'base.html' %}

{% block title %}two{% endblock  %}

{% block content %}
  <h2>I am two!</h2>
{% endblock  %}


```

