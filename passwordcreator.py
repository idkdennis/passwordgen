import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

characters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
    "'", '"', ',', '<', '.', '>', '/', '?', '|', '\\'
]
password = []
Pass_num =int(input("how many numbers do you want in your password: "))
pass_letters = int(input("how many lettrs do you want in your password: "))
Pass_symbols = int(input("how many symbols do you want in your password: "))

for num in range (0, Pass_num ):
	password += random.choice(numbers)	

for char in range (0, pass_letters ):
	password += random.choice(characters)
	
for sym in range (0, Pass_symbols ):
	password += random.choice(symbols)
	
print(password)

random.shuffle(password)
print(password)
#print(*password)

password_string=""

for pas in password:
	password_string+= pas
	
print(f"Bro This Is Your Strong Asf Password: {password_string}")