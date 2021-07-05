import random
# 클래스 , 함수 선언부
class Node:
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link != None :
        current = current.link
        print(current.data, end=' ')
    print()

# 삽입
def insertNodes(findData,insertData) :
    global memory,head, current,pre

    #첫번째 노드 삽입
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    # 중간노드 삽입
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # 마지막 노드 삽입
    node = Node()
    node.data = insertData
    current.link = node

def deleteNode(deleteData) :
    global memory,head, current, pre

    # 첫번째 노드 삭제
    if head.data == deleteData :
        current = head
        head = head.link
        del(current)
        return

    #첫번째 외 노드 삭제
    current - head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return
#전역변수
memory = []
head, pre, current = None, None, None
dataArray = [random.randint(1000,9999) for _ in range(20)]

#main

if __name__ == '__main__':
    #첫번째 노드
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data =data
        pre.link = node
        memory.append(node)

    printNodes(head)