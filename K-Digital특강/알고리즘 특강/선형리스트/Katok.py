
# 함수선언

def add_data(friend) :
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

def insert_data(position,friend):
    katok.append(None)
    klen = len(katok)

    for i in range(position,friend,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend


def delete_data(position):
    klen = len(katok)
    katok[position] = None

    for i in range(position,klen,+1):
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[klen-1])

# 전역변수 선언
katok = []
select = -1

# 메인 코드

if __name__ == "__main__":

    while(select != 4):
        select = int(input("선택하세요(1:추가, 2:삽입, 3:삭제, 4:종료)"))

        if (select==1):
            data = input("추가 할 데이터 : ")
            add_data(data)
            print(katok)

