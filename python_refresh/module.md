# deque

## - Stack 과 Queue를 지원하는 모듈

## - List에 비해 효율적인 자료 저장 방식을 지원

```python
from collections import deque
deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)
deque_list.appendleft(10)
print(deque_list)
```



## - deque는 기존 list 보다 효율적인 자료구조 제공

## - 효율적 메모리 구조로 처리속도 향상

```python
# deque
from collections import deque
import time
start_time = time.clock()
deque_list = deque()
#stack
for i in range(10000):
    for i in range(10000):
        deque_list.append(i)
        deque_list.pop()
print(time.clock() - start_time, "seconds")
```

```python
#general list
import time
start_time = time.clock()
just_list = []
for i in range(10000):
    for i in range(10000):
        just_time.append(i)
        just_time.pop()
print(time.clock() - start_time, "seconds")
```



# OrderedDict

## Dict 와 달리, 데이터를 입력한 순서대로 dict를 반환

```python
for k,v in OrderedDict(stored(d.items(),key=lambda t:t[0])).items():
print(k,v)
```



# defaultdict

## - Dict type의 값에 기본값을 지정, 신규값 생성시 사용

```python
from colloctions import defaultdict
d = defaultdict(object)   #default dictionary 생성
d = defaultdict(lambda:0) # default 값을 0으로 설정
print(d["first"])
```



# Counter

## - Sequence type의 data element 들의 갯수를 dict 형태로 반환

```python
c = Count()
c = Count("anonymous")
print(c)
```



