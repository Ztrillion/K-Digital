def isStackFull():
    global SIZE, stack, top

    # 스택이 꽉 찾는지 확인
    if(top >= SIZE -1) :
        return True
    else:
        return False

def push(data) :
    global  SIZE, stack, top
    if isStackFull() :
        print("스택꽉찼다")
        return
    top += 1
    stack[top] = data

# 비어있는지 확인
def isStackEmpty() :
    global  SIZE, stack, top
    if (top == -1) :
        return True
    else:
        return False


# 데이터 추출해서 리턴
def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        print("스택이 비었습니다")
        return None
    data = stack[top]
    stack[top] = None
    top = -1
    return data

# 전역변수
SIZE = 5
stack = ['커피','석류쥬스',None,None,None]
top = 1

print("스택 비어있니? : ", isStackEmpty())
print(stack)
retdata = pop()
print('추출한 데이터 : ', retdata)
