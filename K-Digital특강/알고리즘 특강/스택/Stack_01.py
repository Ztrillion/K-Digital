stack = [None for _ in range(5)]
top = -1 #top기본값 -1 설정

top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print(stack)
data = stack[top]
stack[top] = None
top -= 1
print(data)

data = stack[top]
stack[top] = None
top -= 1
print(data)

data = stack[top]
stack[top] = None
top -= 1
print(data)