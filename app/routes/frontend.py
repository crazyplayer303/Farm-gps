from flask import Blueprint, send_from_directory
import os

frontend_bp = Blueprint("frontend", __name__)

@frontend_bp.route("/")
def home():
    return send_from_directory(
        os.path.join(os.path.dirname(__file__), "../../static"),
        "avocadoFarms.html"
    )
