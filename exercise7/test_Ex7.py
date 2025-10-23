import Ex7
import marshal
import base64
import math

solution = '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'


def test_input_number():
    try:
        Ex7.input_number
        print('Variable input_number found!')
    except:
        print('Variable input_number does not exist')
        assert False
    if not isinstance(Ex7.input_number, float) and not isinstance(Ex7.input_number, int):
        print(f'Invalid input_number = {Ex7.input_number}')
        assert False
    else:
        print(f'Valid input_number = {Ex7.input_number}')


def test_category():
    try:
        Ex7.category
        print('Variable category found!')
    except:
        print('Variable category does not exist')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    category = locals()['categorize_number'](Ex7.input_number)

    if Ex7.category != category:
        print(f'Invalid category = {Ex7.category}')
        assert False
    else:
        print(f'Valid category = {Ex7.category}')


def test_cemented_soil_model():
    try:
        Ex7.y
        print('Variable y found!')
    except:
        print('Variable y does not exist')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    p = locals()['cemented_soil_model'](Ex7.y)

    if Ex7.p != p:
        print(f'Invalid p = {Ex7.p}')
        assert False
    else:
        print(f'Valid p = {Ex7.p}')


def test_heaviside_function_1():
    try:
        Ex7.x
        print('Variable x found!')
    except:
        print('Variable x does not exist')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    flag = locals()['heaviside_function'](Ex7.x)

    if Ex7.flag != flag:
        print(f'Invalid flag = {Ex7.flag}')
        assert False
    else:
        print(f'Valid flag = {Ex7.flag}')


def test_heaviside_function_2():
    try:
        Ex7.x
        print('Variable x found!')
    except:
        print('Variable x does not exist')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    ternary_flag = locals()['heaviside_function_ternary'](Ex7.x)

    if Ex7.ternary_flag != ternary_flag:
        print(f'Invalid ternary_flag = {Ex7.ternary_flag}')
        assert False
    else:
        print(f'Valid ternary_flag = {Ex7.ternary_flag}')


def test_heaviside_function_3():
    try:
        Ex7.x
        print('Variable x found!')
    except:
        print('Variable x does not exist')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    g = locals()['heaviside_function_match'](Ex7.x)

    if abs(Ex7.g - g) > 1e-6:
        print(f'Invalid g = {Ex7.g}')
        assert False
    else:
        print(f'Valid g = {Ex7.g}')