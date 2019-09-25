# homework day20

```python
# 1.School 모델과 Student 모델을 1:N 관계로 설정하려고 한다 . models.py 의 Student 모델
# 에서 필요한 코드를 작성하시오

class Student(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
```



```python
# 2.
# Question 모델과 Comment 모델은 1:N 관계를 형성하고 있다
	question = Question.objects.get(id=id)
# 위와 같은 코드가 있을 때 , views.py 에서 해당 Question 의 모든 Comment 를 가져오기
# 위한 코드를 작성하시오 . 단 , related_name 은 설정하지 않았다고 가정한다

-> question = Question.comment_set.all()
```



```python
# 3.기본적으로 1:N 관계를 설정할 때 , ForeignKey 를 이용해서 1 에 해당하는 클래스를 지정
# 한다 . 지정한 클래스가 Movie 일 때 , ForeignKey 로 지정된 컬럼의 이름은 무엇인가

답 : movie_id
```

