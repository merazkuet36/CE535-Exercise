import pytest
from Model2D.Point import Point
from Model2D.Line import Line


def test_line_invalid_id():
    # id as string that cannot convert to int
    with pytest.raises(RuntimeError):
        Line("abc", [Point(1, 0, 0), Point(2, 1, 1)])
    # id as list
    with pytest.raises(RuntimeError):
        Line([1, 2], [Point(1, 0, 0), Point(2, 1, 1)])
    # id as None
    with pytest.raises(RuntimeError):
        Line(None, [Point(1, 0, 0), Point(2, 1, 1)])
    # id as float string that is not integer
    with pytest.raises(RuntimeError):
        Line("3.14", [Point(1, 0, 0), Point(2, 1, 1)])

def test_line_valid_creation():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 1)
    l = Line(1, [p1, p2])
    assert l.id == 1
    assert l.points == [p1, p2]

def test_line_str_repr():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 1)
    l = Line(1, [p1, p2])
    assert len(str(l)) > 0

def test_line_invalid_points():
    # points as not a list
    with pytest.raises(RuntimeError):
        Line(1, "abc")
    # points as a list with not Point objects
    with pytest.raises(RuntimeError):
        Line(1, [1, 2])
    # points as a list with None
    with pytest.raises(RuntimeError):
        Line(1, [None, Point(2,1,1)])
    # points as a list with not Point objects
    with pytest.raises(RuntimeError):
        Line(1, [Point(1,0,0), "abc", Point(3,2,2)])

def test_line_valid_points():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 1)
    l = Line(1, [p1, p2])
    assert l.points == [p1, p2]

def test_line_length():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 1)
    l = Line(1, [p1, p2])
    assert l.length() == (1**2 + 1**2)**0.5
    
def test_line_direction():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 1)
    l = Line(1, [p1, p2])
    assert l.direction() == (1/((1**2 + 1**2)**0.5), 1/((1**2 + 1**2)**0.5))
    
def test_line_invalid_direction():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 1)
    l = Line(1, [p1, p2])
    assert l.direction() == (1/((1**2 + 1**2)**0.5), 1/((1**2 + 1**2)**0.5))

def test_line_direction_unit_vector():
    p1 = Point(1, 0, 0)
    p2 = Point(2, 1, 1)
    l = Line(1, [p1, p2])
    assert l.direction() == (1/((1**2 + 1**2)**0.5), 1/((1**2 + 1**2)**0.5))