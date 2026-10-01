from calculator import average, grade


def test_average():
    assert average([80, 90, 70]) == 80


def test_grade():
    assert grade(80) == "B"


def test_empty():
    try:
        average([])
        assert False
    except ValueError:
        assert True
