# A program to create files based on two inputs,
#   file's name, and the number of files to be created

file_name_input = input("File name: ")
file_create_input = int(input("How many files to create: "))

def create_files(file_name, create_count):
    file_number = 1

    for i in range(create_count):
        new_file_name = f"{file_name} {file_number}"

        with open(f"Project 1/TextFiles/{new_file_name}", "w") as file:
            file.write("Hello world")

        file_number = file_number + 1

create_files(file_name_input, file_create_input)
