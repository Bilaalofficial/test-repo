from app import add, hello

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_hello():
    assert hello("Bilaal") == "Hello, Bilaal!"
