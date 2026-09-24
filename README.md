<<<<<<< HEAD
# School Grade Predictor - Version 1

A deliberately simple Flask application for teaching:

- Python
- pytest
- code coverage
- SonarQube
- Docker
- Docker Compose
- Azure DevOps Pipelines
- GitHub Actions

The application intentionally contains some code-quality issues so students can observe SonarQube findings.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python -m pytest
python -m coverage run -m pytest
python -m coverage xml -o coverage.xml
python app/main.py
```

Open http://localhost:5000

## Test API

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Rahul\",\"attendance\":95,\"study_hours\":8,\"previous_score\":90,\"assignment_score\":92,\"internal_score\":94}"
```

## Docker

```bash
docker build -t school-grade-predictor:latest .
docker run -d --name grade-predictor -p 5000:5000 school-grade-predictor:latest
```

## Docker Compose

```bash
docker compose up --build
```

## CI/CD

- Azure DevOps: `azure-pipelines.yml`
- GitHub Actions: `.github/workflows/ci-cd.yml`

Both pipelines install dependencies, run tests/coverage, and build the Docker image.

## SonarQube

For SonarQube Cloud/Server, configure the project and scanner in the CI platform, then use `sonar-project.properties`.

The project is intentionally designed so students can first analyze the "bad" version, fix issues, increase test coverage, and analyze it again.
=======
# sonarqube-integration-
>>>>>>> 09d91870f12053559bf6c47cbac8dbaf6a417af4
