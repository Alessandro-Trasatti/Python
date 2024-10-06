from pset2.plates import is_valid
from random import randint

def main():
    test_starts_with_letters()
    is_correct_lenght()
    ends_with_numbers_if_present()
    has_no_special_characters()
    
    
def test_starts_with_letters():
    assert is_valid("AAA222") == True
    assert is_valid("1AA222") == False
    
def is_correct_lenght():
    short_plate = "AA"
    long_plate = "AAA222"
    
    assert is_valid(short_plate) == True
    assert is_valid(long_plate) == False
    
    assert is_valid("B" + long_plate) == False
    assert is_valid(short_plate[0]) == False

def ends_with_numbers_if_present():
    assert is_valid("AAA2A2") == False
    
    
def has_no_special_characters():
    assert is_valid("AA#2A2") == False
    assert is_valid("A*A2A@") == False    
    
if __name__ == '__main__':
    main()