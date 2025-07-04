# a=[1,1,2,3,2]
# result=a[0]
# n=5
# for i in range(1,n-1):
#     result=result^a[i]
#     print(result)

#missing wrg
# arr=[1,0,3]
# list=range(0,len(arr)+1)
# result=arr[0]
# for i in range(0,len(arr)):
#     result =result^arr[i]
#     print(result)
# for i in list:
#     result=result^i


#missing number using X-OR
arr=[0,1,5,6,2,3]
n=len(arr)                       #TC=O(n)  SC=O(1)
missing=(n*(n+1)//2)-sum(arr)
print(missing)




