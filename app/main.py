from math import isfinite

from flask import Flask, jsonify, render_template, request
from grade_predictor import predict_grade

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Send the student details as a JSON object."}), 400

    name = data.get("name")
    if not isinstance(name, str) or not name.strip() or len(name.strip()) > 80:
        return jsonify({"error": "Enter a student name between 1 and 80 characters."}), 400

    try:
        attendance = float(data["attendance"])
        study_hours = float(data["study_hours"])
        previous_score = float(data["previous_score"])
        assignment_score = float(data["assignment_score"])
        internal_score = float(data["internal_score"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Complete every score and study-hours field with a number."}), 400

    numeric_values = (attendance, study_hours, previous_score, assignment_score, internal_score)
    if not all(isfinite(value) for value in numeric_values):
        return jsonify({"error": "Values must be finite numbers."}), 400

    if not 0 <= attendance <= 100:
        return jsonify({"error": "Attendance must be between 0 and 100."}), 400
    if not 0 <= study_hours <= 24:
        return jsonify({"error": "Study hours must be between 0 and 24 per day."}), 400
    if any(not 0 <= score <= 100 for score in (previous_score, assignment_score, internal_score)):
        return jsonify({"error": "Scores must be between 0 and 100."}), 400

    result = predict_grade(
        name.strip(),
        attendance,
        study_hours,
        previous_score,
        assignment_score,
        internal_score,
    )

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
