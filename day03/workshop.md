# Workshop 03

```
# Problem : 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.

def palindrome(word):
    for i in range(len(word) // 2): # 입력된 단어 길이의 1/2 만큼의 범위까지 for문
        if word[i] != word[-1 - i]: # 대칭되는 위치에 있는 단어들을 비교한 후 값이 다르면
            return False # False 리턴
    return True # 대칭 위치의 단어들이 모두 같다면 True 리턴

def palindrome2(word):
    return True if list(word) == list(reversed(word)) else False

# 강사님
def palindrome(word):
return word == word[::-1]
```

