from cipherart import art

print(art[0])
print(art[1])
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(original_text, shift_amount,encode_or_decode):
    message = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if  letter not in alphabet:
            message+=letter
        else:



            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            message += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {message}")


should_continue = True
while should_continue:
    user_input = input("Enter 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(original_text=text, shift_amount=shift, encode_or_decode=user_input)
    again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if again == "no":
        print("Goodbye")
        should_continue = False
