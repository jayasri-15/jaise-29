# list=[3,2,1,4,2,0,1,2,0,12,0,7,0,0,0,4]
# number=0
# for i in range(len(list)):
#     list[i]=0
#     if list[i]==number:
#      print( list.append(0))            

list=[0,0,1,2,0,3,0,0,4]
index=0
for i in range(len(list)):
    if list[i]!=0:
        list[index]=list[i]
        index+=1
for i in range(index,len(list)):
    list[i]=0
    print(list)

