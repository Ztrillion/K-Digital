# 2차원 배열 생성 클래스

class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]



#전역변수
G1, G3 = None, None
#메인코드
# 그래프의 정점 연결
G1 = Graph(4)
G1.graph[0][1] = 1;G1.graph[0][2] = 1;G1.graph[0][3] = 1
G1.graph[1][0] = 1;G1.graph[1][2] = 1
G1.graph[2][0] = 1;G1.graph[2][1] = 1;G1.graph[2][3] = 1
G1.graph[3][0] = 1;G1.graph[3][2] = 1

print('G1무방향 그래프')
for row in range(4):
    for cols in range(4):
        print(" ",G1.graph[row][cols], end=' ')
    print()


