import Ex6
import marshal
import base64

solution = '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'


def test_mortgage_value():
    """Test input 'value'"""
    try:
        Ex6.value
        print('Variable value found!')
    except:
        print('Variable value does not exist')
        assert False
    if Ex6.value <= 0:
        print(f'Invalid value = {Ex6.value}')
        assert False
    else:
        print(f'Valid value = {Ex6.value}')

    if isinstance(Ex6.value, float):
        print(f'Correct type(value) = {type(Ex6.value)}')
    else:
        print(f'Incorrect type(value) = {type(Ex6.value)}')
        assert False


def test_mortgage_downpay():
    """Test input 'downpay'"""
    try:
        Ex6.downpay
        print('Variable downpay found!')
    except:
        print('Variable downpay does not exist')
        assert False
    if Ex6.downpay <= 0:
        print(f'Invalid downpay = {Ex6.downpay}')
        assert False
    else:
        print(f'Valid downpay = {Ex6.downpay}')

    if isinstance(Ex6.downpay, float):
        print(
            f'Correct type(downpay) = {type(Ex6.downpay)}')
    else:
        print(f'Incorrect type(downpay) = {type(Ex6.downpay)}')
        assert False

    if Ex6.downpay > Ex6.value:
        print(f'Invalid downpay = {Ex6.downpay}')
        assert False
    else:
        print(f'Valid downpay = {Ex6.downpay}')

    print(f'Passed to test input "downpay"')


def test_mortgage_fixed_rate():
    """Test input 'fixed_rate'"""
    try:
        Ex6.fixed_rate
        print('Variable fixed_rate found!')
    except:
        print('Variable fixed_rate does not exist')
        assert False
    if Ex6.fixed_rate <= 0:
        print(f'Invalid fixed_rate = {Ex6.fixed_rate}')
        assert False
    elif Ex6.fixed_rate > 1:
        print(f'Invalid fixed_rate = {Ex6.fixed_rate}')
        assert False
    else:
        print(f'Valid fixed_rate = {Ex6.fixed_rate}')

    if isinstance(Ex6.fixed_rate, float):
        print(f'Valid type(fixed_rate) = {type(Ex6.fixed_rate)}')
    else:
        print(f'Invalid type(fixed_rate) = {type(Ex6.fixed_rate)}')
        assert False

    if Ex6.fixed_rate <= 0:
        print(f'Invalid fixed_rate = {Ex6.fixed_rate}')
        assert False
    elif Ex6.fixed_rate > 1:
        print(f'Invalid fixed_rate = {Ex6.fixed_rate}')
        assert False


def test_mortgage_N():
    """Test input 'N'"""
    try:
        Ex6.N
        print('Variable N found!')
    except:
        print('Variable N does not exist')
        assert False
    if Ex6.N <= 0:
        print(f'Invalid N = {Ex6.N}')
        assert False
    elif Ex6.N > 100:
        print(f'Invalid N = {Ex6.N}')
        assert False
    else:
        print(f'Valid N = {Ex6.N}')

    if isinstance(Ex6.N, int):
        print(f'Correct type(N) = {type(Ex6.N)}')
    else:
        print(f'Incorrect type(N) = {type(Ex6.N)}')
        assert False

    print(f'Passed to test input "N"')


def test_mortgage_message():
    """Test message to user"""
    try:
        Ex6.message
        print('Variable message found!')
    except:
        print('Variable message does not exist')
        assert False

    if isinstance(Ex6.message, str):
        print(f'Correct type(message) = {type(Ex6.message)}')
    else:
        print(f'Incorrect type(message) = {type(Ex6.message)}')
        assert False

    if len(Ex6.message) < 20:
        print(f'Too short message = {Ex6.message}')
        assert False
    else:
        print(f'Message = {Ex6.message}')


