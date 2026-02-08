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

## Docker Support

You can also run this application using Docker.

### Build the Image
```bash
docker build -t user-segmentation .
```

### Run the Container
```bash
# Run on port 3000
docker run -p 3000:3000 user-segmentation

# Run on a different port (e.g., 4000) mapped to internal 3000
# Note: You can also override the internal PORT env var if needed: -e PORT=4000
docker run -p 4000:3000 user-segmentation
```

