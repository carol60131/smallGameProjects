# Diamonds, Draws diamonds of various sizes.

"""
						   /\       /\
						  /  \     //\\
			/\     /\    /    \   ///\\\
		   /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
"""

def displayFilledDiamond(size):
	# top half
	for i in range(size):
		print(' ' * (size - i - 1), end='')  # Left space
		print('/' * (i + 1), end='')  # # Left side
		print('\\' * (i + 1))  # Right side

	# bottom half
	for i in range(size):
		print(' ' * i, end='')  # Left space.
		print('\\' * (size - i), end='')  # Left side
		print('/' * (size - i))  # Right side


def displayOutlineDiamond(size):
	
	# top half
	for i in range(size):
		print(' ' * (size - i - 1), end='')  # Left space
		print('/', end='')  # Left side
		print(' ' * (i * 2), end='')  # Interior space
		print('\\')  # Right side

	# bottom half
	for i in range(size):
		print(' ' * i, end='')  # Left space
		print('\\', end='')  # Left side
		print(' ' * ((size - i -1) * 2 ), end='')  # Interior space
		print('/')  # Right side


def main():

	print('Please enter the number of diamond size.')
	number = input('> ')
	
	if number != '' and number.isdigit():
		number = int(number)

		# Display diamonds
		for diamondSize in range(number, number + 1):
			displayOutlineDiamond(diamondSize)
			print()
			displayFilledDiamond(diamondSize)
			print()


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
	main()
