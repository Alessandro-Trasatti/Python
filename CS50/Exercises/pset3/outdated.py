# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order,
# formatted like 9/8/1636 or September 8, 1636. Then output that same date in YYYY-MM-DD format.
# If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days;
# no need to validate whether a month has 28, 29, 30, or 31 days.
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date, date_type = get_date()
    formatted_date = format_date(date, date_type)
    print(formatted_date)
    
    
def get_date() -> tuple[str, int]:
    '''
    Returns a tuple of string, integer, with
    string = the date;
    integer = 0 if the date is in the format is MM/DD/YYYY and 1 if it is formatted like September 8, 1636
    '''
    while True:
        date = input("Date: ").strip()
        if is_first_admissible_format(date):
            return date, 0
        else:
            return date, 1


def is_first_admissible_format(string: str) -> bool:
    try:
        month, day, year = string.split("/")
        return 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and int(year) >= 0
    except:
        return False

    
def is_second_admissible_format(string: str) -> bool:
    try:
        month, day, year = string.split(" ")
        if "," not in string:
            return False
        return month in months and 1 <= int(day[:-1]) <= 31 and int(year) >= 0
    except:
        return False
    

def format_date(date: str, date_type: int) -> str:
    if date_type == 0:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
    else:
        month, day, year = date.split(" ")
        month = months.index(month) + 1
        day = int(day[:-1])
        year = int(year)
        
    return f"{year}-{int(month):02}-{int(day):02}"
        
if __name__ == "__main__":
    main()
        