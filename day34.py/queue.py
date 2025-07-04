#create an endless loop where each element in the queue is a dictionary containing two properties : name and priority order
#higher priority  gets served first 
#in each iteration:
#program should print queue and user should have two options : add an element (with name and priority)
#                                                            :dequeue the queue to get element at front element
#HINT:priority queue uses min heap

from collections import deque
queue = deque()

while True:
    print("Current Queue:")
    sorted_queue = sorted(queue)
    for person in sorted_queue:
        print(sorted_queue)

    print("\nOptions:")
    print("1. Add an element")
    print("2. Dequeue (serve highest priority)")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter name: ")
        priority = int(input())
        queue.append(priority)
        print(name,priority)
    elif choice == "2":
        if not queue:
            print("Queue is empty")
        else:
            highest = max(queue)
            queue.remove(highest)
            print(name,priority)   
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again.")

