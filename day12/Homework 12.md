# homework 12

```
# 1. 
반응형 웹 디자인이란 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는
_____(a)_____에 따라 가로폭이나 배치를 변경하여 가독성을 높이도록 하는 웹페이지
접근 기법이다. 여기서 (a)에 들어갈 말을 작성하시오.

(a) : Display
```



```
# 2. 
모바일 디바이스에서 반응형 웹이 정상적으로 동작하기 위해서는 head tag 내부에 특
정 meta tag를 정의하여야 한다. 여기서 말하는 meta tag의 가장 일반적인 형태를 작성
하시오.

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
```



```css
# 3.
Bootstrap에서는 총 5개의 반응형 그룹으로 나누어 화면 크기별로 다른 Layout이 표시
된다. 여기서 말하는 5개의 그룹을 구분 짓는 화면 크기의 가로 해상도 4가지를 px단위
로 작성하시오.

// Extra small devices (portrait phones, less than 576px)
// No media query for `xs` since this is the default in Bootstrap

// Small devices (landscape phones, 576px and up)
@media (min-width: 576px) { ... }

// Medium devices (tablets, 768px and up)
@media (min-width: 768px) { ... }

// Large devices (desktops, 992px and up)
@media (min-width: 992px) { ... }

// Extra large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }
```



