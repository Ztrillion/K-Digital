class Twice():
    # 생성자 init
    def __init__(self):
        #data,link 노드 구조
        self.data = None
        self.link = None

node1 = Twice()
node1.data = '다현'

node2 = Twice()
node2.data = '정연'
node1.link = node2

node3 = Twice()
node3.data = '쯔위'
node2.link = node3

node4 = Twice()
node4.data = '사나'
node3.link = node4

node5 = Twice()
node5.data = '지효'
node4.link = node5

#노드삽입
newNode = Twice()
newNode.data = '영성'
newNode.link = node2.link
node2.link = newNode


current = node1
print(current.data, end=' ')
while current.link != None :
    current = current.link
    print(current.data, end=' ')
