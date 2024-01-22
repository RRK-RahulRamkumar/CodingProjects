# List must contain the same datatype

list = [1, 4, 3, 5]

index = 0

def code():
    global var1, var2, list, index
    var1, var2 = list[index], list[index + 1]
    list[index], list[index + 1] = var2, var1

for x in range(len(list)):
    try:
        for i in range(len(list)):
            if type(list[0]) == str:
                if list[index][0] > list[index + 1][0]:
                    code()
            elif type(list[0]) == int:
                if list[index] > list[index + 1]:
                    code()
            
            index = index + 1
            
    except IndexError as error:
        pass
    finally:
        index = 0

print(list)