# SQL Data Reconciliation Framework

## 📌 Overview

This project provides a reusable framework to validate and reconcile data between **source and target systems** using SQL-based validation techniques.

It helps ensure **data accuracy, consistency, and completeness** in ETL pipelines and data migration processes.

---

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

```bash id="n1i0bx"
pytest
```

Generate HTML report:

```bash id="c0g39j"
pytest --html=reports/report.html
```

---

## 📊 Example Validation

- Compare row counts between source and target
- Validate no missing or null values
- Ensure aggregated values match

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

## 💡 Use Cases

- ETL testing
- Data migration validation
- Data warehouse testing
- Data quality checks

---

## 🚧 Future Improvements

- Support for multiple databases (Snowflake, Redshift, etc.)
- Logging and monitoring
- Advanced reconciliation rules
- Dashboard/reporting integration

---
