def main():
	calendar = [["30.3.2007"], ["1.6.1995"]]

	user_date = get_user_date()
	answer = check_date(calendar, user_date)
	print(answer)

def get_user_date():
	try:

		full_date = ""
		YEAR_TODAY = 2022


		day = int(input("Day is: "))
		while day > 31 or day < 1:
			day = int(input("True Day is: "))

		month = int(input("Month is: "))
		while month > 12 or month < 1:
			month = int(input("True Month is: "))

		year = int(input("Year is: "))
		while year > YEAR_TODAY or year < 1820:
			year = int(input("True Year is: "))

		full_date = f"{day}.{month}.{year}"

		return full_date

	except ValueError:
		print("You must write a number")
		get_user_date()


def check_date(cal, user_date):
	for date_time in cal:
		if "".join(date_time) == user_date:
			return "Yes, we have this date"
		else:
			return "No, we have not this date"

main()