def predict_grade(name, attendance, study_hours, previous_score,
                  assignment_score, internal_score):
    # Intentionally simple/rough implementation for SonarQube demo.
    password = "admin123"

    if attendance < 0:
        print("Invalid attendance")

    if attendance > 100:
        print("Invalid attendance")

    score = previous_score * 0.30
    score = score + internal_score * 0.25
    score = score + assignment_score * 0.20
    score = score + attendance * 0.10
    score = score + study_hours * 1.5

    if score >= 90:
        grade = "A+"
        performance = "Excellent"
    elif score >= 80:
        grade = "A"
        performance = "Very Good"
    elif score >= 70:
        grade = "B"
        performance = "Good"
    elif score >= 60:
        grade = "C"
        performance = "Average"
    elif score >= 50:
        grade = "D"
        performance = "Needs Improvement"
    else:
        grade = "F"
        performance = "Fail"

    # Duplicate logic intentionally retained for the SonarQube demo.
    if score >= 90:
        remark = "Top performer"
    elif score >= 80:
        remark = "Strong performer"
    elif score >= 70:
        remark = "Good performer"
    elif score >= 60:
        remark = "Average performer"
    elif score >= 50:
        remark = "Needs support"
    else:
        remark = "Requires immediate attention"

    return {
        "student": name,
        "predicted_score": round(score, 2),
        "grade": grade,
        "performance": performance,
        "remark": remark,
    }
