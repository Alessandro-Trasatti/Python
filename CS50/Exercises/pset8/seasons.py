# In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format
# and then prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals,
# just like the song from Rent, without any and between words.
# Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight
# (i.e., 00:00:00) on that date. And assume that the current time is also midnight.
# In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date.
# Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

# You’re welcome to import other (built-in) libraries, or any that are specified in the below hints.
# Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.

from datetime import date
from sys import exit
from re import fullmatch

def main():
    birth_date: date = get_date()
    today: date = date.today()

    if birth_date > today:
        print("Your birth date should be before today!")
        exit()

    age_in_minutes = int((today - birth_date).total_seconds() / 60)
    
    print(f"You are {age_in_minutes} minutes old.")

def get_date() -> date:
    birth_date = input("Your birth day (YYYY-MM-DD): ").strip()
    match = fullmatch(r"^(\d{4})-(\d{2})-(\d{2})$", birth_date)
    if match:
        try:
            return date.fromisoformat(birth_date)
        except ValueError as e:
            print(f"Invalid birth date inserted. Date should be in the format 'YYYY-MM-DD'.\n{e}")
            exit()
    print("Invalid birth date inserted. Date should be in the format 'YYYY-MM-DD'.")
    exit()

if __name__ == "__main__":
    main()