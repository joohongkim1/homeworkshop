# homework 07

```
class Calculator:
    count = 0

    def info(self):
        print('나는 계산기 입니다.')

    
    @staticmethod
    def add(a, b):
        Calculator.count += 1
        print(f'{a} + {b} 는 {a + b} 입니다.')

    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')
```



```
# 1. 
- 인스턴스 메서드 : info(self)
  -> 데코레이터가 없다. 
  -> 첫 번째 인자로 self를 받도록 정의. 자동으로 인스턴스 객체가 self가 된다.
  
- 스태틱 메서드 : add()
  -> @staticmethod 데코레이터
  -> 인자 정의가 자유롭다.
  -> 어떠한 인자도 자동으로 넘어가지 않는다.
  
- 클래스 메서드 : history(cls)
  -> @classmethod 데코레이터
  -> 첫 번째 인자로 cls를 받도록 정의. 자동으로 클래스 객체가 cls가 된다.
 
```



```
# 2.
cal = Calculator()

cal.info()
cal.add(1, 2)
cal.add(2,3)
cal.history()

[결과]
나는 계산기 입니다.
1 + 2 는 3 입니다.
2 + 3 는 5 입니다.
총 2번 계산 했습니다.
```



```
# 3.
- self 에는 인스턴스 객체가 할당
- cls 에는 클래스 객체가 할당
```

