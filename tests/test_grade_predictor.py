from app.grade_predictor import predict_grade


def test_grade_a_plus():
    result = predict_grade("Rahul", 95, 8, 95, 90, 92)
    assert result["grade"] == "A+"


def test_grade_a():
    result = predict_grade("Priya", 90, 6, 85, 80, 82)
    assert result["grade"] == "A"


def test_grade_b():
    result = predict_grade("Arun", 85, 5, 75, 70, 72)
    assert result["grade"] == "B"


def test_grade_c():
    result = predict_grade("Meena", 80, 4, 65, 60, 62)
    assert result["grade"] == "C"


def test_grade_f():
    result = predict_grade("Kiran", 60, 1, 30, 35, 40)
    assert result["grade"] == "F"
