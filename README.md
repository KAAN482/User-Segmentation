# User Segmentation Project

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

The server will start on port 3000.

### Endpoints

- `GET /evaluate`: Returns the `test.html` page.
- `POST /evaluate`: Accepts JSON data, prints it, and returns `{"status": "pending"}`.
