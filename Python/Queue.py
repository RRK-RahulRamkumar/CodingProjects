# Currently, the queue can hold four values, to change the number of values it can hold, add or remove "None" to the queue
queue = [None, None, None, None]

front_pointer = 0
rear_pointer = 0

def enqueue(enqueue_value):
    global rear_pointer

    if rear_pointer < len(queue):
        queue[rear_pointer] = enqueue_value
        rear_pointer = rear_pointer + 1

        print(queue)
    else:
        print("Did not enqueue.")
    
def dequeue():
    global front_pointer

    if front_pointer < len(queue) and queue[front_pointer] != None:
        # Take the value stored in the position
        value = queue[front_pointer]

        queue[front_pointer] = None
        front_pointer = front_pointer + 1

        print(queue)
    else:
        print("Did not dequeue.")

while True:
    option = int(input("Enqueue(1) or dequeue(2): "))
    if option == 1:
        value = int(input("The number: "))
        enqueue(value)
    elif option == 2:
        dequeue()
    else:
        print("Incorrect operation.")



