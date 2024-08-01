from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
#alphalet element = 25
End_game = False
def caesar(text, shift, direction):
    result = ""
    for letter in text:
        pos = alphabet.index(letter)
        if direction == "encode":
            new_pos = pos + shift
            if new_pos > 25: #if at pos 26, should equal to 'a' which is index 0, so minus -26 will get to index 0
                new_pos -= 26
        elif direction == "decode":
            new_pos = pos - shift
            if new_pos <0:
                new_pos += 25
        result += alphabet[new_pos]
    print(f"Here's the {direction}d result: {result}\n")

while End_game != True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    ask_repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if ask_repeat == "no":
        End_game = True
        print("Goodbye")