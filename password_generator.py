import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '&','*', '@']

num_letters = 5
num_digits = 2
num_symbols = 1

letters_part = [random.choice(letters) for i in range(num_letters)]
digits_part = [random.choice(digits) for i in range(num_digits)]
symbols_part = [random.choice(symbols) for i in range(num_symbols)]

password_characters = letters_part + digits_part + symbols_part
random.shuffle(password_characters)
final = ''.join(password_characters)

# Displaying the generated password
print("Generated Password :- ",final)




