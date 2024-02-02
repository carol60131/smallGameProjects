# Guess the Number, Try to guess the secret number based on hints.
# 猜數字(1~100)

import random


def guessNumber():
	while True:
		# 取得使用者輸入數字
		guess = input('> ')

		if guess.isdecimal():
			if  1 <= int(guess) <= 100:
				return int(guess)
		print('Please enter a number between 1 and 100')


def main():
	print('Guess the Number between 1 and 100')
	secretNumber = random.randint(1, 100)	

	# 遊戲迴圈
	for i in range(10):
		print('You have {} guesses left. Take a guess.'.format(10 - i))

		# 判斷數字大小，提供提示
		guess = guessNumber()
		if guess < secretNumber:
			print('You guess is too low.')
		if guess > secretNumber:
			print('You guess is to high.')
		if guess == secretNumber:
			break  # 猜中正確數字，離開迴圈

	# 判斷是否猜中，告知謎底
	if guess == secretNumber:
		print('You guessed Number!')
	else:
		print('Game Over! The Number is', secretNumber)


if __name__ == '__main__':
	main()
