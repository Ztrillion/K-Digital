# 두개의 list값을 병렬적으로 추출
aa = ['a1','a2','a3']
bb = ['b1','b2','b3']

for i,j in zip(aa,bb):
    print(i,j)

for i,(a,b) in enumerate(zip(aa,bb)):
    print(i,a,b) # i=index, a,b

a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c) # zip을 이용해 같은 index 끼리 묶음

