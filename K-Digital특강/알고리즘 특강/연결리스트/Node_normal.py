# 클래스 or 함수 선언문
import random


class Twice():
    # 생성자 init
    def __init__(self):
        #data,link 노드 구조
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

#전역변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '졍연', '쯔위', '사나', '지효'] # DB, 크롤링


# 메인코드
if __name__ == '__main__':
    
    node = Twice()
    node.data = dataArray[0] #첫번째 노드
    head = node
    memory.append(node)

    for data in dataArray[1:] : #['졍연', '쯔위', '사나', '지효']
        pre = node
        node = Twice()
        node.data = data # 정연, 쯔위....
        pre.link = node
        memory.append(node)

    printNodes(head)
