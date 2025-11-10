import Ex12
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


def test_n_even_SimpsonRule():
    """Test 'n' is positive even number for SimpsonRule"""
    try:
        Sn = Ex12.SimpsonRule(1.0, 2.0, 9)
        Sn.integrate(f1)
        if Sn.Sn != 0:
            print(
                'function should check if "n" is even number')
            assert False
    except:
        print(f'Errors in SimpsonRule function')
        assert False
    try:
        Sn = Ex12.SimpsonRule(1.0, 2.0, -10)
        Sn.integrate(f1)
        if Sn.Sn == 0:
            print(
                'function should flip the sign if "n" is negative')
            assert False
    except:
        print(f'Errors in SimpsonRule function')
        assert False


def test_docstring_SimpsonRule():
    """Test docstring"""
    try:
        if Ex12.SimpsonRule.__doc__ is None:
            print(
                'function should have docstring')
            assert False
    except:
        print(f'Errors in SimpsonRule function')
        assert False
    try:
        if len(Ex12.SimpsonRule.__doc__) == 0:
            print(
                "function's docstring should have contents")
            assert False
    except:
        print(f'Errors in SimpsonRule function')
        assert False


def test_docstring_TrapezoidRule():
    """Test docstring"""
    try:
        if Ex12.TrapezoidRule.__doc__ is None:
            print(
                'function should have docstring')
            assert False
    except:
        print(f'Errors in TrapezoidRule function')
        assert False


def test_docstring_BaseClass():
    """Test docstring"""
    try:
        if Ex12.NumericalIntegration.__doc__ is None:
            print(
                'function should have docstring')
            assert False
    except:
        print(f'Errors in NumericalIntegration function')
        assert False


def test_docstring_MidpointRule():
    """Test docstring"""
    try:
        if Ex12.MidpointRule.__doc__ is None:
            print(
                'function should have docstring')
            assert False
    except:
        print(f'Errors in MidpointRule function')
        assert False


def run_fx(fx, gx, a, b, tol, rule, function_name):
    exactInteg = gx(b) - gx(a)
    flag_convergence = False
    prev_error = 1e6
    for i in range(10):
        n = 2**(i+1)
        if rule == 'SimpsonRule':
            numericIntegObj = Ex12.SimpsonRule(a, b, n)
        elif rule == 'TrapezoidRule':
            numericIntegObj = Ex12.TrapezoidRule(a, b, n)
        elif rule == 'MidpointRule':
            numericIntegObj = Ex12.MidpointRule(a, b, n)
        else:
            numericIntegObj = Ex12.NumericalIntegration(a, b, n)
        numericIntegObj.integrate(fx)
        numericInteg = numericIntegObj.Sn
        error = abs(numericInteg-exactInteg)
        print(f'{function_name} -- {rule} -- n: {n}, numericInteg: {numericInteg}, exactInteg: {exactInteg}, error: {error}')
        if error < prev_error or error < tol:
            flag_convergence = True
        else:
            flag_convergence = False
        prev_error = error

    if prev_error < tol:
        flag_convergence = True
    else:
        flag_convergence = False
    return flag_convergence


def test_x_power_4_SimpsonRule():
    assert run_fx(f1, g1, 2.5, 6.75, 1e-7, 'SimpsonRule', 'x^4')


def test_x_power_5_SimpsonRule():
    assert run_fx(f2, g2, 1.3, 10.4, 1e-10, 'SimpsonRule', 'x^5')


def test_1_over_x_SimpsonRule():
    assert run_fx(f3, g3, 0.018, 3.49, 1e-2, 'SimpsonRule', '1/x')


def test_e_x_SimpsonRule():
    assert run_fx(f4, g4, 1.5, 6.5, 1e-6, 'SimpsonRule', 'e^x')


def test_sin_x_SimpsonRule():
    assert run_fx(f5, g5, 0.1*math.pi, 0.9*math.pi,
                  1e-9, 'SimpsonRule', 'sin(x)')


def test_default_arguments_SimpsonRule():
    """Test default arguments"""
    try:
        Sn = Ex12.SimpsonRule()
        Sn.integrate(f6)
        print(
            f'f(x)=1 -- SimpsonRule -- n: {Sn.n}, numericInteg: {Sn.Sn}, exactInteg: 1.0, error: {abs(Sn.Sn - 1.0)}')
        if Sn.Sn != 1.0:
            assert False
    except:
        print(f'Errors in simpson_rule function')
        assert False

    print(f'Passed to test default arguments_SimpsonRule')


