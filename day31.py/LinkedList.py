# head=> tail 
#  <<<single linked list>>>
class Node:
    def __init__(self , value=0 , nextNode=None):
        self.val=value
        self.next=nextNode
# item1=Node(100)
# item2=Node(200)
# item3=Node(300)
# item4=Node(400)
# item5=Node(500)

# item1.next=item2
# item2.next=item3
# item3.next=item4
# item4.next=item5           5th line to 14th line another optional

head=Node(100)
head.next=Node(200)
head.next.next=Node(300)
head.next.next.next=Node(400)
head.next.next.next.next=Node(500)

result=[]
# current=head  
# # length=0                         #current=head 
# while current!=None:                   #current=current.next  (next value of current  )  nolde1=>node2=>node3
#     print(current.val,end=" ")         
#     current=current.next
    # length=+1
    # print(length)

#inserting another element to last
# current=head
# while current.next!=None:
#     current=current.next
#     current.next=Node(int(input()))
#     print(current.next)

#insserting middle to linkedlist
position =3
newNode=250
current=head
while current!=None:
    node_position+=1
    if node_position==position-1:
        temp=current.next
        current.next=newNode
        newNode.next=temp
    current=current.next
print(head)



