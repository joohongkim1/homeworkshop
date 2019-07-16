# Homework 02

## 1번 

````
# 아래 보기 중, 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을
구분 하시오.  => String, List, Tuple, Range, Set, Dictionary

mutable -> Set, Dictionary, List
immutable -> String, Tuple, Range
````



## 2번

```
# range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.

r = list(range(1, 51)) # 1부터 50까지의 숫자로 이루어진 리스트 생성
result = r[0:50:2] # r리스트에서 1부터 2씩 증가시켜서 홀수만 result에 저장
print(result) # 출력

```

## 3번

```
# 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 딕셔너리를 만드시오.

d = dict({'kim': 23, 'kang': 24, 'shin': 25}) 
print(d)
```



