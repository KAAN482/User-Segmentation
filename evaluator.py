import sqlite3
import time

def evaluate_rules(user_data, segments):
    """
    Evaluates user against a set of SQL-like rules using in-memory SQLite.
    Returns a dictionary of segment results or raises an exception on error.
    """
    # Connect to in-memory database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    try:
        # Dynamically create table based on user keys
        columns = []
        values = []
        placeholders = []
        
        for key, value in user_data.items():
            if isinstance(value, int):
                col_type = "INTEGER"
            elif isinstance(value, float):
                col_type = "REAL"
            else:
                col_type = "TEXT"
            columns.append(f"{key} {col_type}")
            values.append(value)
            placeholders.append("?")

        create_table_sql = f"CREATE TABLE users ({', '.join(columns)})"
        cursor.execute(create_table_sql)

        # Insert user data
        insert_sql = f"INSERT INTO users ({', '.join(user_data.keys())}) VALUES ({', '.join(placeholders)})"
        cursor.execute(insert_sql, values)

        # Evaluate segments
        results = {}
        current_time = int(time.time())

        for segment_name, rule in segments.items():
            # Replace _now() with current timestamp
            effective_rule = rule.replace("_now()", str(current_time))

            try:
                # Check if user matches the rule
                query = f"SELECT 1 FROM users WHERE {effective_rule}"
                cursor.execute(query)
                match = cursor.fetchone()
                results[segment_name] = True if match else False
            except sqlite3.Error as e:
                # Re-raise with context
                raise ValueError(f"Invalid rule in segment '{segment_name}': {str(e)}")

        return results

    finally:
        conn.close()
