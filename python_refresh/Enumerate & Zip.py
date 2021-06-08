# 리스트의 element 추출 시 번호를 붙여서 추출

for a,b in enumerate(['tic','tac','toc']):
    print(a,b)

mlist = ['a','b','c','d']
print(list(enumerate(mlist))) # list에 있는 index와 값을 list로 저장

#문장을 list로 만들고 list의 index와 값을 dic으로 저장
print({i:j for i,j in enumerate('I am chart Analyst'.split())})
