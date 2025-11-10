from Shape import Shape
from Rectangle import Rectangle
from Sphere import Sphere
import math


def test_shape_str():
    shape = Shape()
    success = False
    try:
        s = str(shape)
        success = True
    except Exception as e:
        success = False
    assert success


def test_shape_area():
    shape = Shape()
    try:
        area = shape.area()
    except Exception as e:
        assert False
    assert area == 0.0


def test_shape_perimeter():
    shape = Shape()
    try:
        perimeter = shape.perimeter()
    except Exception as e:
        assert False
    assert perimeter == 0.0


def test_shape_volume():
    shape = Shape()
    try:
        volume = shape.volume()
    except Exception as e:
        assert False
    assert volume == 0.0


def test_rectangle_init():
    success = False
    try:
        rectangle = Rectangle(width=10, height=20)
        success = True
    except Exception as e:
        success = False
    assert success


def test_rectangle_init_negative_width():
    success = False
    try:
        rectangle = Rectangle(width=-10, height=20)
        success = False
    except RuntimeError as e:
        success = True
    assert success


def test_rectangle_init_negative_height():
    success = False
    try:
        rectangle = Rectangle(width=10, height=-20)
        success = False
    except RuntimeError as e:
        success = True
    assert success


def test_rectangle_str():
    success = False
    try:
        rectangle = Rectangle(width=10, height=20)
        s = str(rectangle)
        success = True
    except Exception as e:
        success = False
    assert success


def test_rectangle_area():
    rectangle = Rectangle(width=10, height=20)
    try:
        area = rectangle.area()
    except Exception as e:
        assert False
    assert area == 200.0


def test_rectangle_perimeter():
    rectangle = Rectangle(width=10, height=20)
    try:
        perimeter = rectangle.perimeter()
    except Exception as e:
        assert False
    assert perimeter == 60.0


def test_rectangle_volume():
    rectangle = Rectangle(width=10, height=20)
    success = False
    try:
        volume = rectangle.volume()
        success = False
    except RuntimeError as e:
        success = True
    assert success


def test_sphere_init():
    try:
        sphere = Sphere(radius=10)
    except Exception as e:
        assert False
    assert True


def test_sphere_init_negative_radius():
    try:
        sphere = Sphere(radius=-10)
        assert False
    except RuntimeError as e:
        assert True


def test_sphere_str():
    try:
        sphere = Sphere(radius=10)
        s = str(sphere)
        assert True
    except Exception as e:
        assert False


def test_sphere_area():
    sphere = Sphere(radius=10)
    try:
        area = sphere.area()
    except Exception as e:
        assert False
    assert abs(area - 400.0 * math.pi) < 1e-6


def test_sphere_perimeter():
    sphere = Sphere(radius=10)
    success = False
    try:
        perimeter = sphere.perimeter()
        success = False
    except Exception as e:
        success = True
    assert success


def test_sphere_volume():
    sphere = Sphere(radius=10)
    try:
        volume = sphere.volume()
    except Exception as e:
        assert False
    assert abs(volume - 4/3 * math.pi * 10 ** 3) < 1e-6