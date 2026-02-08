# User Segmentation Engine 🚀

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)

A high-performance, lightweight microservice for evaluating users against dynamic segmentation rules. Built with **Flask** and powered by **In-Memory SQLite** for rapid rule processing.

## 📖 Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Docker Deployment](#docker-deployment)

---

## 🧐 Overview
This project solves the problem of dynamically categorizing users into segments based on real-time data. Instead of hardcoding rules, it accepts SQL-like conditions (e.g., `level > 10` or `country = 'TR'`) and evaluates them on the fly against a user object.

It is designed to be:
- **Stateless:** No persistent database required.
- **Fast:** Uses SQLite in-memory mode (`:memory:`).
- **Flexible:** Supports complex logic (AND/OR, comparisons) and custom functions like `_now()`.

---

## ✨ Key Features
*   **Dynamic Rule Evaluation:** Rules are passed in the request, not hardcoded.
*   **SQL-Based Syntax:** Use standard SQL WHERE clauses for rules.
*   **Time-Aware:** Helper function `_now()` injects the current Unix timestamp for time-based segments (e.g., "last login < 7 days ago").
*   **Input Validation:** Robust checking of JSON payloads.
*   **Visual Testing UI:** Built-in split-pane HTML interface for easy testing.

---

## 🏗 Project Architecture

The codebase is modularized for maintainability:

```plaintext
User-Segmentation/
├── app.py                # 🚀 Entry point. Defines Flask routes and error handling.
├── evaluator.py          # 🧠 Core Logic. detailed SQL evaluation engine.
├── validator.py          # 🛡️ Validation Layer. Checks input integrity.
├── test.html             # 🎨 Frontend. A modern UI for testing API payloads.
├── Dockerfile            # 🐳 Container configuration.
├── requirements.txt      # 📦 Python dependencies.
├── manual_tests.md       # 🧪 Reference for curl/PowerShell commands.
└── examples/             # 📂 Sample JSON payloads for quick testing.
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Local Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KAAN482/User-Segmentation.git
    cd User-Segmentation
    ```

2.  **Create a Virtual Environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```
    The server will start at `http://localhost:3000`.

---

## 🚀 Usage

### Browser UI (Recommended)
This is the easiest way to interact with the API.

1.  Start the server.
2.  Navigate to [http://localhost:3000/evaluate](http://localhost:3000/evaluate).
3.  You will see a JSON editor. Paste a sample JSON (prom `examples/` folder) and click **"Test Et"**.
4.  View results instantly in the right pane.

### API Endpoints

#### `GET /`
Returns a welcome message verifying the service is active.

#### `GET /evaluate`
Serves the testing UI (`test.html`).

#### `POST /evaluate`
The core endpoint. Accepts a JSON body containing user data and segmentation rules.

**Request Body:**
```json
{
    "user": {
        "id": 101,
        "level": 15,
        "country": "Turkey",
        "last_login": 1700000000
    },
    "segments": {
        "is_vip": "level > 10",
        "is_tr": "country = 'Turkey'",
        "active_recently": "last_login > _now() - 86400"
    }
}
```

**Response:**
```json
{
    "results": {
        "is_vip": true,
        "is_tr": true,
        "active_recently": false
    }
}
```

---

## 🐳 Docker Deployment

You can containerize this application for production deployment.

### 1. Build the Image
```bash
docker build -t user-segmentation .
```

### 2. Run the Container
```bash
# Run on port 3000
docker run -p 3000:3000 user-segmentation

# Run on a different port (e.g. 4000)
docker run -p 4000:3000 -e PORT=3000 user-segmentation
```

---

## 🧪 Testing

### Manual Testing
Refer to `manual_tests.md` for specific command-line instructions using:
- **PowerShell** (`Invoke-RestMethod`)
- **CMD** (`curl`)

### Sample Data
Check the `examples/` directory for ready-to-use JSON files:
- `basic_comparison.json`: Simple numeric checks.
- `case_sensitivity.json`: Testing string matching.
- `multiple_conditions.json`: Complex logic with AND/OR.

---

## 📝 License
This project is open-source and available for educational purposes.
