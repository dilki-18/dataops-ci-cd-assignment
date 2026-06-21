# DataOps CI/CD Assignment

This repository demonstrates a simple Python ETL pipeline for cleaning customer data, with Docker support and a small validation test.

## Repository Structure

- `src/etl.py` - ETL script that reads `data/customers.csv`, drops rows with missing values, and writes cleaned output to `data/processed/cleaned_customers.csv`.
- `data/customers.csv` - raw customer dataset used as the ETL input.
- `data/processed/` - output directory for the cleaned dataset.
- `requirements.txt` - Python dependencies for the ETL pipeline and tests.
- `Dockerfile` - container definition for running the pipeline in Docker.
- `tests/test_elt.py` - test that verifies the cleaned dataset contains no null values.
- `terraform/` - infrastructure demonstration files.

## Requirements

- Python 3.12+
- `pip`
- `docker` (optional, for containerized execution)

Dependencies are listed in `requirements.txt`, including `pandas` and `pytest`.

## Setup

1. Create and activate a Python virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Running the ETL pipeline

From the repository root, run:

```bash
python src/etl.py
```

This reads the raw input file at `data/customers.csv`, removes any rows with missing values, and writes the cleaned file to `data/processed/cleaned_customers.csv`.

## Running tests

Run the validation test with:

```bash
pytest tests/test_elt.py
```

The test checks that the output CSV contains zero null values.

## Running with Docker

Build and run the container:

```bash
docker build -t dataops-etl .
docker run --rm dataops-etl
```

The Docker container executes `src/etl.py` by default.

## Notes

- The current ETL process only performs null-value removal as the transformation step.
- To extend the pipeline, update `src/etl.py` with additional transformation or validation logic.
- Ensure `data/customers.csv` is present before running the pipeline.
Trigger workflow run
