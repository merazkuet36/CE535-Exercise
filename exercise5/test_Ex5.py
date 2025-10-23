import Ex5
import marshal
import base64


solution = '''
4wAAAAAAAAAAAAAAAAIAAAAAAAAA82YAAACXAGQAZAFsAFoAZAJaAWQDWgJkBFoDZAVaBGUAagoAAAAAAAAAAAAAAAAAAAAAAABkBnoFAABkB3oFAABaBmUAagoAAAAAAAAAAAAAAAAAAAAAAABkCHoFAABaB2QJWghkCloJeQEpC+kAAAAATmcAAAAAAAAMQGcAAAAAAAAUwOkBAAAA2gRhYWFhZy1DHOviNro/ZwAAAAAAAClAZwAAAAAAABlAZzbRaDFCq/c/Z2dmZmZmplhAKQraBG1hdGjaBWFuZ2xl2gVBbmdsZdoFaW5kZXjaA21zZ9oCcGnaAVbaAUHaAXnaAUapAPMAAAAAegZFeDUucHnaCDxtb2R1bGU+chEAAAABAAAAc0UAAADwAwEBAdsAC+AIC4AF2AgMgAXYCAmABdgGDIAD4AQIh0eBR4hHgU+QRNEEGIAB2AQIh0eBR4hGgU6AAdgEGYAB2AQNgQFyEAAAAA==
'''


def test_V():
    """Volume of a cylinder with height of 12.5 meter and radius of 0.32 meter"""
    try:
        Ex5.V
        print('Variable V found!')
    except:
        print('Variable V does not exist')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    if abs(Ex5.V-locals()['V']) > 1e-6:
        print(f'Incorrect V = {Ex5.V}')
        assert False
    else:
        print(f'Correct V = {Ex5.V}')
        assert True


def test_A():
    """Compute the area of a circle with radius 2.5 inch"""
    try:
        Ex5.A
        print('Variable A found!')
    except:
        print('Variable A does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if abs(Ex5.A - locals()['A']) > 1e-6:
        print(f'Incorrect A = {Ex5.A}')
        assert False
    else:
        print(f'Correct A = {Ex5.A}')
        assert True


def test_y():
    """Compute $y = 10^{2/3} - 10^{0.5}$"""
    try:
        Ex5.y
        print('Variable y found!')
    except:
        print('Variable y does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if abs(Ex5.y - locals()['y']) > 1e-6:
        print(f'Incorrect y = {Ex5.y}')
        assert False
    else:
        print(f'Correct y = {Ex5.y}')
        assert True


def test_F():
    """Convert 37 degree Celsius to Fahrenheit"""
    try:
        Ex5.F
        print('Variable F found!')
    except:
        print('Variable F does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if abs(Ex5.F - locals()['F']) > 1e-6:
        print(f'Incorrect F = {Ex5.F}')
        assert False
    else:
        print(f'Correct F = {Ex5.F}')
        assert True


def test_positive_float():
    """Test positive float type"""
    try:
        Ex5.angle
        print('Variable angle found!')
    except:
        print('Variable "angle" does not exist')
        assert False
    if type(Ex5.angle) != float:
        print(f'Incorrect angle type = {type(Ex5.angle)}')
        assert False
    else:
        print(f'Correct angle type = {type(Ex5.angle)}')

    if Ex5.angle <= 0:
        print(f'Incorrect angle = {Ex5.angle}')
        assert False
    else:
        print(f'Correct angle = {Ex5.angle}')
        assert True


def test_negative_float():
    """Test negative float type"""
    try:
        Ex5.Angle
        print('Variable "Angle" found!')
    except:
        print('Variable "Angle" does not exist')
        assert False

    if type(Ex5.Angle) != float:
        print(f'Incorrect type(Angle) = {type(Ex5.Angle)}')
        assert False
    else:
        print(f'Correct type(Angle) = {type(Ex5.Angle)}')

    if Ex5.Angle >= 0:
        print(f'Incorrect Angle = {Ex5.Angle}')
        assert False
    else:
        print(f'Correct Angle = {Ex5.Angle}')
        assert True


def test_int():
    """Test negative float type"""
    try:
        Ex5.index
        print('Variable "index" found!')
    except:
        print('Variable "index" does not exist')
        assert False

    if type(Ex5.index) != int:
        print(f'Incorrect type(index) = {type(Ex5.index)}')
        assert False
    else:
        print(f'Correct type(index) = {type(Ex5.index)}')
        assert True


def test_string():
    """Test string type"""
    try:
        Ex5.msg
        print('Variable "msg" found!')

    except:
        print('Variable "msg" does not exist')
        assert False

    if type(Ex5.msg) != str:
        print(f'Incorrect msg type = {type(Ex5.msg)}')
        assert False
    else:
        print(f'Correct msg type = {type(Ex5.msg)}')
        assert True