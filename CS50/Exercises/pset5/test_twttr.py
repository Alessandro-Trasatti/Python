# Aims at testing the shorten function in twttr.py from pset2.
import pytest
from pset2.twttr import shorten, shorten_re

def main():
    test_shorten()
    test_shorten_re()
    test_shorten_with_int()
    test_shorten_re_with_int()
    

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("AeIoU") == ""
    assert shorten("tWItTeR") == "tWtTR"

def test_shorten_with_int():
    with pytest.raises(TypeError):
        shorten(51)
    
def test_shorten_re():
    assert shorten_re("Twitter") == "Twttr"
    assert shorten_re("AeIoU") == ""
    assert shorten_re("tWItTeR") == "tWtTR"
    
def test_shorten_re_with_int():
    with pytest.raises(TypeError):
        shorten_re(51)
    
if __name__ == '__main__':
    main()