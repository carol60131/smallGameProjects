# Print a multiplication Table
# 印出 乘法表

def main():
	# 列 Column
	print('  |  1   2   3   4   5   6   7   8   9  10  11  12')
	print('--+-----------------------------------------------')

	# 行 row
	for number1 in range(1, 13):
		print(str(number1).rjust(2), end='')
		print('|', end='')

		# 逐行印出乘積
		for number2 in range (1, 13):
			print(str(number1 * number2).rjust(3), end=' ')
		print()


if __name__ == '__main__':
	main()
