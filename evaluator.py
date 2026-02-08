import sqlite3
import time

def evaluate_rules(user_data, segments):
    """
    Evaluates user against a set of SQL-like rules using in-memory SQLite.
    Returns a dictionary of segment results or raises an exception on error.
    
    Args:
        user_data (dict): Dictionary containing user attributes (e.g., id, level).
        segments (dict): Dictionary of segment names and their SQL WHERE clauses.
        
    Returns:
        dict: A dictionary mapping segment names to booleans (True/False).
    """
    # Connect to in-memory database.
    # We use :memory: to ensure fastest performance and no persistence requirements.
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    try:
        # 1. Dynamically create table based on user keys
        # We determine the schema on-the-fly based on the input data types.
        columns = []
        values = []
        placeholders = []
        
        for key, value in user_data.items():
            # infer SQLite type from Python type
            if isinstance(value, int):
                col_type = "INTEGER"
            elif isinstance(value, float):
                col_type = "REAL"
            else:
                col_type = "TEXT"
            columns.append(f"{key} {col_type}")
            values.append(value)
            placeholders.append("?")

        # Create the 'users' table
        create_table_sql = f"CREATE TABLE users ({', '.join(columns)})"
        cursor.execute(create_table_sql)

        # 2. Insert user data into the table
        insert_sql = f"INSERT INTO users ({', '.join(user_data.keys())}) VALUES ({', '.join(placeholders)})"
        cursor.execute(insert_sql, values)

        # 3. Evaluate segments
        results = {}
        # Get current Unix timestamp for _now() replacement
        current_time = int(time.time())

        for segment_name, rule in segments.items():
            # Replace custom _now() function with current timestamp
            effective_rule = rule.replace("_now()", str(current_time))

            try:
                # Execute the rule as a SQL WHERE clause
                query = f"SELECT 1 FROM users WHERE {effective_rule}"
                cursor.execute(query)
                match = cursor.fetchone()
                
                # If a row is returned, the condition is True
                results[segment_name] = True if match else False
                
            except sqlite3.Error as e:
                # If SQL syntax is invalid, raise a ValueError to be handled upstream
                raise ValueError(f"Invalid rule in segment '{segment_name}': {str(e)}")

        return results

    finally:
        # Always close the connection to free memory
        conn.close()
