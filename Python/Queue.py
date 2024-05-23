# Queue follows FIFO structure, use None to declare size of queue
queue = [None, None, None, None]
front_pointer = -1
rear_pointer = -1
def enqueue(enqueue_value):
    global rear_pointer
    
    if rear_pointer < len(queue) - 1:
        rear_pointer = rear_pointer + 1
        queue[rear_pointer] = enqueue_value
        print(queue)
    else:
        print("Queue is full.")

def dequeue():
    global front_pointer
    
    if front_pointer < len(queue) - 1:
        front_pointer = front_pointer + 1
        queue[front_pointer] = None
        print(queue)
    else:
        print("Queue is empty")

# Extra code
while True:
    option = int(input("Enqueue(1) or dequeue(2): "))
    if option == 1:
        value = input("Enter a value to enqueue: ")
        enqueue(value)
    elif option == 2:
        dequeue()
    else:
        print("Incorrect option.")
