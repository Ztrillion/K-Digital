# 함수선언부
def isQueueEmpty():
    global SIZE,queue,front,rear
    if (front==rear):
        return True
    else:
        return False

def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1)% SIZE ==front):
        return True
    else:
        return False

def enQueue(data):
    global SIZE,queue,front,rear
    if (isQueueFull()):
        print("큐가 꽉찻다")
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었다")
        return
    front =(front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print("확인할 데이터가 없습니다")
        return None
    return queue[(front+1)%SIZE]


#전역변수부
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0
#main 코드부

if __name__ == "__main__" :
    select = input("삽입(1)/추출(2)/확인(3)/종료(4) : ")

    while (select != 4) :
        if select == 1 :
            data = input("입력할 데이터 : ")
            enQueue(data)
            print("큐상태 : ", queue)
            print("front : ", front, "rear : ", rear)

        elif select == 2:
            data = deQue()
            print("추출된 데이터 : ", data)
            print("큐상태 : ", queue)
            print("front : ", front, "rear : ", rear)

        elif select == 3:
            data = peek()
            print("확인 데이터 : ", data)
            print("큐상태 : ", queue)
            print("front : ", front, "rear : ", rear)

        else:
            print("입력이 잘못됨")

        select = input("삽입(1)/추출(2)/확인(3)/종료(4) : ")

    print("프로그램 종료")