# homework 06

```
# 1. Python에서 기본적으로 정의되어 있는 클래스 5가지
- str : instance=> '', 'hello', '123'   methods => .capitalize(), .join(), .split()
- list : instance => [], ['a', 'b']   methods => .append(), .reverse(), sort()
- dict : instance => {}, {'key', 'value'}   methods => .keys(), .values(), .items()
- int : instance => 0, 1 ..   attributes => .real, .imag
- float : instance => 1.5, 3.5 ...
```



```
# 2. 매직 메서드의 역할을 간단하게 작성하시오.
- __init__ : 객체 생성 시에 자동으로 호출되는 메서드
- __del__ : 객체 소멸 시에 자동으로 호출되는 메서드
- __str__ : 객체의 비공식적인 문자열 출력 시 사용, 사용자가 보기 쉬운 형태로 보여줄 때 사용
- __repr__ : 객체의 공식적인 문자열 출력 시 사용, 시스템이 해당 객체를 인식할 수 있는 공식적인 문자열로 
			나타내줄 때 사용
```



```
# 3. 문자열, 리스트, 딕셔너리 등을 조작하는 메서드 3가지를 그 역할과 함께 작성하시오.
- 리스트 조작 메서드 : .append()  => 리스트에 값 추가
- 문자열 조작 메서드 : .replace() => 기존 문자열을 다른 값으로 대체
- 딕셔너리 조작 메서드 : .keys(), .values(), .items() => 차례대로 딕셔너리의 key, value, (key, value) 를 						출력
```

