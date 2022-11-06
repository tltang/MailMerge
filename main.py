#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as import_content:
    cContent = import_content.read()

with open("Input/Names/invited_names.txt") as import_name:
    cName = import_name.readlines()

for name in cName:
    name1 = name.strip()
    cContent1 = cContent.replace("[name]", name1)
    with open(f"Output/ReadyToSend/{name1}.txt", mode="w") as final_letters:
        final_letters.write(cContent1)

