from server import app, db, Farm

sample_farms = [
    {
        'name': 'Sunshine Coast Avocados',
        'lat': -26.6267,
        'lng': 152.9593,
        'area': 45,
        'region': 'Sunshine Coast',
        'established': 2010,
        'type': 'Avocado'
    },
    {
        'name': 'Atherton Strawberries',
        'lat': -17.2686,
        'lng': 145.4743,
        'area': 30,
        'region': 'Atherton',
        'established': 2005,
        'type': 'Strawberry'
    },
    {
        'name': 'Bundaberg Berries',
        'lat': -24.8662,
        'lng': 152.3499,
        'area': 75,
        'region': 'Bundaberg',
        'established': 2012,
        'type': 'Blueberry'
    }
]

with app.app_context():
    db.create_all()
    if not Farm.query.first():
        for data in sample_farms:
            farm = Farm(**data)
            db.session.add(farm)
        db.session.commit()
        print('Seeded database with sample farms')
    else:
        print('Database already has data')
