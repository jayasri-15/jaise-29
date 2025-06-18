# n=int(input())
# name_list=[]


# for i in range(n):
#     name=input()
#     name_list.append(name)
#     print(name_list)



user_list=[]
n=int(input())
for i in range (n):
    user_dict={}
    user_dict["name"]=input()
    user_dict["id"]=int(input())
    user_list.append(user_dict)
print(user_list)
keyword=input()
filterd_list=[]
for i in user_list:
    if keyword.lower() in i["name"].lower():
       filterd_list.append(i)
    print(filterd_list)
   
