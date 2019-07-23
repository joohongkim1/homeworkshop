def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiple(x, y):
    return x * y
def divide(x, y):
    try: 
        return  x / y
    except ZeroDivisionError:
        return "0으로는 나눌 수 없습니다."
