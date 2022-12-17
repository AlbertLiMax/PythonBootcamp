#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def process_invite_names():
    with open("Input/Names/invited_names.txt") as file:
        names = file.read().splitlines()

    return names
def prepare_mails(names):
    for name in names:
        with open("Input/Letters/starting_letter.txt") as file_r:
            letter = file_r.read().replace("[name]", name)
            with open(f"Output/ReadyToSend/letter_for_{name}", "w") as file_w:
                file_w.write(letter)

invited_names = process_invite_names()
prepare_mails(invited_names)