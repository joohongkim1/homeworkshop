# workshop 05

```
# 1. 2개의 숫자를 인자로 받아 더하기, 빼기, 곱하기, 나누기 연산의 결과를 반환하는 4개의 함수를 calc.py에 작성하시오. 단, 나누기 연산에서는 try except 구문을 사용하여 '0'으로 나누려고 하는 경우에는 문자열 '0으로는 나눌 수 없습니다.'을 반환하시오.

def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiple(x, y):
    return x * y
def divide(x, y):
    try: 
        return  x / y
    except ZeroDivisionError:
        return "0으로는 나눌 수 없습니다."
```



```
# 2. 1번의 모듈을 import하여, 함수 실행 코드 작성
import calc 
print(calc.plus(1, 3))
print(calc.minus(1, 3))
print(calc.multiple(1, 3))
print(calc.divide(1, 0))

[결과]
student@M702 MINGW64 ~/homeworkshop/day05 (master)
$ python workshop.py
4
-2
3
0으로는 나눌 수 없습니다.
```

