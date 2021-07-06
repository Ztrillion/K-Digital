# 선택정렬
# 최솟값 위치 찾는 함수

def findMin(ary):
    min = 0
    for i in range(1,len(ary)):
       if(ary[min]> ary[i]) :
           min = 1
    return min


#전역변수
import random
before = [random.randint(50,100) for _ in range(8)]
after = []

#메인코드부

print('정렬전 : ', before)
for _ in range(len(before)):
    minpos = findMin(before)
    after.append(before[minpos])
    del(before[minpos])

print('정렬 후:',after)