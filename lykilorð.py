import string
import random


## characters to generate password from
alphabets = list('HeiðarIngiRagnheiðurSunnaElísabetLára')
digits = list("200420192022")
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Hvað er lykilorðið langt?: "))

	## number of character types
	alphabets_count = int(input("Fjöldi bókstafa: "))
	digits_count = int(input("Fjöldi tölustafa: "))
	special_characters_count = int(input("fjöldi tákna: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	## check the total length with characters sum count
	## print not valid if the sum is greater than length
	if characters_count > length:
		print("Fjöldinn sem þú hefur slegið inn er lengri en lykilorðið sem þú ætlaðir að gera")
		return


	## initializing the password
	password = []
	
	## picking random alphabets
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	## picking random digits
	for i in range(digits_count):
		password.append(random.choice(digits))


	## picking random alphabets
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	## if the total characters count is less than the password length
	## add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))



## invoking the function
generate_random_password()