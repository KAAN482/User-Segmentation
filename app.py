from flask import Flask, request, jsonify, send_file
import os
from validator import validate_input
from evaluator import evaluate_rules

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """
    Root endpoint. Returns a welcome message.
    """
    return "<h1>Project Active!</h1><p>Go to <a href='/evaluate'>/evaluate</a> to test.</p>"

@app.route('/evaluate', methods=['GET'])
def evaluate_get():
    """
    Serves the test.html file for browser-based testing.
    """
    try:
        return send_file('test.html')
    except Exception as e:
        return str(e), 404

@app.route('/evaluate', methods=['POST'])
def evaluate_post():
    """
    Main evaluation endpoint.
    Receives user data and segment rules in JSON format.
    Returns the evaluation results (True/False) for each segment.
    """
    try:
        data = request.get_json()
        
        # 1. Validate Input
        # Ensure 'user' and 'segments' keys exist
        is_valid, error_msg = validate_input(data)
        if not is_valid:
            # Return 400 Bad Request if validation fails
            return jsonify({"error": error_msg}), 400

        user_data = data['user']
        segments = data['segments']

        # 2. Evaluate Rules
        try:
            # Delegate logic to the evaluator module
            results = evaluate_rules(user_data, segments)
            return jsonify({"results": results})
            
        except ValueError as e:
            # Handle specific invalid rule errors from the evaluator (SQL syntax errors)
            return jsonify({"error": str(e)}), 400
            
        except Exception as e:
            # Handle unexpected errors during evaluation
            return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle general server errors
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Get port from environment variable or default to 3000
    # This is critical for deployments (e.g. Heroku, Docker) where the port is assigned dynamically.
    port = int(os.environ.get('PORT', 3000))
    
    # Host must be '0.0.0.0' to make the server accessible from outside the container.
    app.run(host='0.0.0.0', port=port, debug=True)


