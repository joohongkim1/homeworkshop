# workshop

```
# 문제 , 이분법을 이용 제곱근 근사값 구하기

def sqr(x):
    y = 1 
    temp = x
    while True:
        if round(y, 4) == round(temp, 4):
            break
        if x > y ** 2:
            y = (y + temp) / 2
            if x < y ** 2:
                y = 2 * y - temp
        if x < temp ** 2:
            temp = (y + temp) / 2
            if x > temp ** 2:
                temp = temp * 2 - y
    return y, temp 

n = int(input())
print(sqr(n))

# 강사님

import math

# 이분법으로 제곱근 구하기
def my_sqrt(n):
    x, y = 1, n
    result = 1 # 우리가 추측하는 제곱근 result

    while abs(result ** 2 - n) > 0.000000000001:
        result = (x + y) / 2
        if result ** 2 < n:
            x = result
        else:
            y = result

    return result

print('math.sqrt: \t', math.sqrt(2))
print('my_sqrt: \t', my_sqrt(2))
```

