from flask import Flask, request, jsonify, send_file
import os
from validator import validate_input
from evaluator import evaluate_rules

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
    Evaluates user against a set of SQL-like rules.
    """
    try:
        data = request.get_json()
        
        # Validation
        is_valid, error_msg = validate_input(data)
        if not is_valid:
            if "Invalid input." in error_msg and "key is required" in error_msg:
                 return jsonify({"error": error_msg}), 400
            # Keeping consistent with original logic handling
            return jsonify({"error": error_msg}), 400

        user_data = data['user']
        segments = data['segments']

        # Evaluation
        try:
            results = evaluate_rules(user_data, segments)
            return jsonify({"results": results})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            # Re-raise for general 500 handler or handle safely
            return jsonify({"error": str(e)}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Get port from environment variable or default to 3000
    # This is critical for deployments (e.g. Heroku, Docker) where the port is assigned dynamically.
    port = int(os.environ.get('PORT', 3000))
    
    # Host must be '0.0.0.0' to make the server accessible from outside the container.
    app.run(host='0.0.0.0', port=port, debug=True)


