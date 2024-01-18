# Used to create a file for each section in the Notes text file
# For personal use, saved it on github

starting_title = ""
notes_path = ""
folder_path = ""
section_start = ""
file_extension = ""

with open(f"{notes_path}", "r") as Notes:
    current_file = f"{folder_path}/{starting_title}{file_extension}"

    for line in Notes:
        if "#" in line:
            edited_title = line.replace(section_start, "").strip().capitalize()
            current_file = f"{folder_path}/{edited_title}{file_extension}"
        else:
            with open(current_file, "a") as file:
                file.write(line)