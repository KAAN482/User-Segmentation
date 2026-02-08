from flask import Flask, request, jsonify, send_file
import os
import sqlite3
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Project Active!</h1><p>Go to <a href='/evaluate'>/evaluate</a> to test.</p>"

@app.route('/evaluate', methods=['GET'])
def evaluate_get():
    """
    Serves the test.html file.
    """
    try:
        return send_file('test.html')
    except Exception as e:
        return str(e), 404

@app.route('/evaluate', methods=['POST'])
def evaluate_post():
    """
    Evaluates user against a set of SQL-like rules using in-memory SQLite.
    Expected JSON:
    {
        "user": {"id": 1, "level": 10, "country": "TR", ...},
        "segments": {"segment1": "level > 5", "segment2": "country = 'TR'", ...}
    }
    """
    try:
        data = request.get_json()
        if not data or 'user' not in data or 'segments' not in data:
            return jsonify({"error": "Invalid input. 'user' and 'segments' are required."}), 400

        user_data = data['user']
        segments = data['segments']

        # Connect to in-memory database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        # Dynamically create table based on user keys
        # We assume keys are safe (simple strings) and values determine types
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
            # Using simple replacement for now. 
            # Note: This replaces all occurrences of '_now()' string.
            effective_rule = rule.replace("_now()", str(current_time))

            try:
                # Check if user matches the rule
                query = f"SELECT 1 FROM users WHERE {effective_rule}"
                cursor.execute(query)
                match = cursor.fetchone()
                results[segment_name] = True if match else False
            except sqlite3.Error as e:
                # If a rule is invalid SQL, we can either fail partially or totally.
                # Here we mark it as error or return 400. 
                # Let's return 400 for the whole request per user spec "catch SQL error... return 400"
                conn.close()
                print(f"SQL Error in rule '{segment_name}': {e}")
                return jsonify({"error": f"Invalid rule in segment '{segment_name}': {str(e)}"}), 400

        conn.close()
        return jsonify({"results": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Running on port 3000 as requested
    app.run(port=3000, debug=True)

