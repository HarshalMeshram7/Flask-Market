from market import app, db, Item

with app.app_context():
    # item1 = Item(name='Phone', barcode='893212299897', price=500, description='A smartphone')
    # item2 = Item(name='Laptop', barcode='123985473165', price=900, description='A powerful laptop')
    # item3 = Item(name='Keyboard', barcode='231985128446', price=150, description='A mechanical keyboard')

    # db.session.add_all([item1, item2, item3])
    # db.session.commit()
    Item.query.all()
    # print("Items added.")

# with app.app_context():
#     db.create_all()
