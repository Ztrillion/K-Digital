katok = ['다현', '졍연', '쯔위', '사나', '지효']

# 중간 데이터 삭제

def delete_data(position) :
    klen = len(katok)
    katok[position] = None
    # 맨 뒤부터 앞으로 땡기기
    for i in range(position+1,klen,1) :
        katok[i-1] = katok[i]
        katok[i] = None

    # 다 땡겼으면 마지막칸 삭제
    del(katok[klen-1])

delete_data(1)
print(katok)
delete_data(3)
print(katok)