def test_arbitrary_arguments_SimpsonRule():
    """Test arbitrary arguments"""
    try:
        Sn = Ex12.SimpsonRule(2.0, 3.0, 20, 5, 2.0, m=1.5, l=10.0, k=1)
        Sn.integrate(f7)
        print(
            f'f(x)=x^(h+1)/(h+1) + j + k + l*cos(m*x) / m -- SimpsonRule -- n: {Sn.n}, numericInteg: {Sn.Sn}, exactInteg: 123.52798931153073, error: {abs(Sn.Sn - 123.52798931153073)}')
        if abs(Sn.Sn - 123.52798931153073) > 1e-6:
            assert False
    except Exception as e:
        print(f'Errors {e} in simpson_rule function')
        assert False


def test_x_power_4_TrapezoidRule():
    assert run_fx(f1, g1, 2.5, 6.75, 1e-2, 'TrapezoidRule', 'x^4')


def test_x_power_5_TrapezoidRule():
    assert run_fx(f2, g2, 1.3, 10.4, 1e-2, 'TrapezoidRule', 'x^5')


def test_1_over_x_TrapezoidRule():
    assert run_fx(f3, g3, 0.018, 3.49, 1e-2, 'TrapezoidRule', '1/x')


def test_e_x_TrapezoidRule():
    assert run_fx(f4, g4, 1.5, 6.5, 1e-2, 'TrapezoidRule', 'e^x')


def test_sin_x_TrapezoidRule():
    assert run_fx(f5, g5, 0.1*math.pi, 0.9*math.pi,
                  1e-2, 'TrapezoidRule', 'sin(x)')


def test_default_arguments_TrapezoidRule():
    """Test default arguments"""
    try:
        Sn = Ex12.TrapezoidRule()
        Sn.integrate(f6)
        print(
            f'f(x)=1 -- TrapezoidRule -- n: {Sn.n}, numericInteg: {Sn.Sn}, exactInteg: 1.0, error: {abs(Sn.Sn - 1.0)}')
        if Sn.Sn != 1.0:
            assert False
    except:
        print(f'Errors in TrapezoidRule function')
        assert False


def test_arbitrary_arguments_TrapezoidRule():
    """Test arbitrary arguments"""
    try:
        Sn = Ex12.TrapezoidRule(2.0, 3.0, 20, 5, 2.0, m=1.5, l=10.0, k=1)
        Sn.integrate(f7)
        print(
            f'f(x)=x^(h+1)/(h+1) + j + k + l*cos(m*x) / m -- TrapezoidRule -- n: {Sn.n}, numericInteg: {Sn.Sn}, exactInteg: 123.52798931153073, error: {abs(Sn.Sn - 123.52798931153073)}')
        if abs(Sn.Sn - 123.52798931153073) > 1e-1:
            assert False
    except Exception as e:
        print(f'Errors {e} in TrapezoidRule function')
        assert False


def test_x_power_4_MidpointRule():
    assert run_fx(f1, g1, 2.5, 6.75, 1e-2, 'MidpointRule', 'x^4')


def test_x_power_5_MidpointRule():
    assert run_fx(f2, g2, 1.3, 10.4, 1e-2, 'MidpointRule', 'x^5')


def test_1_over_x_MidpointRule():
    assert run_fx(f3, g3, 0.018, 3.49, 1e-2, 'MidpointRule', '1/x')


def test_e_x_MidpointRule():
    assert run_fx(f4, g4, 1.5, 6.5, 1e-2, 'MidpointRule', 'e^x')


def test_sin_x_MidpointRule():
    assert run_fx(f5, g5, 0.1*math.pi, 0.9*math.pi,
                  1e-2, 'MidpointRule', 'sin(x)')


def test_default_arguments_MidpointRule():
    """Test default arguments"""
    try:
        Sn = Ex12.MidpointRule()
        Sn.integrate(f6)
        print(
            f'f(x)=1 -- MidpointRule -- n: {Sn.n}, numericInteg: {Sn.Sn}, exactInteg: 1.0, error: {abs(Sn.Sn - 1.0)}')
        if Sn.Sn != 1.0:
            assert False
    except:
        print(f'Errors in MidpointRule function')
        assert False


def test_arbitrary_arguments_MidpointRule():
    """Test arbitrary arguments"""
    try:
        Sn = Ex12.MidpointRule(2.0, 3.0, 20, 5, 2.0, m=1.5, l=10.0, k=1)
        Sn.integrate(f7)
        print(
            f'f(x)=x^(h+1)/(h+1) + j + k + l*cos(m*x) / m -- MidpointRule -- n: {Sn.n}, numericInteg: {Sn.Sn}, exactInteg: 123.52798931153073, error: {abs(Sn.Sn - 123.52798931153073)}')
        if abs(Sn.Sn - 123.52798931153073) > 1e-1:
            assert False
    except Exception as e:
        print(f'Errors {e} in MidpointRule function')
        assert False