# lambda 함수

def f(x,y):
    return x+y
print(f(1,4))

f = lambda x,y: x+y
print(f(1,4))

f = lambda x:x**2
print(f(3))

f = lambda x:x/3
print(f(9))

f = lambda x,y:x-y
print(f(3,1))

print((lambda x: x*3)(3))

