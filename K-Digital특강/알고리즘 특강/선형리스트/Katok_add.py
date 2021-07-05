katok = [] #빈 배열

def add_data(friend) :

    katok.append(None)
    klen = len(katok) # 카톡의 길이
    katok[klen-1] = friend

add_data('다현')
add_data('졍연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)
