from src.db_connection import get_connection


def row_count_check(conn, src_table, tgt_table):
    cur = conn.cursor()

    cur.execute(f"SELECT COUNT(*) FROM {src_table}")
    src_count = cur.fetchone()[0]

    cur.execute(f"SELECT COUNT(*) FROM {tgt_table}")
    tgt_count = cur.fetchone()[0]

    print(f"{src_table} count:", src_count)
    print(f"{tgt_table} count:", tgt_count)

    cur.close()

    return src_count == tgt_count


def get_mismatched_rows(conn, src_table, tgt_table):
    cur = conn.cursor()

    query = f"""
    SELECT * FROM {src_table}
    EXCEPT
    SELECT * FROM {tgt_table}
    """
    cur.execute(query)
    rows = cur.fetchall()

    print("Mismatched Rows:", rows)

    cur.close()
    return rows


# Aggregation check (SUM)
def sum_check(conn, src_table, tgt_table, column):
    cur = conn.cursor()

    cur.execute(f"SELECT SUM({column}) FROM {src_table}")
    src_sum = cur.fetchone()[0]

    cur.execute(f"SELECT SUM({column}) FROM {tgt_table}")
    tgt_sum = cur.fetchone()[0]

    print(f"{src_table} {column} sum:", src_sum)
    print(f"{tgt_table} {column} sum:", tgt_sum)

    cur.close()

    return src_sum == tgt_sum