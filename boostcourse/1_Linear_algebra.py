
#Vector
x = [2,2]
y = [5,8]
z = [4,6]

result = [sum(i) for i in zip(x,y,z)]
print(result)

# Scalar-Vector product
u = [1,5,9]
v = [7,8,5]
alpha= 2
result = [alpha*sum(t) for t in zip(u,v)]
print(result)

#Matrix
mat_a = [[5,4],[2,5]]
mat_b = [[7,3],[5,7]]
result = [[sum(row)for row in zip(*m)]
          for m in zip(mat_a,mat_b)]
print(result)

#Matrix Transpose
matrix_a=[[1,2,3],[4,5,6]]
result = [[element for element in mt]for mt in zip(*matrix_a)]
print(result)