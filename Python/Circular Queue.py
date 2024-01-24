# Circular Queue follows FIFO structure, use None to declare size of queue
queue = [None, None, None, None]
front_pointer = -1
rear_pointer = -1
error_message = "Unable to carryout the action."
def enqueue(enqueue_value):
    global rear_pointer
    rear_pointer = rear_pointer + 1
    if rear_pointer <= len(queue) - 1 and queue[rear_pointer] == None:
        queue[rear_pointer] = enqueue_value
        print(queue)
    else:
        rear_pointer = 0
        if queue[rear_pointer] == None:
            queue[rear_pointer] = enqueue_value
            print(queue)
        else:
            print(error_message)
def dequeue():
    global front_pointer
    front_pointer = front_pointer + 1
    if front_pointer <= len(queue) - 1:
        queue[front_pointer] = None
        print(queue)
    else:
        front_pointer = 0
        queue[front_pointer] = None
        print(queue)
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