"""Flask application factory."""

from flask import Flask

from .config import config_by_name
from .models import db


def create_app(config_name: str = "default") -> Flask:
    """Application factory used to create app instances.

    Parameters
    ----------
    config_name: str
        The configuration name to use. Defaults to "default" which
        loads configuration from environment variables.
    """
    app = Flask(__name__)
    config_class = config_by_name.get(config_name, config_by_name["default"])
    app.config.from_object(config_class)

    # Initialize database
    db.init_app(app)

    # Register blueprints
    from .routes.farms import farms_bp
    app.register_blueprint(farms_bp, url_prefix="/api/farms")

    return app