def test_mortgage_PV():
    """Test internal variable PV"""
    try:
        Ex6.PV
        print('Variable PV found!')
    except:
        print('Variable PV does not exist')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    message, PV, i, n, PMT, totalPMT, totalInterests, output_message = locals()['mortgage_calculation'](
        Ex6.value, Ex6.downpay, Ex6.fixed_rate, Ex6.N)

    if isinstance(Ex6.PV, float):
        print(f'Correct type(PV) = {type(Ex6.PV)}')
    else:
        print(f'Incorrect type(PV) = {type(Ex6.PV)}')
        assert False

    if abs(Ex6.PV - locals()['PV']) > 1e-6:
        print(f'Invalid PV = {Ex6.PV}')
        assert False
    else:
        print(f'Valid PV = {Ex6.PV}')


def test_mortgage_i():
    """Test internal variable 'i'"""
    try:
        Ex6.i
        print('Variable i found!')
    except:
        print('Variable i does not exist')
        assert False

    if isinstance(Ex6.i, float):
        print(f'Correct type(i) = {type(Ex6.i)}')
    else:
        print(f'Incorrect type(i) = {type(Ex6.i)}')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    message, PV, i, n, PMT, totalPMT, totalInterests, output_message = locals()['mortgage_calculation'](
        Ex6.value, Ex6.downpay, Ex6.fixed_rate, Ex6.N)
    if abs(Ex6.i - locals()['i']) > 1e-6:
        print(f'Invalid i = {Ex6.i}')
        assert False
    else:
        print(f'Valid i = {Ex6.i}')


def test_mortgage_n():
    """Test internal variable 'n'"""
    try:
        Ex6.n
        print('Variable n found!')
    except:
        print('Variable n does not exist')
        assert False

    if isinstance(Ex6.n, int):
        print(f'Correct type(n) = {type(Ex6.n)}')
    else:
        print(f'Incorrect type(n) = {type(Ex6.n)}')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    message, PV, i, n, PMT, totalPMT, totalInterests, output_message = locals()['mortgage_calculation'](
        Ex6.value, Ex6.downpay, Ex6.fixed_rate, Ex6.N)

    if abs(Ex6.n - locals()['n']) > 1e-6:
        print(f'Invalid n = {Ex6.n}')
        assert False
    else:
        print(f'Valid n = {Ex6.n}')


def test_mortgage_PMT():
    """Test internal variable 'PMT'"""
    try:
        Ex6.PMT
        print('Variable PMT found!')
    except:
        print('Variable PMT does not exist')
        assert False

    if isinstance(Ex6.PMT, float):
        print(f'Correct type(PMT) = {type(Ex6.PMT)}')
    else:
        print(f'Incorrect type(PMT) = {type(Ex6.PMT)}')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    message, PV, i, n, PMT, totalPMT, totalInterests, output_message = locals()['mortgage_calculation'](
        Ex6.value, Ex6.downpay, Ex6.fixed_rate, Ex6.N)

    if abs(Ex6.PMT - locals()['PMT']) > 1e-6:
        print(f'Invalid PMT = {Ex6.PMT}')
        assert False
    else:
        print(f'Valid PMT = {Ex6.PMT}')


def test_mortgage_output_message():
    """Test output message to user"""
    try:
        Ex6.output_message
        print('Variable output_message found!')
    except:
        print('Variable output_message does not exist')
        assert False

    if isinstance(Ex6.output_message, str):
        print(
            f'Correct type(output_message) = {type(Ex6.output_message)}')
    else:
        print(
            f'Incorrect type(output_message) = {type(Ex6.output_message)}')
        assert False

    if len(Ex6.output_message) < 20:
        print(
            f'Too short output_message = {Ex6.output_message}')
        assert False
    else:
        print(f'Message = {Ex6.output_message}')


def test_mortgage_totalPMT():
    """Test output variable 'totalPMT'"""
    try:
        Ex6.totalPMT
        print('Variable totalPMT found!')
    except:
        print(
            'Variable totalPMT does not exist')
        assert False

    if isinstance(Ex6.totalPMT, float):
        print(
            f'Correct type(totalPMT) = {type(Ex6.totalPMT)}')
    else:
        print(
            f'Incorrect type(totalPMT) = {type(Ex6.totalPMT)}')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    message, PV, i, n, PMT, totalPMT, totalInterests, output_message = locals()['mortgage_calculation'](
        Ex6.value, Ex6.downpay, Ex6.fixed_rate, Ex6.N)

    if abs(Ex6.totalPMT - locals()['totalPMT']) > 1e-6:
        print(
            f'Invalid totalPMT = {Ex6.totalPMT}')
        assert False
    else:
        print(
            f'Valid totalPMT = {Ex6.totalPMT}')


