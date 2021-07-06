# ## 50-1까지 합계
#
# def addNumber(num) :
#     if num <= 1 :
#         return 1
#     return num + addNumber(num-1)
# print(addNumber(50))
#
# ## 팩토리얼 구현(10부터 1까지 곱하기)
# ## 일반코드
# factValue = 1
# for n in range(10,0,-1):
#     factValue *= n
# print(factValue)
#
# ## 재귀함수로 호출
#
# def factorial(num):
#     if num <= 1 :
#         return 1
#     print("%d * %d : " %(num,num-1))
#     retVal = factorial(num-1)
#
#     print("%d * %d (=%d)반환" %(num,num-1,retVal) )
#     return num * retVal
# print("\n5=", factorial(5))

## 우주선 발사 카운트다운

def countDown(n) :
    if n == 0 :
        print("발사!!")
    else:
        print(n)
        countDown(n - 1)
countDown(10)

def star(s):
    if s > 0:
        star(s-1)
        print('*'*s)
star(5)