alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(original_text, shift_amount,choice):
    output_text = ""
    if choice == "decode":
        shift_amount *= -1

    for char in original_text:
        if char not in alphabet:
            output_text += char
        else:
            new_index = alphabet.index(char) + shift_amount

            new_index %= len(alphabet)
            output_text += alphabet[new_index]

    print(f"Here is the {choice}d result: {output_text}")

redo = True
while redo:
    direction = input("Type 'encode' to encrype, tyep 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text,shift_amount=shift,choice=direction)

    choice = input("Do you want to do this again? Type 'y' if yes, or type 'n' for no: ").lower()

    if choice == "n":
        redo = False