#map function과 달리 list에 똑같은 함수를 적용해서 통합

from functools import reduce

print(reduce(lambda x,y:x+y, [1,2,3,4,5]))

def factorial(n):
    return reduce(lambda x,y:x*y, range(1,n+1))

print(factorial(5))

# lambda, map, reduce 는 간단한 코드로 다양한 기능제공
# but 코드의 직관성이 떨어져서 lambda나 reduce는 python3에서 사용권장 안함
# legacy library나 다양한 머신러닝 코드는 여전히 사용