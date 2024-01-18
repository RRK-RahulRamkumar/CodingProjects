# Taking an input and appending it to user_inputs_store
user_inputs_store = []
user_input = input(f"Enter a binary code (1 byte): ")
user_inputs_store = user_inputs_store + (user_input.split())

# Convert each string in list to integer
converted_list = []
for a_string in user_inputs_store:
    converted_list.append(int(a_string))

# Calculating the denary value
weighting_index = 0
weighting_list = [128, 64, 32, 16, 8, 4, 2, 1]
total = 0

for a_bit in converted_list:
    if a_bit == 1:
        total = total + weighting_list[weighting_index]
        weighting_index = weighting_index + 1
    else:
        weighting_index = weighting_index + 1

print(f"The denary value is: {total}")
