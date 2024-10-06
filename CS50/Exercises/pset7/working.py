# In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below
# and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
# Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
# Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM

# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
# (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem;
# someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

from re import fullmatch

PATTERN = r"^(\d{1,2})(\:\d{2})? (AM|PM) to (\d{1,2})(\:\d{2})? (AM|PM)$"

def main():
    try:
        print(convert(input("Hours: ")).strip())
    except ValueError as e:
        print(e)

def convert(s: str) -> str:
    validate(s)
    match = fullmatch(PATTERN, s)

    # First time conversion
    hour1 = int(match.group(1))
    minute1 = match.group(2)[1:] if match.group(2) else "00"
    period1 = match.group(3)

    if period1 == "PM" and hour1 != 12:
        hour1 += 12
    elif period1 == "AM" and hour1 == 12:
        hour1 = 0

    # Second time conversion
    hour2 = int(match.group(4))
    minute2 = match.group(5)[1:] if match.group(5) else "00"
    period2 = match.group(6)

    if period2 == "PM" and hour2 != 12:
        hour2 += 12
    elif period2 == "AM" and hour2 == 12:
        hour2 = 0

    # Return the formatted 24-hour time
    return f"{hour1:02}:{minute1} to {hour2:02}:{minute2}"

def validate(s: str) -> None:
    match = fullmatch(PATTERN, s)
    if not match:
        raise ValueError("Invalid time format.")
    
    minute1 = int(match.group(2)[1:]) if match.group(2) else 0
    minute2 = int(match.group(5)[1:]) if match.group(5) else 0

    if not (0 <= minute1 <= 59 and 0 <= minute2 <= 59):
        raise ValueError(f"Invalid minutes: {minute1}, {minute2}")

if __name__ == '__main__':
    main()