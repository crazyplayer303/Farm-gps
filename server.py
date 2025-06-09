from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from geopy.geocoders import Nominatim

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    region = db.Column(db.String(120))
    area = db.Column(db.Float)
    year_established = db.Column(db.Integer)
    address = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'lat': self.lat,
            'lng': self.lng,
            'region': self.region,
            'area': self.area,
            'year_established': self.year_established,
            'address': self.address,
        }

# Initialize database
with app.app_context():
    db.create_all()

geolocator = Nominatim(user_agent="farm_api")

@app.route('/api/farms', methods=['GET'])
def get_farms():
    q = request.args.get('q')
    query = Farm.query
    if q:
        like = f"%{q}%"
        query = query.filter(db.or_(Farm.name.ilike(like), Farm.region.ilike(like)))
    farms = [farm.to_dict() for farm in query.all()]
    return jsonify(farms)

@app.route('/api/farms', methods=['POST'])
def add_farm():
    data = request.get_json() or {}
    name = data.get('name')
    if not name:
        return jsonify({'error': 'name is required'}), 400
    lat = data.get('lat')
    lng = data.get('lng')
    address = data.get('address')
    if (not lat or not lng) and address:
        location = geolocator.geocode(address)
        if location:
            lat = location.latitude
            lng = location.longitude
    farm = Farm(
        name=name,
        lat=lat,
        lng=lng,
        region=data.get('region'),
        area=data.get('area'),
        year_established=data.get('year_established'),
        address=address,
    )
    db.session.add(farm)
    db.session.commit()
    return jsonify(farm.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
