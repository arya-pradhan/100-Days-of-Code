alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrype, tyep 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for char in original_text:
        new_index =  alphabet.index(char) + shift_amount

        new_index %= len(alphabet)
        cipher_text += alphabet[new_index]

    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    decipher_text = ""
    for char in original_text:
        new_index = alphabet.index(char) - shift_amount

        new_index %= len(alphabet)
        decipher_text += alphabet[new_index]

    print(f"Here is the decoded result: {decipher_text}")

def caesar(original_text, shift_amount,choice):
    output_text = ""
    if choice == "decode":
        shift_amount *= -1

    for char in original_text:

        new_index = alphabet.index(char) + shift_amount

        new_index %= len(alphabet)
        output_text += alphabet[new_index]

    print(f"Here is the {choice}ed result: {output_text}")

caesar(original_text=text,shift_amount=shift,choice=direction)