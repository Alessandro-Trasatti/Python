from Basics.hello import hello

def test_default():
    assert hello() == "Hello, world"
    
def test_argument():
    assert hello("Alessandro") == "Hello, Alessandro"
    