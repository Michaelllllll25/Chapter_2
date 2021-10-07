from main import add

def test_add():
    assert add(5, 6) == 11
    assert add(0, 0) == 0
    assert add(-5, -3) == -8
