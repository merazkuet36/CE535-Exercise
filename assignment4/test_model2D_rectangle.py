import pytest
from Model2D.Face.Rectangle import Rectangle
from Model2D.Point import Point
from Model2D.Line import Line


def test_rectangle_invalid_id():
    with pytest.raises(RuntimeError):
        Rectangle("abc", [Line(2, [Point(3, 0, 0), Point(4, 1, 0)]), Line(3, [Point(4, 1, 0), Point(
            5, 1, 1)]), Line(4, [Point(5, 1, 1), Point(6, 0, 1)]), Line(5, [Point(6, 0, 1), Point(3, 0, 0)])])
    with pytest.raises(RuntimeError):
        Rectangle([1, 2], [Line(2, [Point(3, 0, 0), Point(4, 1, 0)]), Line(3, [Point(4, 1, 0), Point(
            5, 1, 1)]), Line(4, [Point(5, 1, 1), Point(6, 0, 1)]), Line(5, [Point(6, 0, 1), Point(3, 0, 0)])])
    with pytest.raises(RuntimeError):
        Rectangle(None, [Line(2, [Point(3, 0, 0), Point(4, 1, 0)]), Line(3, [Point(4, 1, 0), Point(
            5, 1, 1)]), Line(4, [Point(5, 1, 1), Point(6, 0, 1)]), Line(5, [Point(6, 0, 1), Point(3, 0, 0)])])


def test_rectangle_invalid_number_of_lines():
    # Rectangle expects 4 lines, not 3
    with pytest.raises(RuntimeError):
        Rectangle(1, [Line(2, [Point(3, 0, 0), Point(4, 1, 0)]),
                  Line(3, [Point(4, 1, 0), Point(5, 1, 1)])])
    # Rectangle expects 4 lines, not 5
    with pytest.raises(RuntimeError):
        Rectangle(1, [Line(2, [Point(3, 0, 0), Point(4, 1, 0)]), Line(
            3, [Point(4, 1, 0), Point(5, 1, 1)]), Line(4, [Point(5, 1, 1), Point(6, 0, 1)])])
    # Rectangle expects 4 lines, not 2
    with pytest.raises(RuntimeError):
        Rectangle(1, [Line(2, [Point(3, 0, 0), Point(4, 1, 0)])])
    # Rectangle expects 4 lines, not 1
    with pytest.raises(RuntimeError):
        Rectangle(1, [Line(2, [Point(3, 0, 0), Point(4, 1, 0)])])


def test_rectangle_non_connected_lines():
    with pytest.raises(RuntimeError):
        p1 = Point(1, 0, 0)
        p2 = Point(2, 1, 0)
        p3 = Point(3, 0, 1)
        p4 = Point(4, 0, 0)
        l1 = Line(1, [p1, p2])
        l2 = Line(2, [p2, p3])
        l3 = Line(3, [p3, p4])
        l4 = Line(4, [p4, p1])
        lines = [l1, l2, l3, l4]
        Rectangle(1, lines)
    with pytest.raises(RuntimeError):
        p1 = Point(1, 0, 0)
        p2 = Point(2, 1, 0)
        p3 = Point(3, 1, 1)
        p4 = Point(4, 0, 1)
        l1 = Line(1, [p1, p2])
        l2 = Line(2, [p2, p3])
        l3 = Line(3, [p3, p4])
        l4 = Line(4, [p4, p2])
        lines = [l1, l2, l3, l4]
        Rectangle(1, lines)
        

def test_rectangle_non_parallel_lines():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 2, 2)
    p4 = Point(4, 0, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p4])
    l4 = Line(4, [p4, p1])
    lines = [l1, l2, l3, l4]
    with pytest.raises(RuntimeError):
        Rectangle(1, lines)


def test_rectangle_non_perpendicular_lines():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 2, 1)
    p4 = Point(4, 0, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p4])
    l4 = Line(4, [p4, p1])
    lines = [l1, l2, l3, l4]
    with pytest.raises(RuntimeError):
        Rectangle(1, lines)


def test_rectangle_valid_creation():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 1, 1)
    p4 = Point(4, 0, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p4])
    l4 = Line(4, [p4, p1])
    lines = [l1, l2, l3, l4]
    r = Rectangle(1, lines)

    for line in lines:
        print(line.length())
    assert r.id == 1
    assert r.lines == lines


def test_rectangle_valid_area():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 1, 1)
    p4 = Point(4, 0, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p4])
    l4 = Line(4, [p4, p1])
    lines = [l1, l2, l3, l4]
    r = Rectangle(1, lines)
    assert abs(r.area() - 1) < 1e-6


def test_rectangle_valid_perimeter():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 1, 1)
    p4 = Point(4, 0, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p4])
    l4 = Line(4, [p4, p1])
    lines = [l1, l2, l3, l4]
    r = Rectangle(1, lines)
    assert abs(r.perimeter() - 4) < 1e-6
