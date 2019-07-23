# workshop 06

```
# 1. x, y 좌표가  (2,4)고 반지름이 3인 원의 둘레와 넓이 구하기

class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)
        

c = Circle(3, 2, 4)
print(c.area())
print(c.circumference())
```



