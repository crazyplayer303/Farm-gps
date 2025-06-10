"""Database models for the application."""

from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy instance; created here so it can be imported by modules
# without causing circular imports.
db = SQLAlchemy()

class Farm(db.Model):
    """Represents a farm record."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    area = db.Column(db.Float)
    region = db.Column(db.String(100))
    established = db.Column(db.Integer)
    type = db.Column(db.String(100))
