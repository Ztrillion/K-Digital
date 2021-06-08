#split() : string 타입의 값을 나눠서 List 형태로 변환

i1 = 'zero one two three'.split() #빈칸을 기준으로 문자열 나누기
print(i1)

i2 = 'python,jquery,java' # ","를 기준으로 문자열 나누기
print(i2.split(","))

a,b,c = i2.split(",") #리스트에 있는 각 값을 a,b,c 변수로 unpacking

i3 = 'python.edu.fire'
sub,domain,tld = i3.split(".")
print(domain)