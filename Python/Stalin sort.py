list = [2, 4, 1, 5, 3, 6]

def StalinSort(list):
    current_number = 0

    for number in list:
        if number > current_number:
            current_number = number
        else:
            list.remove(number)
    
    return list

print(f"""
Unsorted list: {list}
Sorted list: {StalinSort(list)}
""")