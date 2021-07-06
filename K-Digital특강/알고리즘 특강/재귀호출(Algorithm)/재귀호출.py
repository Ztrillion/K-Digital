# 재귀호출 : 자기 자신을 무한으로 호출


def openBox():
    global count
    print("종이상자 열기")
    count -= 1
    if count == 0 :
        print("반지넣기")
        return
    openBox()
    print("종이상자를 닫습니다.")



#전역변수
count = 10

openBox()