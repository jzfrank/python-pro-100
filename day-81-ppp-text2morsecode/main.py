from config import letters, morsecodes


class MorseCodeTranslator:
    def __init__(self):
        self.letter2morsecode = dict(zip(letters, morsecodes))
        self.morsecode2letter = dict(zip(morsecodes, letters))

    def encode(self, message):
        morsecode = ""
        for i, c in enumerate(message):
            c = c.lower()
            if c in self.letter2morsecode:
                morsecode += self.letter2morsecode[c]
                morsecode += " "
            else:
                raise Exception("Unknown character: " + c)
        morsecode = morsecode[:-1]
        return morsecode

    def decode(self, morsecode):
        message = ""
        for i, c in enumerate(morsecode.split(" ")):
            if c in self.morsecode2letter:
                message += self.morsecode2letter[c]
            else:
                raise Exception("Unknown morsecode: " + c)
        return message


if __name__ == "__main__":
    # demo
    translator = MorseCodeTranslator()
    message = "Hello World, how are you? I really like you!"
    morsecode = translator.encode(message)
    print(morsecode)
    message = translator.decode(morsecode)
    print(message)
    # GUI logic
    input("Welcome to Morse Code Translator! Press Enter to continue...\n")
    while True:
        task = input(
            "Do you want to encode or decode? (Press Enter to encode, type 'd' to decode, type 'q' to quit)\n")
        if task == "d":
            morsecode = input("Please enter the morsecode: ")
            message = translator.decode(morsecode)
            print("Decoded message: ", message)
        elif task == "q":
            break
        else:
            message = input("Please enter the message: ")
            morsecode = translator.encode(message)
            print("Encoded morsecode: ", morsecode)
