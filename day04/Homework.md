# Homework 04

```
# 1. Python에서 변수를 찾을 때 접근하는 이름 공간을 순서대로 작성하시오.
답 => LEGB , Local Scope -> Enclosed Scope -> Global Scope -> Built-in Scope
```



```
# 2. 다음 중 옳지 않은 것을 고르시오.
(1) 함수는 오직 하나의 객체만 반환할 수 있어서, ‘return a, b’처럼 쓸 수 없다. 
=> 튜플의 형태로 반환된다.
(2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
(3) 함수의 인자(parameter)는 함수를 선언할 때 설정한 값이며,
	인수(argument)는 함수를 호출할 때 넘겨주는 값이다.
(4) 가변 인자를 설정할 때는 인자 앞에 *을 붙이고, 이 때는 함수 내에서 tuple로 처리된다.

답 : 1번,  return값으로 여러 객체를 반환할 수 있다. 
     ex) def plus_minus(a, b):
    		return a+b, a-b
		print(plus_minus(1,3))


```



```
# 3. 재귀함수의 장점과 단점을 설명하시오
장점 : 코드가 더 직관적이고, 이해하기 쉽다. 변수 사용을 줄일 수 있다.
단점 : Stack overflow(메모리 스택이 넘치는 것)가 발생하거나 실행 속도가 느려진다.
```

