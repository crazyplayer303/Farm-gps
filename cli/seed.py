"""Command line tool for seeding the database with farm data."""

import argparse
import json
from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.models import db, Farm
from app.services.fetcher import FarmDataFetcher


def load_json(path: Path):
    """Load farm records from a JSON file."""
    with path.open() as f:
        return json.load(f)


def seed_farms(records):
    """Insert a list of farm dictionaries into the database."""
    for record in records:
        farm = Farm(**record)
        db.session.add(farm)
    db.session.commit()


def main():
    parser = argparse.ArgumentParser(description="Seed farm data into the database")
    parser.add_argument("--file", type=Path, help="Path to JSON file containing farms")
    parser.add_argument("--fetch", choices=["abares"], help="Fetch farms from external source")
    args = parser.parse_args()

    app = create_app()
    with app.app_context():
        db.create_all()
        records = []
        if args.file:
            records = load_json(args.file)
        elif args.fetch:
            fetcher = FarmDataFetcher()
            fetcher.fetch_from_apis()
            records = fetcher.farms_data
        else:
            parser.error("Specify --file or --fetch")

        seed_farms(records)
        print(f"Seeded {len(records)} farms")


if __name__ == "__main__":
    main()
