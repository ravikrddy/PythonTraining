mat=[[1,2,3],[4,5,6],[7,8,9]]
print(mat[1][1])

mat[1][1]='x' #update
mat[2].append(10) #add
mat[0].pop(1) #delete
mat.insert(2,[22,33,44]) #insert
print(mat)

for row in mat:
    for col in row:
        print(col,end='\t')
    print()