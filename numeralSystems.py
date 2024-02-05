# Numeral System Counters, Shows equivalent numbers in decimal, hexadecimal, and binary.
# 十進位數值轉換二進位、八進位、十六進位

def main():
	print('Enter a number for the numeral systems:')

	# 取得使用者輸入數字
	while True:
		decNumber = input('> ')
		if decNumber.isdecimal() and int(decNumber) >= 0:
			decNumber = int(decNumber)
			break

		print('Please enter a number.')
		continue

	# 計算不同進位數值
	binNumber = bin(decNumber)[2:].upper()
	octNumber = oct(decNumber)[2:]
	hexNumber = hex(decNumber)[2:]

	print('Decimal: ', decNumber)
	print('Bin: ', binNumber)
	print('Oct: ', octNumber)
	print('Hex: ', hexNumber)


if __name__ == '__main__':
	main()