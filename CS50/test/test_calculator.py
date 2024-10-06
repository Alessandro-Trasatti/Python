import pytest
from Basics.calculator import square

def main():
    test_positive()
    test_negative()
    test_zero()
    test_str()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")

# Above there is way too much code because of the try/except, printng etc... pytest takes care of it while not
# making the code so verbose
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()