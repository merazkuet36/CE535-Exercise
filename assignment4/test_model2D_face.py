import pytest
from Model2D.Point import Point
from Model2D.Line import Line
from Model2D.Face import Face


def test_face_invalid_id():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 1, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p1])
    lines = [l1, l2, l3]
    # id as string
    with pytest.raises(RuntimeError):
        Face("abc", lines)
    # id as list
    with pytest.raises(RuntimeError):
        Face([1, 2], lines)
    # id as None
    with pytest.raises(RuntimeError):
        Face(None, lines)
    # id as a string-number not convertible to int
    with pytest.raises(RuntimeError):
        Face("3.14", lines)


def test_face_valid_creation():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 1, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p1])
    lines = [l1, l2, l3]
    f = Face(1, lines)
    assert f.id == 1
    assert f.lines == lines


def test_face_invalid_lines():
    # lines as not a list
    with pytest.raises(RuntimeError):
        Face(1, "abc")
    # lines as a list with not Line objects
    with pytest.raises(RuntimeError):
        Face(1, [1, 2])
    # lines as a list with None
    with pytest.raises(RuntimeError):
        Face(1, [None, Line(2, [Point(2, 1, 1), Point(3, 2, 2)])])
    # lines as a list with not Line objects
    with pytest.raises(RuntimeError):
        Face(1, [Line(1, [Point(1, 0, 0), Point(2, 1, 1)]),
             "abc", Line(3, [Point(3, 2, 2), Point(4, 3, 3)])])


def test_face_valid_lines():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 1, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p1])
    lines = [l1, l2, l3]
    f = Face(1, lines)
    assert f.lines == lines


def test_face_str_repr():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 1, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p1])
    lines = [l1, l2, l3]
    f = Face(1, lines)
    assert len(str(f)) > 0


def test_face_valid_perimeter():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 1, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p1])
    lines = [l1, l2, l3]
    f = Face(1, lines)
    assert abs(f.perimeter() - (1 + 1 + 2**0.5)) < 1e-6


def test_face_valid_area():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 1, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p1])
    lines = [l1, l2, l3]
    f = Face(1, lines)
    assert abs(f.area() - 0.0) < 1e-6
