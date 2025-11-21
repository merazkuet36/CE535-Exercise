import pytest
from Model2D.Face.Circle import Circle
from Model2D.Line import Line
from Model2D.Point import Point
import math


def test_circle_invalid_id():
    # Invalid id: string
    with pytest.raises(RuntimeError):
        Circle("xyz", [Line(1, [Point(1, 0, 0), Point(2, 1, 0)])])
    # Invalid id: list
    with pytest.raises(RuntimeError):
        Circle([1, 2], [Line(1, [Point(1, 0, 0), Point(2, 1, 0)])])
    # Invalid id: None
    with pytest.raises(RuntimeError):
        Circle(None, [Line(1, [Point(1, 0, 0), Point(2, 1, 0)])])


def test_circle_invalid_number_of_lines():
    # Invalid number of lines: 0
    with pytest.raises(RuntimeError):
        Circle(1, [])
    # Invalid number of lines: 2
    with pytest.raises(RuntimeError):
        Circle(1, [Line(1, [Point(1, 0, 0), Point(2, 1, 0)]),
               Line(2, [Point(2, 1, 0), Point(3, 0, 1)])])
    # Invalid number of lines: 3
    with pytest.raises(RuntimeError):
        Circle(1, [Line(1, [Point(1, 0, 0), Point(2, 1, 0)]), Line(
            2, [Point(2, 1, 0), Point(3, 0, 1)]),
            Line(3, [Point(3, 0, 1), Point(1, 0, 0)])])


def test_circle_invalid_radius():
    with pytest.raises(RuntimeError):
        Circle(1, [Line(1, [Point(1, 0, 0), Point(2, 0, 0)])])


def test_circle_valid_creation():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    l1 = Line(1, [p1, p2])
    lines = [l1]
    c = Circle(1, lines)
    assert c.id == 1
    assert c.lines == lines
    assert c.radius == 1
    assert c.center == p1
    
def test_circle_valid_perimeter():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    l1 = Line(1, [p1, p2])
    lines = [l1]
    c = Circle(1, lines)
    assert abs(c.perimeter() - 2 * math.pi * 1) < 1e-6
    
def test_circle_valid_area():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 0)
    l1 = Line(1, [p1, p2])
    lines = [l1]
    c = Circle(1, lines)
    assert abs(c.area() - math.pi * 1**2) < 1e-6