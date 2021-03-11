# Author: Jeong Bin Lee
# Date: 2021.03.11
# Brief: Create a Python project of a Magic 8 Ball which is a toy used for fortune-telling or seeking advice.

#Allow the user to input their question.
#Show an in progress message.
#Allow the user to ask another question/advice or quit the game.


#import random to generate random numbers
import random

#create a list of answers
answer = ['As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.']


class Magic_8_Ball:
	def __init__(self, name):
		self.name = name;
	
	@staticmethod
	def randomNumber():
		return (int)(random.random()*(len(answer)-1)+ 0.5)
	
	@staticmethod
	def random_answer():
		print(answer[Magic_8_Ball.randomNumber()])

class Person(Magic_8_Ball):
	def __init__(self, name):
		super().__init__(name)
	
	@staticmethod
	def random_answer():
		print(answer[Magic_8_Ball.randomNumber()])


#introduction
print("Hi, I am Magic 8 Ball.")

#ask first question
question = input("Ask me a question: ")

#answer
Magic_8_Ball.random_answer()


#ask if the user has more questions.
repeat = input("Would you like to ask again [Y/n]? ")

while (repeat.lower() != 'n'):
	#account for invalid input
	if repeat.lower() != 'y':
		print("Invalid input")
	else:
		question = input("Ask me a question: ")
		Magic_8_Ball.random_answer()
	
	#ask if the user has more questions.
	repeat = input("Would you like to ask again [Y/n]? ")

#print a goodbye message
if (repeat.lower() == 'n'):
	print("Thanks or using magic 8 ball.")
exit()
