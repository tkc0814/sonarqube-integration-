const form = document.querySelector("#predict-form");
const submitButton = document.querySelector("#submit-button");
const errorBox = document.querySelector("#form-error");
const emptyResult = document.querySelector("#result-empty");
const resultContent = document.querySelector("#result-content");

const numberFields = ["attendance", "study_hours", "previous_score", "assignment_score", "internal_score"];

function clearError() {
  errorBox.hidden = true;
  errorBox.textContent = "";
  form.querySelectorAll("[aria-invalid='true']").forEach((field) => field.removeAttribute("aria-invalid"));
}

function showError(message, fieldName) {
  errorBox.textContent = message;
  errorBox.hidden = false;
  if (fieldName) {
    const field = form.elements.namedItem(fieldName);
    field?.setAttribute("aria-invalid", "true");
    field?.focus();
  }
}

function readForm() {
  const values = Object.fromEntries(new FormData(form).entries());
  values.name = values.name.trim();
  for (const field of numberFields) values[field] = Number(values[field]);
  return values;
}

function validate(values) {
  if (!values.name) return ["Add the student's name to continue.", "name"];
  for (const field of numberFields) {
    if (!Number.isFinite(values[field])) return ["Enter a valid number in every learning indicator.", field];
  }
  for (const field of ["attendance", "previous_score", "assignment_score", "internal_score"]) {
    if (values[field] < 0 || values[field] > 100) return ["Attendance and scores must be between 0 and 100.", field];
  }
  if (values.study_hours < 0 || values.study_hours > 24) return ["Study time must be between 0 and 24 hours per day.", "study_hours"];
  return null;
}

function showResult(result) {
  document.querySelector("#result-name").textContent = result.student;
  document.querySelector("#result-grade").textContent = result.grade;
  document.querySelector("#result-performance").textContent = result.performance;
  document.querySelector("#result-score").textContent = Number(result.predicted_score).toFixed(2);
  document.querySelector("#result-remark").textContent = result.remark;
  document.querySelector("#score-fill").style.width = `${Math.max(0, Math.min(100, result.predicted_score))}%`;
  emptyResult.hidden = true;
  resultContent.hidden = false;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  clearError();
  const values = readForm();
  const validationError = validate(values);
  if (validationError) {
    showError(...validationError);
    return;
  }

  submitButton.disabled = true;
  submitButton.querySelector(".button-text").textContent = "Calculating…";
  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(values),
    });
    const result = await response.json();
    if (!response.ok) {
      showError(result.error || "We couldn't generate a prediction. Check the details and try again.");
      return;
    }
    showResult(result);
    document.querySelector(".result-panel").scrollIntoView({ behavior: "smooth", block: "nearest" });
  } catch {
    showError("The predictor couldn't be reached. Please check that the app is running and try again.");
  } finally {
    submitButton.disabled = false;
    submitButton.querySelector(".button-text").textContent = "Generate prediction";
  }
});

document.querySelector("#sample-button").addEventListener("click", () => {
  const sample = { name: "Alex Morgan", attendance: 92, study_hours: 4, previous_score: 82, assignment_score: 86, internal_score: 88 };
  for (const [name, value] of Object.entries(sample)) form.elements.namedItem(name).value = value;
  clearError();
  form.elements.namedItem("name").focus();
});

document.querySelector("#reset-button").addEventListener("click", () => {
  resultContent.hidden = true;
  emptyResult.hidden = false;
  form.elements.namedItem("name").focus();
});

form.addEventListener("input", (event) => {
  if (event.target.matches("input[aria-invalid='true']")) event.target.removeAttribute("aria-invalid");
  if (form.querySelectorAll("[aria-invalid='true']").length === 0) clearError();
});
