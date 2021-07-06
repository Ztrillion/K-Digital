#함수 선언부

# 큐가 꽉찼는지 확인
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE-1) and (front == -1) :
        return True
    else:
        for i in range(front+1,SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -=1
        rear -=1
        return False

def isQueueEmpty():
    global SIZE,queue,front,rear
    if (front==rear):
        return True
    else:
        return False

# 데이터 추가
def enQueue(data):
    global SIZE,queue,front,rear
    if (isQueueFull()):
        print("큐가 꽉찻다")
        return
    rear += 1
    queue[rear] = data

# 데이터 추출
def deQue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었다")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data
# 전역변수부
SIZE = 5
queue = [None for _ in range(SIZE)]
front = -1
rear = -1
#메인코드부

# print("큐가 꽉찾는지? : ", isQueueFull())
# print("큐가 비었니? : ", isQueueEmpty())
print(queue)
enQueue('화사'); enQueue('솔라'); enQueue('휘인')
print(queue)

retData = deQue()
print(retData)
print(queue)