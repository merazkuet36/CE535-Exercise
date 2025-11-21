import importlib

def test_line_module_exists():
    try:
        importlib.import_module("Model2D.Line")
    except ModuleNotFoundError:
        assert False, "Model2D.Line module not found"

def test_face_rectangle_module_exists():
    try:
        importlib.import_module("Model2D.Face.Rectangle")
    except ModuleNotFoundError:
        assert False, "Model2D.Face.Rectangle module not found"

def test_face_triangle_module_exists():
    try:
        importlib.import_module("Model2D.Face.Triangle")
    except ModuleNotFoundError:
        assert False, "Model2D.Face.Triangle module not found"

def test_face_circle_module_exists():
    try:
        importlib.import_module("Model2D.Face.Circle")
    except ModuleNotFoundError:
        assert False, "Model2D.Face.Circle module not found"

def test_face_module_exists():
    try:
        importlib.import_module("Model2D.Face")
    except ModuleNotFoundError:
        assert False, "Model2D.Face module not found"

def test_point_module_exists():
    try:
        importlib.import_module("Model2D.Point")
    except ModuleNotFoundError:
        assert False, "Model2D.Point module not found"
