# DataOps CI/CD Assignment

This repository contains a simple ETL pipeline for cleaning customer data, along with Docker and test support.

## Repository Structure

- `src/etl.py` - ETL script that reads `data/customers.csv`, drops rows with missing values, and writes the cleaned output to `data/processed/cleaned_customers.csv`.
- `data/customers.csv` - raw customer dataset.
- `data/processed/` - output directory for processed data.
- `requirements.txt` - Python dependencies for the ETL pipeline.
- `Dockerfile` - container definition for running the ETL pipeline in Docker.
- `tests/test_elt.py` - basic validation to ensure the cleaned CSV has no null values.
- `terraform/` - infrastructure-related files for demonstration.

## Requirements

- Python 3.12+ (Dockerfile uses `python:3.12.4-slim`)
- `pandas`

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the ETL pipeline

```bash
python src/etl.py
```

The script reads `data/customers.csv` and writes cleaned data to `data/processed/cleaned_customers.csv`.

## Run tests

```bash
pytest
```

## Run with Docker

```bash
docker build -t dataops-etl .
docker run --rm dataops-etl
```

## Notes

- The current ETL process only removes rows with missing values.
- Update `src/etl.py` to extend transformation logic or add validation steps.
