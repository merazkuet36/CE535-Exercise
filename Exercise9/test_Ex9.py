import Ex9
import math


def f1(x):
    return x**4


def g1(x):
    return x**5/5.0


def f2(x):
    return x**3


def g2(x):
    return x**4/4.0


def f3(x):
    return 1.0 / x


def g3(x):
    return math.log(x)


def f4(x):
    return math.exp(x)


def g4(x):
    return math.exp(x)


def f5(x):
    return math.sin(x)


def g5(x):
    return -math.cos(x)


def f6(x):
    return 1.0


def g6(x):
    return x


def f7(x, h, j, k, l, m):
    return x**h + (j+k)*x - l*math.sin(m*x)


def g7(x, h, j, k, l, m):
    return x**(h+1)/(h+1) + j + k + l*math.cos(m*x) / m


def test_a_int():
    """Test 'a' for int"""
    try:
        Sn = Ex9.simpson_rule(f1, 1, 2.0, 10)
        if Sn != 0:
            print(
                'function should check if "a" is a float')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_a_float():
    """Test 'a' for float"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, 2.0, 10)
        if Sn == 0:
            print(
                'function wrongly check if "a" is a float'
            )
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_a_bool():
    """Test 'a' for bool"""
    try:
        Sn = Ex9.simpson_rule(f1, True, 2.0, 10)
        if Sn != 0:
            print(
                'function should check if "a" is a float')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_a_other_type():
    """Test 'a' for other type"""
    try:
        Sn = Ex9.simpson_rule(f1, [], 2.0, 10)
        if Sn != 0:
            print(
                'function should check if "a" is a float')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_b_int():
    """Test 'b' for int"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, 2, 10)
        if Sn != 0:
            print(
                'function should check if "b" is a float')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_b_float():
    """Test 'b' for float"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, 2.0, 10)
        if Sn == 0:
            print(
                'function wrongly check if "b" is a float'
            )
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_b_bool():
    """Test 'b' for bool"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, True, 10)
        if Sn != 0:
            print(
                'function should check if "b" is a float')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_b_other_type():
    """Test 'b' for other type"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, [], 10)
        if Sn != 0:
            print(
                'function should check if "b" is a float')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_n_int():
    """Test 'n' for int"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, 2.0, 10)
        if Sn == 0:
            print(
                'function wrongly check if "n" is an int')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_n_float():
    """Test 'n' for float"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, 2.0, 10.0)
        if Sn != 0:
            print(
                'function should check if "n" is an int'
            )
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_n_bool():
    """Test 'n' for bool"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, 2.0, True)
        if Sn != 0:
            print(
                'function should check if "n" is an int')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_n_other_type():
    """Test 'n' for other type"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, 2.0, [])
        if Sn != 0:
            print(
                'function should check if "n" is an int')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_a_less_than_b():
    """Test 'a< b'"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, 2.0, 10)
        if Sn == 0:
            print(
                'function wrongly check if "a < b"')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False
    try:
        Sn = Ex9.simpson_rule(f1, 2.0, 1.0, 10)
        if Sn != 0:
            print(
                'function should check if "a < b"')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_n_even():
    """Test 'n' is positive even number"""
    try:
        Sn = Ex9.simpson_rule(f1, 1.0, 2.0, 10)
        if Sn == 0:
            print(
                'function wrongly check if "n" is even number')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False
    try:
        Sn = Ex9.simpson_rule(f1, 2.0, 1.0, 9)
        if Sn != 0:
            print(
                'function should check if "n" is even number')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False
    try:
        Sn = Ex9.simpson_rule(f1, 2.0, 1.0, -10)
        if Sn != 0:
            print(
                'function should check if "n" is positive')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def test_docstring():
    """Test docstring"""
    try:
        if Ex9.simpson_rule.__doc__ is None:
            print(
                'function should have docstring')
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False
    try:
        if len(Ex9.simpson_rule.__doc__) == 0:
            print(
                "function's docstring should have contents")
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False


def run_fx(fx, gx, a, b, tol):
    exactInteg = gx(b) - gx(a)
    flag_convergence = False
    prev_error = 1e6
    for i in range(8):
        n = 2**(i+1)
        numericInteg = Ex9.simpson_rule(fx, a, b, n)
        error = abs(numericInteg-exactInteg)
        if error < prev_error or error < tol:
            flag_convergence = True
        prev_error = error

    if prev_error < tol:
        flag_convergence = True
    else:
        flag_convergence = False
    return flag_convergence


# for fx, gx, name, a, b in [
#         (f1, g1, 'x^4', 2.5, 6.75),
#         (f2, g2, 'x^5', 1.3, 10.4),
#         (f3, g3, '1/x', 0.018, 3.49),
#         (f4, g4, 'e(x)', 1.5, 6.5),
#         (f5, g5, 'sin(x)', 0.1*math.pi, 0.9*math.pi)
#     ]:

def test_x_power_4():
    assert run_fx(f1, g1, 2.5, 6.75, 1e-7)


def test_x_power_5():
    assert run_fx(f2, g2, 1.3, 10.4, 1e-10)


def test_1_over_x():
    assert run_fx(f3, g3, 0.018, 3.49, 1e-2)


def test_e_x():
    assert run_fx(f4, g4, 1.5, 6.5, 1e-6)


def test_sin_x():
    assert run_fx(f5, g5, 0.1*math.pi, 0.9*math.pi, 1e-9)


def test_default_arguments():
    """Test default arguments"""
    try:
        Sn = Ex9.simpson_rule(f6)
        if Sn != 1.0:
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False

    print(f'Passed to test default arguments')


def test_arbitrary_arguments():
    """Test arbitrary arguments"""
    try:
        Sn = Ex9.simpson_rule(f7, 2.0, 3.0, 20, 5, 2.0, m=1.5, l=10.0, k=1)
        if abs(Sn - 123.52798931153073) > 1e-6:
            assert False
    except Exception as e:
        print(f'Errors {e} in simpson_rule function')
        assert False