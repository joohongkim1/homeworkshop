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

avg = sum(student.values()) / len(student)  # 과목별 점수를 sum 함수로 합산한 후 student의 길이로 나눔
print(avg) # 출력

```



## 3번 문제

```
# 문제
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
blood = {}

for key in set(blood_types):
        blood[key] = blood_types.count(key)
print(blood)



# 강사님 
for blood in blood_type:
if blood_dict.get(blood):
	blood_dict[blood] += 1
else:
	blood_dict[blood] = 1

```

