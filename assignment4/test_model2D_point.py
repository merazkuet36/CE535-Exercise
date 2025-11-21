
import pytest
from Model2D.Point import Point


def test_point_invalid_id():
    # id as string that cannot convert to int
    with pytest.raises(RuntimeError):
        Point("abc", 1.0, 2.0)

    # id as float string that can be float but not int
    with pytest.raises(RuntimeError):
        Point("3.14", 1.0, 2.0)

    # id as None
    with pytest.raises(RuntimeError):
        Point(None, 1.0, 2.0)

    # id as list
    with pytest.raises(RuntimeError):
        Point([1, 2], 1.0, 2.0)


def test_point_valid_creation():
    p = Point(1, 1.0, 2.0)
    assert p.id == 1
    assert p.x == 1.0
    assert p.y == 2.0


def test_point_str_repr():
    p = Point(1, 1.0, 2.0)
    assert len(str(p)) > 0


def test_point_invalid_x():
    # x as a string that can't convert to float
    with pytest.raises(RuntimeError):
        Point(1, "abc", 2.0)

    # x as None
    with pytest.raises(RuntimeError):
        Point(1, None, 2.0)

    # x as a list
    with pytest.raises(RuntimeError):
        Point(1, [1, 2], 2.0)

    # x as a dict
    with pytest.raises(RuntimeError):
        Point(1, {}, 2.0)


def test_point_valid_x():
    p = Point(1, 1.0, 2.0)
    assert p.x == 1.0


def test_point_invalid_y():
    # y as a string that can't convert to float
    with pytest.raises(RuntimeError):
        Point(1, 1.0, "abc")

    # y as None
    with pytest.raises(RuntimeError):
        Point(1, 1.0, None)

    # y as a list
    with pytest.raises(RuntimeError):
        Point(1, 1.0, [1, 2])

    # y as a dict
    with pytest.raises(RuntimeError):
        Point(1, 1.0, {})


def test_point_valid_y():
    p = Point(1, 1.0, 2.0)
    assert p.y == 2.0


def test_point_move():
    p = Point(1, 1.0, 2.0)
    p.move(1.0, 2.0)
    assert p.x == 2.0
    assert p.y == 4.0

    # test invalid dx and dy
    with pytest.raises(RuntimeError):
        p.move("abc", 2.0)
    with pytest.raises(RuntimeError):
        p.move(1.0, "abc")
    with pytest.raises(RuntimeError):
        p.move(1.0, None)
    with pytest.raises(RuntimeError):
        p.move([1, 2], 2.0)
    with pytest.raises(RuntimeError):
        p.move(1.0, [1, 2])
    with pytest.raises(RuntimeError):
        p.move({}, 2.0)
    with pytest.raises(RuntimeError):
        p.move(1.0, {})


def test_point_valid_move():
    p = Point(1, 1.0, 2.0)
    p.move(1.0, 2.0)
    assert p.x == 2.0
    assert p.y == 4.0
