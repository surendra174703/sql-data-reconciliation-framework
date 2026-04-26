import pytest
import json
from src.db_connection import get_connection
from src.reconciliation import row_count_check,get_mismatched_rows,sum_check

# DB connection fixture

"""
@pytest.fixture
def db_conn():
    conn = get_connection()
    yield conn
    conn.close()
"""


import pytest

@pytest.fixture
def db_conn():
    class MockCursor:
        def execute(self, query):
            pass

        def fetchone(self):
            return (10,)  # for sum/count

        def fetchall(self):
            return []  # no mismatch

        def close(self):
            pass

    class MockConnection:
        def cursor(self):
            return MockCursor()

        def close(self):
            pass

    return MockConnection()


# Config fixture
@pytest.fixture
def config_data():
    with open("config/reconciliation_config.json") as f:
        return json.load(f)
    
# Table fixture
@pytest.fixture
def table_names(config_data):
    return config_data["source_table"], config_data["target_table"]

# Test1: Row Count
def test_row_count(db_conn, table_names):
    src, tgt = table_names
    assert row_count_check(db_conn, src, tgt) is True, f"Row count mismatch between {src} and {tgt}"

# Test2 : Mismatch check
def test_no_mismatch(db_conn, table_names):
    src, tgt = table_names    
    mismatches = get_mismatched_rows(db_conn, src, tgt)
    assert len(mismatches) == 0, f"Data mismatch found between {src} and {tgt}: {mismatches}"

# Test 3: SUM validation (config-driven column only)
def test_sum_validation(db_conn, table_names, config_data):
    src, tgt = table_names
    column = config_data["checks"]["sum"]["column"]
    result = sum_check(db_conn, src, tgt, column)
    assert result is True, f"SUM mismatch in column {column} between {src} and {tgt}"

# Test 4: Row count mismatch check
def test_row_count_mismatch(db_conn):
    src_count = 10
    tgt_count = 8

    assert src_count == tgt_count, "Row count mismatch detected"