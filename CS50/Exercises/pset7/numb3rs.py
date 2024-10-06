# In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns
# True or False, respectively, if that input is a valid IPv4 address or not.

# An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet,
# akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#.
# But each # should be a number between 0 and 255, inclusive. 

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    # First check if the ip address is in the format #.#.#.#, with # a number...
    reg_ex = r"^(\d{1,3}\.){3}\d{1,3}$"
    match = re.fullmatch(reg_ex, ip)
    if match: 
        # ... then check that each number is between 0 and 255, included
        ip_numbers = ip.split(".")
        for num in ip_numbers:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()