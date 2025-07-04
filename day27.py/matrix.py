mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[9,8,7],[6,5,4],[3,2,1]]
row=3
col=3
result=[]                               #addition
for i in range(0,row):
    rowList=[]
    for j in range(0,col):
        rowList.append(mat1[i][j]+mat2[i][j])
    result.append(rowList)
print(result)