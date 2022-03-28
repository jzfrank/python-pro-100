#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def replace_name(letter, name):
    salute = letter[0]
    # start = salute.find('[')
    # end = salute.find(']')
    # salute = salute[:start] + name + salute[end+1:]
    salute = salute.replace("[name]", name)
    return [salute] + letter[1:]

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.readlines()
    print(letter)

with open("Input/Names/invited_names.txt") as file:
    names = list(
        map(lambda x: x.strip(), file.readlines())
    )

for name in names:
    with open(f"Output/ReadyToSend/{name}.txt", "w") as file:
        letter_content = replace_name(letter, name)
        letter_content = "".join(letter_content)
        file.write(
            letter_content
        )

