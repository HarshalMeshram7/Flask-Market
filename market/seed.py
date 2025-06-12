from market import db
from market.models import Item
from market import app

# Seed data
items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500, 'description': 'Smartphone with 64GB storage'},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900, 'description': '15-inch laptop with 16GB RAM'},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150, 'description': 'Mechanical keyboard with RGB'}
]

# Insert data using app context
with app.app_context():
    db.create_all()  # Ensures tables are created
    if not Item.query.first():  # Avoid duplicate inserts
        for item_data in items:
            item = Item(**item_data)
            db.session.add(item)
        db.session.commit()
        print("Database seeded successfully!")
    else:
        print("Items already exist in the database.")
