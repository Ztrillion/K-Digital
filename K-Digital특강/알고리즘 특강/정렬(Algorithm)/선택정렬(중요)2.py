# 전역변수

dataArray = [84,97,12,50,76,31]

#함수선언

def selet(dataArray):
    for i in range(0,len(dataArray)):
        minIdx = i
        for j in range(i+1,len(dataArray)):
            if dataArray[minIdx] > dataArray[j]:
                minIdx = j
        dataArray[i], dataArray[minIdx] = dataArray[minIdx],dataArray[i]
    return dataArray




#메인
print("정렬 전 : ", dataArray)
dataArray = selet(dataArray)
print("정렬 후 : ", dataArray)

