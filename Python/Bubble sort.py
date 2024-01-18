# Bubble sort for numbers
# To bubble sort for words, line 11 list[index][0] > list[index + 1][0]:
# List must contain the same datatype

list = [1, 3, 2, 4, 7, 6]

index = 0

for x in range(len(list)):
    try:
        for i in range(len(list)):
            if list[index] > list[index + 1]:
                var1, var2 = list[index], list[index + 1]
                list[index], list[index + 1] = var2, var1
            
            index = index + 1
            
    except IndexError as error:
        pass
    finally:
        index = 0

print(list)
