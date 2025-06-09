# Farm GPS

This project provides tools for working with farm data in Queensland. The `server.py` file exposes a small REST API backed by a SQLite database.

## Requirements

Install the dependencies with pip:

```bash
pip install flask flask_sqlalchemy geopy
```

## Running the API

The Flask server creates `app.db` on first start. Run:

```bash
python3 server.py
```

The API exposes the following routes:

- `GET /api/farms` – list farms (optional query parameter `q` performs a simple search on name or region).
- `POST /api/farms` – add a new farm. Provide JSON with at least `name`. If `lat`/`lng` are missing but an `address` is supplied, the address will be geocoded.
