# SQL Data Reconciliation Framework

## 📌 Overview

This project provides a reusable framework to validate and reconcile data between **source and target systems** using SQL-based validation techniques.

It helps ensure **data accuracy, consistency, and completeness** in ETL pipelines and data migration processes.

## “This framework simulates production-grade data validation by decoupling database dependencies using mocks.”

## 🚀 Features

- Row count validation between source and target
- Data comparison checks
- Config-driven reconciliation
- Modular and reusable architecture
- Automated testing using pytest
- HTML test reporting support

---

## 🏗️ Project Structure

```id="p5j5h1"
sql-data-reconciliation-framework/
│
├── src/
│   ├── db_connection.py        # Handles DB connections
│   ├── reconciliation.py       # Core reconciliation logic
│
├── tests/
│   ├── conftest.py             # Pytest setup & fixtures
│   ├── test_reconciliation.py  # Test cases
│
├── config/
│   └── reconciliation_config.json   # Config-driven inputs
│
├── .github/workflows/
│   └── test.yml               # CI pipeline (pytest execution)
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. Load configuration from `reconciliation_config.json`
2. Connect to source and target systems
3. Execute validation queries
4. Compare results:
   - Row counts
   - Aggregations
   - Data consistency checks

5. Return reconciliation results

---

## 🧪 Running Tests

Run tests locally:

```
pytest
```

Generate HTML report:

```
pytest --html=reports/report.html
```

---

## 🛠️ Tech Stack

- Python
- SQL
- Pytest
- GitHub Actions (CI)

---

## 🔄 CI/CD Integration

This project includes a GitHub Actions workflow:

- Runs tests on every push
- Generates validation results automatically

---
