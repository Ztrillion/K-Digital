# Sequence 자료형 각 element에 동일한 function을 적용
# map(function_name,list_data)
# lambda의 함수가 sequence 함수에 각각 적용됨
# 리스트를 붙여줘야함
ex = [1,2,3,4,5]
f = lambda x:x ** 2
print(list(map(f,ex)))

f = lambda x,y:x+y
print(list(map(f,ex,ex)))

print(list(map(lambda x: x**2 if x % 2 == 0 else x,ex)))

