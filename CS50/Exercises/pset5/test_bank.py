import pytest
from pset1.bank import prize

def main():
    test_prize()
    test_prize_invalid_greeting()
    
def test_prize():
    assert prize("hello") == 0
    assert prize("h") == 20
    assert prize("toto") == 100
    
def test_prize_invalid_greeting():
    with pytest.raises(TypeError):
        prize(0)
        
if __name__ == "__main__":
    main()