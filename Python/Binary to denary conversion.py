bits_list = []
user_input = input("Enter binary code (1 Byte): ")

for bit in user_input:
    bits_list.append(int(bit))

weighting_list = [128, 64, 32, 16, 8, 4, 2, 1]
weighting_index = 0
total = 0

for bit in bits_list:
    if bit == 1:
        total = total + weighting_list[weighting_index]
    weighting_index = weighting_index + 1
    
print(f"The denary value is: {total}")