import operacions


def test_operacions():
    assert operacions.suma(3, 3) == 6
    assert operacions.suma(-3, 3) == 0
    assert operacions.suma(-3, -3) == -6


def test_operacions2():
    assert operacions.resta(3, 3) == 0
    assert operacions.resta(3, 2) == 1
    assert operacions.resta(3, 0) == 3
