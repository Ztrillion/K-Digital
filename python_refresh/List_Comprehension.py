# 기존 list 사용으로 다른 list를 만듬
#포괄적 list, 포함되는 list라는 의미로 사용됨

result = []
for i in range(10):
    result.append(i)
print(result)

result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i%2==0]
print(result)

#list comprehensions 중첩 for문
a1 = ["A","B","C"]
a2 = ["D","E","F"]
result = [i+j for i in a1 for j in a2]
print(result)
result = [i+j for i in a1 for j in a2 if not (i==j)]
print(result)

result = [[i+j for i in a1]for j in a2]
print(result)  # 괄호 뒤가 먼저 고정

for i in range(1,6):
    print(' '*(6-i)+'*'*(2*i-1))

for i in range(1,6):
    print(' '*(6-i)+"*"*(2*i-1))