sequence = [0, 1]

x = int(input("Enter the number of additions: "))

# Main program

index = 0

for i in range(x):
    sequence.append(sequence[index] + sequence[index + 1])
    index = index + 1

print(sequence)