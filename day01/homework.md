# Homework

## 1번문제

```
# 사용 불가능한 식별자 예약어
import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## 2번문제

```
# float 비교
import math
a = 0.1 * 3
b = 0.3
print(math.isclose(a, b))
```

## 3번문제

```
print("안녕하세요. /n 저는 /t 김주홍입니다.\\")
```

## 4번문제

````
name = '철수'
print(f'안녕, {name}야')
````

## 5번문제

- 다음 중 형변환시 오류가 발생하는 것은?

  1) str(1)	2) int('30')	3) int(5)	4) bool('50')	5) int('3.5')

  답 : 5번  => string형 '3.5'를 int형으로 변경 불가 , float형 3.5는 int형으로 변환 가능

