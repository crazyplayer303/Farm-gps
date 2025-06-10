# Farm GPS Backend

This project demonstrates a small Flask API for listing farms in Queensland. The
code is structured using an application factory so it can easily be reused in
other projects.

## Setup

1. Create a virtual environment and install dependencies.
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env` and adjust any settings (for example the database URL).

## Running the API

Use the provided `run.py` entry point:
```bash
python run.py
```

## Seeding Data

You can seed the database with sample data located in `data/sample_farms.json`:
```bash
python cli/seed.py --file data/sample_farms.json
```

The seeder can also call the (mock) `FarmDataFetcher` service:
```bash
python cli/seed.py --fetch abares
```

## Running Tests

Tests live in the `tests/` folder and can be executed with:
```bash
pytest
```
