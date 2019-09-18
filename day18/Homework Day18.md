# Homework Day18

```
1. 
1) 파일보다 더 빠르게 데이터에 접근 가능
2) 특정 패턴에 맞춰 데이터 쉽게 추출 가능
3) 많은 사용자의 동시 접근에 자체 해결법을 가지고 있다.
4) 자체적 권한 시스템을 가진다.
```



```
2.
1) T
2) F
3) T
4) F
5) F
```



```sqlite
3.
sqlite> .nullvalue 'NULL'
sqlite> CREATE TABLE ssafy(
   ...> id INTEGER PRIMARY KEY,
   ...> location TEXT,
   ...> class INTEGER
   ...> );
sqlite> INSERT INTO ssafy (id, location)
   ...> VALUES(1, 'JEJU');
sqlite> SELECT class FROm ssafy WHERE id=1;
class
----------
NULL
```

