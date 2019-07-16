# Workshop

## problem 1

- 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

  ```
  # 문제
  n = 5
  m = 9
  
print((('*' * n) + '\n') * m)
  ```

  
  
  

## problem 2

- print 함수를 한 번만 사용해 다음 문장을 출력하시오![1563179293087](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563179293087.png)

```
print('\"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')
```

## problem 3

- 다음과 같은 이차방정식이 있을 때 근을 찾는 수식을 파이썬 코드를 이용하여 출력해보시오.

```
import math

a = int(input())
b = int(input())
c = int(input())

x = (b ** 2) - 4 * a * c

if x > 0:
    x1 = (-b + math.sqrt(x)) / (2 * a)
    x2 = (-b - math.sqrt(x)) / (2 * a)
    print(x1, x2)
elif x == 0:
    x1 = -b / (2 * a)
else:
    print("근이 없습니다.")
    
```

