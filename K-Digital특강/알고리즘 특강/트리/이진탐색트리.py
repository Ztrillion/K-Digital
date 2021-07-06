# 왼쪽은 작은 수 , 오른쪽은 큰 수
# 메모리를 만들고 root만 잡고있으면 됨.


class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None




#전역변수
memory = []
root = None
#DB 또는 CRAWLING DATA 집합
nameArray = ['걸스데이','레드벨벳','블랙핑크','트와이스','마마무','SES']

#첫번째 노드 생성

name = nameArray[0]
node = TreeNode()
node.data = name
root = node
memory.append(node)

#두번째부터는 달라짐


for name in nameArray[1:] :
    node = TreeNode()
    node.data = name
    current = root
    while True :
        if name < current.data :
            # 왼쪽에 None 이면 current left
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right== None:
                current.right = node
                break
            current = current.right
    memory.append(node)

#데이터검색
findName = '마마무'
current = root
while True :
    if current.data == findName :
        print(findName,"을 찾았음")
        break
    elif current.data > findName :
        if current.left == None :
            print(findName,"없음 ㅜㅜ")
            break
        current = current.left
    else:
        if current.right == None:
            print(findName,"없음 ㅜㅜ")
            break
        current = current.right