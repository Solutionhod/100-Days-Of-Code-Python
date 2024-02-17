PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as file1:
    names = file1.readlines()
        
with open("Input/Letters/starting_letter.txt") as file2:
    contents = file2.read()
    for name in names:
        stripped_name = name.strip()
        letter = contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_to_{stripped_name}", "w") as file3:
            file3.write(letter)
            
            