from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

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
    Receives JSON data, prints it to console, and returns a dummy status.
    """
    data = request.get_json()
    print(f"Received data: {data}")
    return jsonify({"status": "pending"})

if __name__ == "__main__":
    # Running on port 3000 as requested
    app.run(port=3000, debug=True)

