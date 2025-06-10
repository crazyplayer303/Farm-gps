from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    area = db.Column(db.Float)
    region = db.Column(db.String(100))
    established = db.Column(db.Integer)
    type = db.Column(db.String(100))

@app.route('/api/farms', methods=['GET'])
def get_farms():
    query = Farm.query
    search = request.args.get('search', '').strip()
    farm_type = request.args.get('type', '').strip()
    
    if search:
        like = f"%{search}%"
        query = query.filter(or_(Farm.name.ilike(like), Farm.region.ilike(like)))
    if farm_type:
        query = query.filter_by(type=farm_type)
    
    farms = query.all()
    return jsonify([
        {
            'id': farm.id,
            'name': farm.name,
            'lat': farm.lat,
            'lng': farm.lng,
            'area': farm.area,
            'region': farm.region,
            'established': farm.established,
            'type': farm.type
        }
        for farm in farms
    ])

@app.route('/api/farms', methods=['POST'])
def add_farm():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400
    farm = Farm(
        name=data.get('name'),
        lat=data.get('lat'),
        lng=data.get('lng'),
        area=data.get('area'),
        region=data.get('region'),
        established=data.get('established'),
        type=data.get('type')
    )
    db.session.add(farm)
    db.session.commit()
    return jsonify({'message': 'Farm added', 'id': farm.id})

@app.route('/')
def index():
    return send_from_directory('.', 'avocadoFarms.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
