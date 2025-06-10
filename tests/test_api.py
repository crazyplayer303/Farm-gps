import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
"""Basic API tests for the farms endpoints."""

import pytest

from app import create_app
from app.models import db, Farm


@pytest.fixture
def client():
    """Test client with an in-memory database."""
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        # create an initial farm
        db.session.add(Farm(name="Initial Farm", lat=1.0, lng=1.0))
        db.session.commit()
    with app.test_client() as client:
        yield client


def test_get_farms(client):
    """GET request should return the seeded farm."""
    res = client.get("/api/farms/")
    assert res.status_code == 200
    data = res.get_json()
    assert data["total"] == 1


def test_create_farm(client):
    """POST should create a new farm and return its id."""
    res = client.post(
        "/api/farms/",
        json={"name": "New Farm", "lat": 10.0, "lng": 20.0},
    )
    assert res.status_code == 201
    farm_id = res.get_json()["id"]
    assert isinstance(farm_id, int)


def test_search_filter(client):
    """Search query should filter farms by name."""
    client.post(
        "/api/farms/",
        json={"name": "Berry Farm", "lat": 5, "lng": 5, "type": "Berry"},
    )
    res = client.get("/api/farms/?search=Berry")
    assert res.status_code == 200
    data = res.get_json()
    assert data["total"] == 1
