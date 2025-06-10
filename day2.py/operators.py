a=int(input("enter a number:"))
op=input("enter operator:")
result=a

while op !="=":
    a=int(input("enter next number:"))

    if op=="+":
        result +=a
    elif op=="-":
        result -=a
    elif op=="*":
        result *=a
    elif op=="/":
        result /=a
    else:
        print("enter valid operator to perform calculation")
    op=input("enter operator:")
print("result:" ,result)