arr=[1,2,3,99,-8]
n=5
# k=2
# for i in range(0,n-1):
#     if(i)>(i+1):
#         k=i
# for i in range(0,n-1):
#     arr[(i+(n-k))%n]
#     list[i]
# for i in range(0,n-1):
#     if (i)<(i+1):
#         print(True)
#         break
#     else:
#         print(False)

for i in range(0,n-1):
    for j in range(0,i+1):
        if arr[i]<arr[i+1]:
            print(True)
        else:
            print(False)            


            

