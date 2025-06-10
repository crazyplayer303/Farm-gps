# Farm GPS

This repository contains a minimal example for displaying farm locations in Queensland.
It includes a static HTML map and a simple Flask backend with a SQLite database.

## Requirements

- Python 3.9+
- `pip` for installing Python packages

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This installs Flask, Flask-SQLAlchemy and other utilities used by the project.

## Running the server

Start the Flask server from the project root:

```bash
python server.py
```

The application will create a local SQLite database file `farms.db` if it does not already exist.
By default the server listens on `http://localhost:5000/`.
Opening that URL in a browser will display `avocadoFarms.html`.
Run `python seed_data.py` once to populate the database with sample farms.

You can also open the HTML page directly without running the server by opening
`avocadoFarms.html` in a web browser, but the API to store farms will only be
available when the server is running.

## Example API usage

List all stored farms:

```bash
curl http://localhost:5000/api/farms
```

Search farms by name or region:

```bash
curl "http://localhost:5000/api/farms?search=coast"
```

Filter by farm type (e.g. only strawberry farms):

```bash
curl "http://localhost:5000/api/farms?type=Strawberry"
```

Add a new farm record:

```bash
curl -X POST http://localhost:5000/api/farms \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Example Farm",
        "lat": -27.0,
        "lng": 153.0,
        "area": 50,
        "region": "Test Region",
        "established": 2020
        "type": "Avocado"
      }'
```

When a farm is added successfully, the API returns the new record ID.

## Development notes

The backend logic for fetching real agricultural data is in `backend.py` and is
separate from the Flask server in `server.py`. Currently `backend.py` only
contains example code and does not communicate with the API.
