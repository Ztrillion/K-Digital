# 함수선언부

def selectionSort(ary) :
    n = len(ary)
    for i in range(0,n-1): #싸이클 반복(큰반복)
        minIdx = i
        for k in range(i+1,n) : #작은 반복
            if (ary[minIdx]>ary[k]):
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx],ary[i]
    return ary




#전역변수부

import random
dataAry = [random.randint(50,100) for _ in range(8)]




# 메인코드부

print('정렬전 : ', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후:', dataAry)