def test_totalInterests():
    """Test output variable 'totalInterests'"""
    try:
        Ex6.totalInterests
        print('Variable totalInterests found!')
    except:
        print('Variable totalInterests does not exist')
        assert False

    if isinstance(Ex6.totalInterests, float):
        print(
            f'Correct type(totalInterests) = {type(Ex6.totalInterests)}')
    else:
        print(
            f'Incorrect type(totalInterests) = {type(Ex6.totalInterests)}')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    message, PV, i, n, PMT, totalPMT, totalInterests, output_message = locals()['mortgage_calculation'](
        Ex6.value, Ex6.downpay, Ex6.fixed_rate, Ex6.N)

    if abs(Ex6.totalInterests - locals()['totalInterests']) > 1e-6:
        print(
            f'Invalid totalInterests = {Ex6.totalInterests}')
        assert False
    else:
        print(
            f'Valid totalInterests = {Ex6.totalInterests}')


def test_year():
    try:
        Ex6.year
        print('Variable year found!')
    except:
        print('Variable year does not exist')
        assert False

    if isinstance(Ex6.year, int):
        print(f'Correct type(year) = {type(Ex6.year)}')
    else:
        print(f'Incorrect type(year) = {type(Ex6.year)}')
        assert False

    if Ex6.year <= 0:
        print(f'Invalid year = {Ex6.year}')
        assert False
    else:
        print(f'Valid year = {Ex6.year}')


def test_is_leap():
    try:
        Ex6.is_leap
        print('Variable is_leap found!')
    except:
        print('Variable is_leap does not exist')
        assert False

    if isinstance(Ex6.is_leap, bool):
        print(f'Correct type(is_leap) = {type(Ex6.is_leap)}')
    else:
        print(f'Incorrect type(is_leap) = {type(Ex6.is_leap)}')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    is_leap, is_not_leap, leap_year_message = locals()[
        'leap_year_calculation'](Ex6.year)
    if Ex6.is_leap != locals()['is_leap']:
        print(f'Invalid is_leap = {Ex6.is_leap}')
        assert False
    else:
        print(f'Valid is_leap = {Ex6.is_leap}')


def test_is_not_leap():
    try:
        Ex6.is_not_leap
        print('Variable is_not_leap found!')
    except:
        print('Variable is_not_leap does not exist')
        assert False

    if isinstance(Ex6.is_not_leap, bool):
        print(f'Correct type(is_not_leap) = {type(Ex6.is_not_leap)}')
    else:
        print(f'Incorrect type(is_not_leap) = {type(Ex6.is_not_leap)}')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    is_leap, is_not_leap, leap_year_message = locals()[
        'leap_year_calculation'](Ex6.year)
    if Ex6.is_not_leap != locals()['is_not_leap']:
        print(f'Invalid is_not_leap = {Ex6.is_not_leap}')
        assert False
    else:
        print(f'Valid is_not_leap = {Ex6.is_not_leap}')


def test_leap_year_message():
    try:
        Ex6.leap_year_message
        print('Variable leap_year_message found!')
    except:
        print('Variable leap_year_message does not exist')
        assert False

    if isinstance(Ex6.leap_year_message, str):
        print(
            f'Correct type(leap_year_message) = {type(Ex6.leap_year_message)}')
    else:
        print(
            f'Incorrect type(leap_year_message) = {type(Ex6.leap_year_message)}')
        assert False

    if len(Ex6.leap_year_message) < 20:
        print(
            f'Too short leap_year_message = {Ex6.leap_year_message}')
        assert False
    else:
        print(f'Message = {Ex6.leap_year_message}')