"""Blueprint providing /api/farms endpoints."""

from flask import Blueprint, request, jsonify
from sqlalchemy import or_

from ..models import db, Farm

farms_bp = Blueprint("farms", __name__)


@farms_bp.route("/", methods=["GET"])
def list_farms():
    """Return a paginated list of farms with optional filters."""
    query = Farm.query
    search = request.args.get("search", type=str, default="")
    farm_type = request.args.get("type", type=str, default="")
    sort = request.args.get("sort", default="id")
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=20, type=int)

    if search:
        like = f"%{search}%"
        query = query.filter(or_(Farm.name.ilike(like), Farm.region.ilike(like)))
    if farm_type:
        query = query.filter_by(type=farm_type)

    sort_field = sort.lstrip("-")
    if sort_field not in Farm.__table__.columns.keys():
        return jsonify({"error": f"Invalid sort field '{sort_field}'"}), 400

    attr = getattr(Farm, sort_field)
    query = query.order_by(attr.desc() if sort.startswith("-") else attr.asc())

    pagination = query.paginate(page=page, per_page=limit, error_out=False)
    farms = [
        {
            "id": farm.id,
            "name": farm.name,
            "lat": farm.lat,
            "lng": farm.lng,
            "area": farm.area,
            "region": farm.region,
            "established": farm.established,
            "type": farm.type,
        }
        for farm in pagination.items
    ]

    return jsonify({
        "items": farms,
        "total": pagination.total,
        "page": page,
        "pages": pagination.pages,
    })


@farms_bp.route("/", methods=["POST"])
def create_farm():
    """Create a new farm from the posted JSON body."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    try:
        farm = Farm(
            name=data["name"],
            lat=float(data["lat"]),
            lng=float(data["lng"]),
            area=data.get("area"),
            region=data.get("region"),
            established=data.get("established"),
            type=data.get("type"),
        )
    except (KeyError, ValueError):
        return jsonify({"error": "Invalid farm data"}), 400

    db.session.add(farm)
    db.session.commit()
    return jsonify({"id": farm.id}), 201
