# Workshop 02

## 1번 문제

```
n = 5
m = 9
for i in range(1, m+1):
    print(n * '*')
```



## 2번 문제

```
# 문제
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}

sum = 0 # 총 점수를 저장하기 위한 변수 초기화
for number_student in student.values():
    sum += number_student  # 과목별 점수를 받아 sum에 더해 점수 총합 구하기
    print(sum / len(student)) # 총 점수를 과목 수로 나눔 
```



## 3번 문제

```
# 문제
blood_types = {'A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB'}

a = dict()
cnt_a = 0
cnt_b = 0
cnt_o = 0
cnt_ab = 0
for i in blood_types:
    if i == 'A':
        cnt_a += 1 
        a[i] = cnt_a 
    elif i == 'B':
        cnt_b += 1
        a[i] = cnt_b
    elif i == 'AB':
        cnt_ab += 1
        a[i] = cnt_ab
    else:
        cnt_o += 1
        a[i] = cnt_o
print(a)
```

