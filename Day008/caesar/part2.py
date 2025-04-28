# art = [r'''
#  cccc    aaaaa   eeeee  sssss   aaaaa  rrrrr
# c        a   a   e      s       a   a  r   r
# c        aaaaa   eeee   sssss   aaaaa  rrrrr
# c        a   a   e          s   a   a  r  r
#  cccc    a   a   eeeee  sssss   a   a  r   r
# ''',
# r'''
#  cccc   iii  pppp   h   h  eeeee  rrrrr
# c        i   p   p  h   h  e      r   r
# c        i   pppp   hhh   eeee   rrrrr
# c        i   p      h   h  e      r  r
#  cccc   iii  p      h   h  eeeee  r   r
# '''
# ]
#
# print(art[0])
# print(art[1])
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_input= input("Enter 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text= input("Type your message:\n").lower()

shift= int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text=""

    for letter in original_text:
        shifted_position=alphabet.index(letter)+shift_amount

        shifted_position %= len(alphabet)
        cipher_text+= alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    message=""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        message+=alphabet[shifted_position]

    print(f"Here is the decoded result: {message}")

decrypt(original_text=text, shift_amount=shift)

# encrypt(original_text=text, shift_amount=shift)








