arr=[3,2,1]
def generate(index,subset):
    if index==len(arr):
        print(subset)
        return
    #take
    subset.append(arr[index])
    generate(index+1,subset)
    #not take
    subset.pop()
    generate(index+1,subset)
generate(0,[])   


# string = "abc"
# def generate(index, substring):
#     if index == len(string):
#         print("".join(substring)) 
#         return
#     # take
#     substring.append(string[index])
#     generate(index + 1, substring)
#     # not take
#     substring.pop()
#     generate(index + 1, substring)

# generate(0, [])



