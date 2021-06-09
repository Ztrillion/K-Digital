# 흔히 알고 잇는 곱셈(*)을 의미
# 단순곱셈,제곱연산,가변인자 등 다양하게 활용

# *args
def asterisk(a,*args):
    print(a,args)
    print(type(args))

asterisk(1,2,3,4,5,6)

a,b,c = ([1,2],[3,4],[5,6])
print(a,b,c)

data = ([1,2],[3,4],[5,6])
print(*data)

def asterisk_a(a,b,c,d):
    print(a,b,c,d)
data = {"b":1,"c":5,"d":98}
asterisk_a("제목",**data)

for data in zip(*([1,2],[3,4],[5,6])):
    print(data)
#1은 a, 나머지는 튜플형태로 *args

#키워드인자 **kargs

def asterrisk_k(k,**kargs):
    print(k,kargs)
    print(type(kargs))
asterrisk_k(1,b=2,c=3,d=4,e=5,f=6)
# 1은 k, 나머지는 딕셔너리형태로 **kargs

# 튜블 딕셔너리