# User Segmentation Engine

A lightweight, Dockerized Python service for evaluating users against dynamic SQL-like segmentation rules. Built with Flask and in-memory SQLite.

## Project Structure

```
├─ app.py                # Main Flask application
├─ evaluator.py          # SQL rule evaluation engine
├─ validator.py          # Input validation logic
├─ test.html             # Browser-based testing UI
├─ examples/             # JSON examples for testing
├─ manual_tests.md       # Curl/PowerShell test commands
├─ Dockerfile            # Docker configuration
└─ requirements.txt      # Python dependencies
```

## Features
- **Dynamic Rules**: Define segmentation logic using SQL syntax (e.g., `level > 10`).
- **In-Memory Evaluation**: Uses SQLite for fast, on-the-fly evaluation without persistent storage.
- **Custom Functions**: Supports `_now()` for time-based comparisons.
- **Docker Ready**: Ready for containerized deployment with dynamic port configuration.

## Installation & Running

### 1. Local Python Environment
```bash
# Create and activate venv
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```
The server will start on port **3000** (default).

### 2. Docker
```bash
# Build the image
docker build -t user-segmentation .

# Run the container (mapping port 3000)
docker run -p 3000:3000 user-segmentation
```

## Testing

### Browser UI (Recommended)
1. Go to `http://localhost:3000/evaluate`.
2. You will see a split-pane JSON editor.
3. You can copy-paste JSON content from the `examples/` folder to test different scenarios.

### Manual API Testing
Refer to `manual_tests.md` for `curl` and PowerShell commands.

## API Usage

**POST** `/evaluate`

**Input:**
```json
{
    "user": { "level": 15, "country": "TR" },
    "segments": {
        "is_vip": "level > 10"
    }
}
```

**Output:**
```json
{
    "results": {
        "is_vip": true
    }
}
```
