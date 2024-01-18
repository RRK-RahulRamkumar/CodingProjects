# Currently, the queue can hold four values, to change the number of values it can hold, add or remove "None" to the queue
queue = [None, None, None, None]
rear_pointer = -1

def enqueue(enqueue_value):
    global rear_pointer
    if None not in queue:
        print("Queue is full")
    else:
        rear_pointer = rear_pointer + 1
        queue[rear_pointer] = enqueue_value
    print(queue)

def dequeue():
    global rear_pointer
    if rear_pointer < 0:
        print("Queue is empty!")
    else:
        del queue[0]
        rear_pointer = rear_pointer - 1
        queue.append(None)
    print(queue)

while True:
    ask_option = int(input("Do you want to enqueue(1) or dequeue(2): "))
    if ask_option == 1:
        enqueue_value = int(input("Enter a value to enqueue: "))
        enqueue(enqueue_value)
    elif ask_option == 2:
        dequeue()
    else:
        print("Incorrect input")
