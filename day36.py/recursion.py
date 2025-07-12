# def fun(count,end):
#     #base condition
#     if count==end:
#         return
#     #operation
#     print(count)
#     count-=1
#     #rec fun call
#     fun(count,end)
#     #main
# fun(5,0)

#another method   
def jayasri(n):
    if n==0:
        return 
    jayasri(n-1)
    print(n)
jayasri(10)


    