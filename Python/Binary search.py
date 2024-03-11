def BinarySearch(numbers_list, find_number):
    data_valid = False

    if find_number >= numbers_list[0] and find_number <= numbers_list[-1]:
        if numbers_list:
            data_valid = True
        else:
            return f"The list is empty"
    else:
        return f"{find_number} is out of range of the list"
    

    if data_valid:
        while True:
            midpoint = numbers_list[len(numbers_list) // 2]
            if len(numbers_list) > 1:
                if find_number == midpoint:
                    return f"Found {midpoint}"
                    
                elif find_number < midpoint:
                    numbers_list = numbers_list[0:len(numbers_list) // 2]
                else:
                    numbers_list = numbers_list[(len(numbers_list) // 2) + 1:]
            else:
                return f"Could not find {find_number}"


numbers_list = []
find_number = 0
print(BinarySearch(numbers_list, find_number))