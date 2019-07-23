# homework 05

````
# 1. 아래와 같은 코드가 fibo.py 파일에 작성되어 있을 때, 아래와 같이 함수를 실행할 수 있도록 하는 import 구문을 (A), (B), (C)를 채워 넣어 완성하시오.

def fibo_recursion(n):
	if n < 2:
		return n
	else:
		return fibo_recursion(n-1) + fibo_recursion(n-2)
		
from (A) import (B) as (C)
recursion(4)

답
(A) : fibo 		(B) fibo_recursion 		(C) recursion
````

```
# 2. 
- ZeroDivisionError : 나눗셈에서 나누는 수가 0인 경우 발생
- NameError : 정의되지 않은 변수가 호출될 때 발생
- TypeError : str + int 같이 타입이 맞지 않는 경우 발생
- IndexError : 존재하지 않는 인덱스의 값을 검색할 경우 발생
- KeyError : 딕셔너리에서 없는 키로 검색하는 경우 발생
- ModuleNotFoundError : 모듈 이름을 잘 못 써서 import하거나 없는 모듈을 호출하는 경우 발생
- ImportError : 모듈 안에 존재하지 않는 함수를 import하는 경우 발생
```

