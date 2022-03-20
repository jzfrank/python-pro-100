from art import logo 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encript(text, shift):
    text = text.lower()
    encripted_text = ""
    for c in text:
        if c not in alphabet:
            encripted_text += c 
        else:
            shifted_char = alphabet[(ord(c) - ord('a') + shift) % 26]
            encripted_text += shifted_char
    return encripted_text

def decript(text, shit):
    return encript(text, -shift)

if __name__ == "__main__":
    print(logo)
    shoud_continue = True  
    while shoud_continue:
        while True:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            if direction == "encode" or direction == "decode":
                break 
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == "encode":
            encripted_text = encript(text, shift)
            print(f"The encoded text is {encripted_text}")
        elif direction == "decode":
            decripted_text = decript(text, shift)
            print(f"The decoded text is {decripted_text}")

        repeat = input("Do you want to restart the program? (y/n):\n")
        if repeat == 'n':
            print("Good bye")
            shoud_continue = False 



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 