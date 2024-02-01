# Bitmap Message, Displays a text message according to the provided bitmap image.
import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

def loopBitmap(message):

	# Loop over each line in the bitmap
	for line in bitmap.splitlines():
	
		# Loop over each character in the line:
		for i, bit in enumerate(line):
			if bit == ' ':
				print(' ', end='')  # Print an empty space
			else:
				# Print a character from the message
				print(message[i % len(message)], end='')
		
		print()  # Print a newline.


def main():
	print('Enter the message to display with the bitmap.')
	message = input('> ')
	
	if message == '':
		sys.exit()

	loopBitmap(message)


if __name__ == '__main__':
	main()
