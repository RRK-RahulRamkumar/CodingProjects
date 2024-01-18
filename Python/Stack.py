# Currently, the stack can hold four values, to change the number of values it can hold, add or remove "None" to the stack
stack = [None, None, None, None]
top_pointer = -1
 
def push(push_value):
    global top_pointer
 
    if None not in stack:
        print("Stack is full")
    else:
        top_pointer = top_pointer + 1
        stack[top_pointer] = push_value
 
    print(stack)
 
def pop():
    global top_pointer
 
    if top_pointer < 0:
        print("Stack is empty!")
    else:
        stack[top_pointer] = None
        top_pointer = top_pointer - 1
 
    print(stack)
 
