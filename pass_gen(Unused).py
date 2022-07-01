import random
import string
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = 8

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	return "".join(password)



## invoking the function
generate_random_password()