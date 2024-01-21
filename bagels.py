# Bagels, A deductive logic game where you must guess a number based on clues.

import random

NUM_DIGITS = 3  # 幾個數字
MAX_GUESSES = 10  # 猜測次數


# 提示
def getClues(guess, secretNum):
	if guess == secretNum:
		return 'You got it!'

	clues = []

	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clues.append('Fermi')
		elif guess[i] in secretNum:
			clues.append('Pico')

	if len(clues) == 0:
		return 'Bagels'
	else:
		clues.sort()
		return ' '.join(clues)


# 謎底
def getSecretNum():
	numbers = list('0123456789')
	random.shuffle(numbers)

	secretNum = ''
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])
	print('secretNum: ' + secretNum)
	return secretNum


def main():
	# 遊戲說明
	print('''Bagels, a deductive logic game.

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
	Pico         One digit is correct but in the wrong position.
	Fermi        One digit is correct and in the right position.
	Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

	# 遊戲迴圈
	while True:
		secretNum = getSecretNum()
		print('I have thought up a number.')
		print(' You have {} guesses to get it.'.format(MAX_GUESSES))

		numGuesses = 1
		while numGuesses <= MAX_GUESSES:

			guess = ''
			while len(guess) != NUM_DIGITS or not guess.isdecimal():
				print('Guess #{}: '.format(numGuesses))
				guess = input('> ')

			cluse = getClues(guess, secretNum)
			print(cluse)
			numGuesses += 1

			if guess == secretNum:
				break

			if numGuesses > MAX_GUESSES:
				print('You ran out of guesses.')
				print('The answer was {}'.format(secretNum))

		print('Do you want to play again? (yes of no)')
		if not input('> ').lower().startswith('y'):
			break

	print('Thanks for playing!')


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
	main()
