# workshop 07

```
# 1. Animal 을 상속받아 Dog 클래스와 Bird 클래스를 정의

class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def run(self):
        print(f'{self.name}! 달린다!')  # walk 와 eat 메서드는 부모 클래스에 존재

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f'{self.name}! 푸드덕!') # walk 와 eat 메서드는 부모 클래스에 존재

dog = Dog('바둑이')
dog.walk()
dog.run()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()

```

