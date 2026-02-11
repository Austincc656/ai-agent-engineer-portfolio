import sqlite3
from typing import List, Tuple, Any


def connect(db_path: str) -> sqlite3.Connection:
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    return con


def get_schema(con: sqlite3.Connection) -> str:
    q_tables = "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
    tables = [r["name"] for r in con.execute(q_tables).fetchall()]
    lines = []
    for t in tables:
        cols = con.execute(f"PRAGMA table_info({t});").fetchall()
        col_str = ", ".join([f"{c['name']} ({c['type']})" for c in cols])
        lines.append(f"- {t}: {col_str}")
    return "\n".join(lines) if lines else "(no tables found)"


def run_readonly_sql(con: sqlite3.Connection, sql: str) -> Tuple[List[str], List[List[Any]]]:
    cleaned = sql.strip().lower()
    if not cleaned.startswith("select"):
        raise ValueError("Only SELECT queries are allowed in this MVP.")

    cur = con.execute(sql)
    rows = cur.fetchall()
    columns = [d[0] for d in cur.description] if cur.description else []
    data = [[row[c] for c in columns] for row in rows]
    return columns, data
