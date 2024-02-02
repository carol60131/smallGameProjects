# Make Calendar, Create monthly calendars, saved to a text file and fit for printing.
# 輸入年月製作月曆，印出並存檔成文字文件

import datetime

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wendesday', 'Thursday',	'Friday', 'Saturday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
	'September', 'October', 'Nobember', 'December']


def saveFile(year, month, calendarText):
	calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
	with open(calendarFilename, 'w') as fileObj:
		fileObj.write(calendarText)

	print('Saved to ' + calendarFilename)


def getCalendar(year, month):
	# 表頭年、月與週
	calendarText = (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
	calendarText += '     SUN        MON        TUE        WEN        THU        FRI        SAT\n'

	# 週分隔符號
	weekSeparator = ('+----------' * 7) + '+\n'
	blankRow = ('|          ' * 7) + '|\n'

	currentDate = datetime.date(year, month, 1)

	# 計算第一週星期日日期
	while currentDate.weekday() != 6:
		currentDate -= datetime.timedelta(days=1)

	# 循環該月中的週
	while True:
		calendarText += weekSeparator

		# 日期行
		dayNumberRow = ''
		for i in range(7):
			dayNumberLabel = str(currentDate.day).rjust(2)  # 對齊日期位置
			dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
			currentDate += datetime.timedelta(days=1)
		dayNumberRow += '|\n'
		calendarText += dayNumberRow

		# 空白行
		for i in range(3):
			calendarText += blankRow

		# 檢查月份
		if currentDate.month != month:
			break

	# 底部分隔符號
	calendarText += weekSeparator

	return calendarText

def main():

	print('Calendar Maker')

	# 取得使用者輸入年
	while True:
		print('Enter the year for the calender:')
		response = input('> ')

		if response.isdecimal() and int(response) > 0:
			year = int(response)
			break

		print('Please enter the numeric year, like 2024')
		continue

	# 取得使用者輸入月
	while True:
		print('Enter the month for the calender, 1-12:')
		response = input('> ')

		if response.isdecimal() and int(response) > 0:
			month = int(response)
			if 1 <= month <= 12: 
				break

		print('Please enter a number from 1 to 12.')
		continue

	# 製作月曆
	calendarText = getCalendar(year, month)
	print(calendarText)

	# 儲存
	saveFile(year, month, calendarText)


if __name__ == '__main__':
	main()
