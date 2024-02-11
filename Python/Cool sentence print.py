import time
sentence = "" # Add your sentence here
sentence_letter_index = 0
empty = ""

characters = " abcdefghijklmnopqrstuvwxyz"

for i in range(len(sentence)):
    for character in characters:
        if character != sentence[sentence_letter_index]:
            time.sleep(0.075)
            print(empty + character)
        else:
            print(empty + character)
            empty += character
            break
    
    sentence_letter_index += 1
