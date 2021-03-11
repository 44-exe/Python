# Author: Jeong Bin Lee
# Date: 2021.03.11
# Brief: Create a python program to test the persons typing skills, and measure the score and error.

import time
import random

#list of random words
word = ['been', 'also', 'without', 'something', 'them', 'he', 'would', 'again', 'right', 'first', 'away', 'boy','you', 'this', 'let', 'there', 'new', 'high', 'car', 'life', 'name', 'day', 'she', 'small', 'while', 'animal', 'show', 'example', 'children', 'paper', 'large', 'state', 'who', 'it', 'do']

#this function selects a random word from the list
def random_word():
	rand_word = word[(int)(random.random() * (len(word) - 1) + 0.5)]
	print(rand_word)
	return rand_word


#the main function
def main():
	#ask the user to start the typing test
	start = input("Start [Y/n]? ")

	while start.lower() != 'n':
		#check for any invalid inputs
		if start.lower() != 'y':
			print("Invalid input")
		else:
			#initial variables
			init_time = time.time()
			count = 0
			error = 0
			#run the test for 60sec
			while(time.time() - init_time < 60):
				#output a random word
				rand_word = random_word()
				#read what the user typed
				user = input()
				#compare the typed word and produced word
				if user == rand_word:
					count+=1 #record the score
				elif user != rand_word:
					error+=1 #record the error
			print()
			print("END OF TIME")
			print(f"Your score: {count}")
			print(f"Your error: {error}")

		start = input("Try again [Y/n]? ")
	
#run main
main()

print("Exiting program")

exit()


