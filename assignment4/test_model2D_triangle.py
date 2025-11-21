
import pytest
from Model2D.Face.Triangle import Triangle
from Model2D.Point import Point
from Model2D.Line import Line


def test_triangle_invalid_id():
    # Invalid id: string
    with pytest.raises(RuntimeError):
        Triangle("abc", [
            Line(1, [Point(1, 0, 0), Point(2, 1, 0)]),
            Line(2, [Point(2, 1, 0), Point(3, 0, 1)]),
            Line(3, [Point(3, 0, 1), Point(1, 0, 0)])
        ])
    # Invalid id: list
    with pytest.raises(RuntimeError):
        Triangle([1, 2], [
            Line(1, [Point(1, 0, 0), Point(2, 1, 0)]),
            Line(2, [Point(2, 1, 0), Point(3, 0, 1)]),
            Line(3, [Point(3, 0, 1), Point(1, 0, 0)])
        ])
    # Invalid id: None
    with pytest.raises(RuntimeError):
        Triangle(None, [
            Line(1, [Point(1, 0, 0), Point(2, 1, 0)]),
            Line(2, [Point(2, 1, 0), Point(3, 0, 1)]),
            Line(3, [Point(3, 0, 1), Point(1, 0, 0)])
        ])


def test_triangle_invalid_number_of_lines():
    # Triangle expects 3 lines, not 2
    with pytest.raises(RuntimeError):
        Triangle(1, [
            Line(1, [Point(1, 0, 0), Point(2, 1, 0)]),
            Line(2, [Point(2, 1, 0), Point(3, 0, 1)])
        ])
    # Triangle expects 3 lines, not 4
    with pytest.raises(RuntimeError):
        Triangle(1, [
            Line(1, [Point(1, 0, 0), Point(2, 1, 0)]),
            Line(2, [Point(2, 1, 0), Point(3, 0, 1)]),
            Line(3, [Point(3, 0, 1), Point(1, 0, 0)]),
            Line(4, [Point(4, 0, 1), Point(1, 0, 0)])
        ])
    # Triangle expects 3 lines, not 1
    with pytest.raises(RuntimeError):
        Triangle(1, [
            Line(1, [Point(1, 0, 0), Point(2, 1, 0)])
        ])
    # Triangle expects 3 lines, not 0
    with pytest.raises(RuntimeError):
        Triangle(1, [])


def test_triangle_non_connected_lines():
    with pytest.raises(RuntimeError):
        p1 = Point(1, 0, 0)
        p2 = Point(2, 1, 0)
        p3 = Point(3, 0, 1)
        l1 = Line(1, [p1, p2])
        l2 = Line(2, [p2, p3])
        l3 = Line(3, [p3, p2])
        lines = [l1, l2, l3]
        Triangle(1, lines)
    with pytest.raises(RuntimeError):
        p1 = Point(1, 0, 0)
        p2 = Point(2, 1, 0)
        p3 = Point(3, 0, 1)
        l1 = Line(1, [p1, p2])
        l2 = Line(2, [p1, p3])
        l3 = Line(3, [p3, p1])
        lines = [l1, l2, l3]
        Triangle(1, lines)


def test_triangle_perimeter():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 0, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p1])
    lines = [l1, l2, l3]
    t = Triangle(1, lines)
    assert abs(t.perimeter() - (1 + 1 + 2**0.5)) < 1e-6


def test_triangle_area():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 0, 1)
    l1 = Line(1, [p1, p2])
    l2 = Line(2, [p2, p3])
    l3 = Line(3, [p3, p1])
    lines = [l1, l2, l3]
    t = Triangle(1, lines)
    assert abs(t.area() - 0.5) < 1e-6
