import string
import random

# Getting password length
length = int(input("Enter password length: "))

characterList=""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		# Add letters to possible characters
		characterList += string.ascii_letters
	elif(choice == 2):
		
		# Add digits to possible characters
		characterList += string.digits
	elif(choice == 3):
		
		# Add special characters to possible characters
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	# Pick a random character 
	randomchar = random.choice(characterList)
	
	# append a random character to password
	password.append(randomchar)

# print password as a string
print("The random password is " + "".join(password))
