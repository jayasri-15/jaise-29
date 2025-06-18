def slug_generator(ppp:str):

    ppp=ppp.lower()
    ppp=list(ppp)
    result=""
    for i in range(0,len(ppp)):
        if ppp[i].isalnum():
            result+=ppp[i]
        elif ppp[i]==" ":
            result +="-"
        else:
            continue

    return result

title=input()

result=slug_generator(title)

print(result)