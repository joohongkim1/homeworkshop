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
```

