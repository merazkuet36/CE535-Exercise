from Ex11 import login


def test_n_type():
    n = 1234
    pin = '1234'
    assert login(n, pin) == False


def test_pin_type():
    n = '1234'
    pin = 1234
    assert login(n, pin) == False


def test_pin_length():
    n = '1234'
    pin = '12345'
    assert login(n, pin) == False


def test_login_success():
    n = '63'
    pin = '9608'
    assert login(n, pin) == True


def test_login_failure():
    n = '1234'
    pin = '12345'
    assert login(n, pin) == False


def test_login_multiple_pins():
    n = '156'
    pin_1 = '1120'
    pin_2 = '1125'
    assert login(n, pin_1) == True
    assert login(n, pin_2) == True


def test_docstring():
    assert login.__doc__ is not None
    assert len(login.__doc__) > 10