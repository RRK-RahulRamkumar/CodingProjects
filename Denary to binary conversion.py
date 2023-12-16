denary_number = int(input("Enter a denary number: "))
binary_weighting = [128, 64, 32, 16, 8, 4, 2, 1]
binary_list = []

if denary_number <= 255:
    for weighting in binary_weighting:
        if denary_number >= weighting:
            denary_number = denary_number - weighting
            binary_list.append(1)
        else:
            binary_list.append(0)
    print(binary_list)
else:
    print("Denary number is greater than 255")
